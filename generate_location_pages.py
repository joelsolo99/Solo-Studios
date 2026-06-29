#!/usr/bin/env python3
"""Generate Solo Studios location pages.

Inputs:
  assets/data/location_venues.csv
  assets/data/location_copy.json

Outputs:
  _pages/locations/<location-slug>.html

Usage:
  python generate_location_pages.py
  python generate_location_pages.py --include-unpublished
  python generate_location_pages.py --include-unpublished --single plymouth
  python generate_location_pages.py --include-unpublished --single plymouth --refresh-image-cache

Behaviour:
  - Generates a page for every location_slug present in the CSV.
  - If location_copy.json has matching copy, uses it.
  - If location_copy.json does not have matching copy, creates safe fallback copy from the CSV.
  - Populates empty CSV columns with known or derived information.
  - Prefers existing local venue_image files on generated pages.
  - Never overwrites existing real venue_image_url values.
  - If venue_image_url is blank, discovers an image from venue_url.
  - If a real image URL exists or is discovered, downloads it and converts it to WebP.
  - Saves downloaded images to assets/img/locations/venues/<venue-name>.webp.
  - Updates venue_image to the local WebP path.
  - If no image URL can be found, writes "not found" to venue_image_url.
  - Existing "not found" rows are skipped unless --refresh-image-cache is used.
  - Supports any number of venues per location.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
import urllib.request
from html import unescape
from pathlib import Path
from urllib.parse import urljoin

ROOT = Path(__file__).resolve().parent
VENUE_CSV = ROOT / "assets" / "data" / "location_venues.csv"
LOCATION_COPY_JSON = ROOT / "assets" / "data" / "location_copy.json"
IMAGE_CACHE_JSON = ROOT / "assets" / "data" / "location_image_cache.json"
OUTPUT_DIR = ROOT / "_pages" / "locations"
LOCAL_VENUE_IMAGE_DIR = ROOT / "assets" / "img" / "locations" / "venues"

HERO_IMAGE = "/assets/img/photo_gallery/Party_Set.jpg"
HOMEPAGE_VIDEO = "/assets/video/intro_loop.mp4"
SERVICE_WEDDINGS_IMAGE = "/assets/img/homepage/1.webp"
SERVICE_PARTIES_IMAGE = "/assets/img/homepage/2.webp"
SERVICE_EVENTS_IMAGE = "/assets/img/homepage/3.webp"
SERVICE_POWER_HOUR_IMAGE = "/assets/img/homepage/blur.webp"

NOT_FOUND = "not found"
USER_AGENT = "Mozilla/5.0 (compatible; SoloStudiosLocationGenerator/1.0; +https://solostudios.uk)"

NEARBY_CHIPS = {
    "plymouth": ["Plymouth", "South Hams", "Ivybridge", "Tavistock", "Saltash", "Torpoint"],
    "devon": ["Plymouth", "Exeter", "Torquay", "Barnstaple", "Totnes", "Dartmouth"],
    "cornwall": ["Truro", "Newquay", "Falmouth", "St Ives", "Penzance", "Bodmin"],
    "dorset": ["Bournemouth", "Poole", "Dorchester", "Weymouth", "Bridport", "Sherborne"],
    "somerset": ["Bath", "Taunton", "Yeovil", "Wells", "Frome", "Glastonbury"],
    "bristol": ["Bristol", "Bath", "Clifton", "Redland", "Portishead", "Keynsham"],
    "exeter": ["Exeter", "Topsham", "Exmouth", "Crediton", "Honiton", "Newton Abbot"],
    "torquay": ["Torquay", "Paignton", "Brixham", "Newton Abbot", "Totnes", "Dartmouth"],
    "paignton": ["Paignton", "Torquay", "Brixham", "Totnes", "Newton Abbot", "Dartmouth"],
    "newton-abbot": ["Newton Abbot", "Torquay", "Totnes", "Teignmouth", "Dawlish", "Ashburton"],
    "barnstaple": ["Barnstaple", "Bideford", "Ilfracombe", "Braunton", "South Molton", "North Devon"],
    "exmouth": ["Exmouth", "Exeter", "Budleigh Salterton", "Topsham", "Sidmouth", "East Devon"],
    "tiverton": ["Tiverton", "Cullompton", "Crediton", "Exeter", "Mid Devon", "Taunton"],
    "dartmouth": ["Dartmouth", "Kingsbridge", "Totnes", "Salcombe", "Brixham", "South Hams"],
    "totnes": ["Totnes", "Dartmouth", "Kingsbridge", "Paignton", "Newton Abbot", "South Hams"],
    "truro": ["Truro", "Falmouth", "Newquay", "Redruth", "St Austell", "Mid Cornwall"],
    "newquay": ["Newquay", "Truro", "Perranporth", "Padstow", "St Austell", "Wadebridge"],
    "falmouth": ["Falmouth", "Truro", "Penryn", "Helston", "Redruth", "St Mawes"],
    "st-ives": ["St Ives", "Penzance", "Hayle", "Camborne", "Redruth", "West Cornwall"],
    "penzance": ["Penzance", "St Ives", "Marazion", "Mousehole", "Hayle", "West Cornwall"],
    "st-austell": ["St Austell", "Truro", "Bodmin", "Fowey", "Newquay", "Mid Cornwall"],
    "bodmin": ["Bodmin", "Wadebridge", "Liskeard", "St Austell", "Launceston", "Mid Cornwall"],
    "camborne": ["Camborne", "Redruth", "Hayle", "St Ives", "Penzance", "West Cornwall"],
    "redruth": ["Redruth", "Camborne", "Truro", "Falmouth", "Hayle", "West Cornwall"],
    "launceston": ["Launceston", "Bodmin", "Liskeard", "Tavistock", "North Cornwall", "Devon border"],
    "liskeard": ["Liskeard", "Bodmin", "Looe", "Saltash", "Launceston", "South East Cornwall"],
    "bath": ["Bath", "Frome", "Bristol", "Bradford-on-Avon", "Trowbridge", "Somerset"],
    "taunton": ["Taunton", "Bridgwater", "Wellington", "Tiverton", "Yeovil", "Somerset"],
    "yeovil": ["Yeovil", "Sherborne", "Dorchester", "Taunton", "Glastonbury", "South Somerset"],
    "weston-super-mare": ["Weston-super-Mare", "Bristol", "Clevedon", "Wells", "Bridgwater", "North Somerset"],
    "wells": ["Wells", "Glastonbury", "Frome", "Bath", "Shepton Mallet", "Somerset"],
    "frome": ["Frome", "Bath", "Wells", "Trowbridge", "Warminster", "Somerset"],
    "bridgwater": ["Bridgwater", "Taunton", "Burnham-on-Sea", "Glastonbury", "Wells", "Somerset"],
    "glastonbury": ["Glastonbury", "Wells", "Bridgwater", "Street", "Frome", "Somerset"],
    "bournemouth": ["Bournemouth", "Poole", "Christchurch", "Highcliffe", "Wimborne", "Dorset"],
    "poole": ["Poole", "Bournemouth", "Wimborne", "Wareham", "Swanage", "Dorset"],
    "dorchester": ["Dorchester", "Weymouth", "Bridport", "Sherborne", "Wareham", "Dorset"],
    "weymouth": ["Weymouth", "Dorchester", "Portland", "Bridport", "Wareham", "Dorset"],
    "bridport": ["Bridport", "Dorchester", "Lyme Regis", "Weymouth", "Beaminster", "Dorset"],
    "sherborne": ["Sherborne", "Yeovil", "Dorchester", "Bridport", "South Somerset", "Dorset"],
    "cheltenham": ["Cheltenham", "Gloucester", "Cotswolds", "Tewkesbury", "Cirencester", "Gloucestershire"],
    "gloucester": ["Gloucester", "Cheltenham", "Stroud", "Cotswolds", "Tewkesbury", "Gloucestershire"],
    "salisbury": ["Salisbury", "Amesbury", "Andover", "Warminster", "New Forest", "Wiltshire"],
    "swindon": ["Swindon", "Marlborough", "Cirencester", "Chippenham", "Cotswolds", "Wiltshire"],
}

REQUIRED_VENUE_FIELDS = [
    "location_slug",
    "location_name",
    "publish",
    "rank",
    "venue_name",
    "venue_url",
    "venue_note",
    "venue_image",
    "venue_image_url",
    "source_note",
]


def slugify(value: object) -> str:
    text = str(value or "").strip().lower()
    text = text.replace("&", "and")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "venue"


def normalise_slug(value: object) -> str:
    return slugify(value)


def display_name_from_slug(slug: str) -> str:
    small_words = {"and", "of", "the"}
    parts = slug.split("-")
    titled = []
    for index, part in enumerate(parts):
        if index > 0 and part in small_words:
            titled.append(part)
        else:
            titled.append(part.capitalize())
    return " ".join(titled)


def is_not_found_marker(value: str) -> bool:
    return str(value or "").strip().lower() == NOT_FOUND


def is_real_image_url(value: str) -> bool:
    value = str(value or "").strip()
    return bool(value) and not is_not_found_marker(value)


def esc(value: object) -> str:
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def liquid_url(path: str) -> str:
    return "{{ '" + path + "' | relative_url }}"


def root_relative_url(path: Path) -> str:
    return "/" + path.relative_to(ROOT).as_posix()


def local_path_from_csv(value: str) -> Path:
    return ROOT / str(value or "").strip().lstrip("/")


def existing_local_image_url(row: dict[str, str]) -> str:
    raw_path = str(row.get("venue_image", "") or "").strip()
    if not raw_path or raw_path.startswith(("http://", "https://")):
        return ""
    image_path = local_path_from_csv(raw_path)
    if image_path.exists():
        return root_relative_url(image_path)
    return ""


def preferred_local_image_path(row: dict[str, str]) -> Path:
    existing = existing_local_image_url(row)
    if existing:
        return local_path_from_csv(existing)

    location_slug = normalise_slug(row.get("location_slug", ""))
    venue_slug = slugify(row.get("venue_name", "venue"))
    filename = f"{location_slug}-{venue_slug}.webp" if location_slug else f"{venue_slug}.webp"
    target_path = LOCAL_VENUE_IMAGE_DIR / filename
    row["venue_image"] = target_path.relative_to(ROOT).as_posix()
    return target_path


def download_image_to_webp(image_url: str, output_path: Path) -> bool:
    try:
        from PIL import Image
    except ImportError as error:
        raise RuntimeError("Pillow is required. Install it with: python -m pip install pillow") from error

    request = urllib.request.Request(
        image_url,
        headers={"User-Agent": USER_AGENT, "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8"},
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        data = response.read()

    image = Image.open(io.BytesIO(data))
    try:
        image.seek(0)
    except EOFError:
        pass

    if image.mode in ("RGBA", "LA"):
        rgba = image.convert("RGBA")
        background = Image.new("RGB", rgba.size, (255, 255, 255))
        background.paste(rgba, mask=rgba.getchannel("A"))
        image = background
    else:
        image = image.convert("RGB")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path, "WEBP", quality=84, method=6)
    return output_path.exists()


def ensure_local_image(row: dict[str, str], image_url: str) -> bool:
    if not is_real_image_url(image_url):
        return False
    if existing_local_image_url(row):
        return True

    output_path = preferred_local_image_path(row)
    if output_path.exists():
        row["venue_image"] = output_path.relative_to(ROOT).as_posix()
        return True

    try:
        if download_image_to_webp(image_url, output_path):
            row["venue_image"] = output_path.relative_to(ROOT).as_posix()
            print(f"Saved local venue image for {row.get('venue_name', 'Venue')}: {row['venue_image']}")
            return True
    except Exception as error:
        print(f"Could not save local image for {row.get('venue_name', image_url)}: {error}")
    return False


def populate_empty_columns(rows: list[dict[str, str]], fieldnames: list[str]) -> int:
    changed = 0
    next_rank_by_slug: dict[str, int] = {}

    for field in REQUIRED_VENUE_FIELDS:
        if field not in fieldnames:
            fieldnames.append(field)
            for row in rows:
                row[field] = ""
                changed += 1

    for row in rows:
        original = dict(row)

        slug = normalise_slug(row.get("location_slug", ""))
        if slug:
            row["location_slug"] = slug

        if not row.get("location_name", "").strip() and slug:
            row["location_name"] = display_name_from_slug(slug)

        if not row.get("publish", "").strip():
            row["publish"] = "0"

        if slug not in next_rank_by_slug:
            existing_ranks = []
            for candidate in rows:
                if normalise_slug(candidate.get("location_slug", "")) == slug:
                    try:
                        existing_ranks.append(int(str(candidate.get("rank", "")).strip()))
                    except ValueError:
                        pass
            next_rank_by_slug[slug] = max(existing_ranks or [0]) + 1

        if not str(row.get("rank", "")).strip():
            row["rank"] = str(next_rank_by_slug[slug])
            next_rank_by_slug[slug] += 1

        if not row.get("venue_note", "").strip():
            venue_name = row.get("venue_name", "venue").strip() or "venue"
            location_name = row.get("location_name", "the area").strip() or "the area"
            row["venue_note"] = f"A local venue option for weddings, parties and private events in {location_name}: {venue_name}."

        if not row.get("venue_image", "").strip() and row.get("venue_name", "").strip():
            row["venue_image"] = preferred_local_image_path(row).relative_to(ROOT).as_posix()

        if not row.get("source_note", "").strip():
            row["source_note"] = "CSV candidate. Check venue suitability, availability and image rights before setting publish=1."

        if row != original:
            changed += 1

    return changed


def icon_svg(icon: str) -> str:
    icons = {
        "weddings": "<svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.6l-1-1a5.5 5.5 0 0 0-7.8 7.8l1 1L12 21l7.8-7.6 1-1a5.5 5.5 0 0 0 0-7.8z'></path></svg>",
        "parties": "<svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M8 22h8'></path><path d='M12 11v11'></path><path d='M19 3H5l2 8a5 5 0 0 0 10 0l2-8z'></path></svg>",
        "events": "<svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><rect x='3' y='7' width='18' height='13' rx='2'></rect><path d='M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2'></path></svg>",
        "power-hour": "<svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M13 2L3 14h8l-1 8 10-12h-8l1-8z'></path></svg>",
    }
    return icons[icon]


def icon_span(icon: str, class_name: str = "service-icon") -> str:
    return f'<span class="{class_name}" aria-hidden="true">{icon_svg(icon)}</span>'


def fetch_html(url: str, timeout: int = 12) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def attribute_value(tag: str, attribute: str) -> str:
    pattern = rf"\b{re.escape(attribute)}\s*=\s*([\"'])(.*?)\1"
    match = re.search(pattern, tag, flags=re.IGNORECASE | re.DOTALL)
    return unescape(match.group(2).strip()) if match else ""


def best_srcset_url(srcset: str) -> str:
    parts = [part.strip() for part in srcset.split(",") if part.strip()]
    if not parts:
        return ""
    weighted = []
    for part in parts:
        bits = part.split()
        url = bits[0]
        width = 0
        if len(bits) > 1 and bits[1].endswith("w"):
            try:
                width = int(bits[1][:-1])
            except ValueError:
                width = 0
        weighted.append((width, url))
    weighted.sort()
    return weighted[-1][1]


def looks_like_bad_image(url: str, context: str = "") -> bool:
    haystack = f"{url} {context}".lower()
    bad_terms = ["logo", "brand", "monogram", "favicon", "icon", "badge", "mark", "symbol", "crest", "seal", "transparent", "placeholder", "sprite", "avatar", "profile"]
    if any(term in haystack for term in bad_terms):
        return True
    return url.lower().split("?")[0].endswith((".svg", ".ico"))


def score_image(url: str, context: str = "") -> int:
    haystack = f"{url} {context}".lower()
    score = 10
    for term in ["venue", "wedding", "hotel", "manor", "house", "hall", "estate", "garden", "grounds", "barn", "ceremony", "reception", "gallery", "hero", "banner", "room", "interior", "exterior", "celebration"]:
        if term in haystack:
            score += 8
    for term in ["thumb", "thumbnail", "small", "150x", "200x", "300x"]:
        if term in haystack:
            score -= 10
    return score


def normalise_image_url(url: str, base_url: str) -> str:
    return urljoin(base_url, unescape(url.strip()))


def extract_image_candidates(html: str, base_url: str) -> list[dict[str, str | int]]:
    candidates: list[dict[str, str | int]] = []
    for tag in re.findall(r"<meta\b[^>]*>", html, flags=re.IGNORECASE | re.DOTALL):
        key = (attribute_value(tag, "property") or attribute_value(tag, "name")).lower()
        content = attribute_value(tag, "content")
        if content and key in {"og:image", "og:image:url", "og:image:secure_url", "twitter:image", "twitter:image:src"}:
            url = normalise_image_url(content, base_url)
            candidates.append({"url": url, "context": tag, "score": score_image(url, tag) + 25})

    jsonld_blocks = re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, flags=re.IGNORECASE | re.DOTALL)
    for block in jsonld_blocks:
        for match in re.finditer(r'"image"\s*:\s*"([^"]+)"', block):
            url = normalise_image_url(match.group(1), base_url)
            candidates.append({"url": url, "context": block[:700], "score": score_image(url, block) + 20})
        for match in re.finditer(r'"image"\s*:\s*\[\s*"([^"]+)"', block):
            url = normalise_image_url(match.group(1), base_url)
            candidates.append({"url": url, "context": block[:700], "score": score_image(url, block) + 20})

    for tag in re.findall(r"<img\b[^>]*>", html, flags=re.IGNORECASE | re.DOTALL):
        src = ""
        for attr in ["srcset", "data-srcset", "src", "data-src", "data-lazy-src", "data-original"]:
            value = attribute_value(tag, attr)
            if value:
                src = best_srcset_url(value) if "srcset" in attr else value
                break
        if src:
            url = normalise_image_url(src, base_url)
            candidates.append({"url": url, "context": tag, "score": score_image(url, tag)})

    for match in re.finditer(r"background(?:-image)?\s*:\s*url\((['\"]?)(.*?)\1\)", html, flags=re.IGNORECASE):
        raw_url = match.group(2).strip()
        if raw_url:
            url = normalise_image_url(raw_url, base_url)
            context = html[max(0, match.start() - 250): match.end() + 250]
            candidates.append({"url": url, "context": context, "score": score_image(url, context) + 5})

    return candidates


def choose_best_image(candidates: list[dict[str, str | int]]) -> str:
    filtered = []
    seen = set()
    for candidate in candidates:
        url = str(candidate["url"])
        context = str(candidate.get("context", ""))
        if url in seen:
            continue
        seen.add(url)
        if looks_like_bad_image(url, context):
            continue
        if not re.search(r"\.(jpg|jpeg|png|webp)(\?|$)", url, flags=re.IGNORECASE):
            continue
        filtered.append(candidate)
    if not filtered:
        return ""
    filtered.sort(key=lambda item: int(item.get("score", 0)), reverse=True)
    return str(filtered[0]["url"])


def load_image_cache() -> dict[str, str]:
    if not IMAGE_CACHE_JSON.exists():
        return {}
    try:
        return json.loads(IMAGE_CACHE_JSON.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def save_image_cache(cache: dict[str, str]) -> None:
    IMAGE_CACHE_JSON.parent.mkdir(parents=True, exist_ok=True)
    IMAGE_CACHE_JSON.write_text(json.dumps(cache, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def discover_image_for_venue(row: dict[str, str], cache: dict[str, str], refresh: bool) -> str:
    existing = row.get("venue_image_url", "").strip()
    if is_real_image_url(existing):
        ensure_local_image(row, existing)
        return existing
    if is_not_found_marker(existing) and not refresh:
        return NOT_FOUND

    venue_url = row.get("venue_url", "").strip()
    if not venue_url:
        return NOT_FOUND

    cached = cache.get(venue_url, "").strip()
    if cached and not refresh:
        if is_real_image_url(cached):
            ensure_local_image(row, cached)
        return cached

    try:
        html = fetch_html(venue_url)
        image_url = choose_best_image(extract_image_candidates(html, venue_url))
        if image_url:
            cache[venue_url] = image_url
            ensure_local_image(row, image_url)
            print(f"Found image for {row.get('venue_name', venue_url)}: {image_url}")
            return image_url
    except Exception as error:
        print(f"Could not fetch image for {venue_url}: {error}")

    cache[venue_url] = NOT_FOUND
    return NOT_FOUND


def fallback_image_js() -> str:
    return "'{{ '/assets/img/photo_gallery/Party_Set.jpg' | relative_url }}'"


def venue_card(row: dict[str, str]) -> str:
    venue_name = esc(row.get("venue_name", "Venue"))
    url = row.get("venue_url", "").strip()
    local_image_url = existing_local_image_url(row)
    remote_image_url = row.get("venue_image_url", "").strip()
    image_url = local_image_url or (remote_image_url if is_real_image_url(remote_image_url) else HERO_IMAGE)
    href_open = f'<a href="{esc(url)}" target="_blank" rel="noopener noreferrer">' if url else ""
    href_close = "</a>" if url else ""
    return "\n".join([
        '      <div class="venue-card">',
        f'        {href_open}<img src="{esc(image_url)}" alt="{venue_name}" loading="lazy" onerror="this.onerror=null;this.src={fallback_image_js()};">{href_close}',
        f'        <div class="venue-caption">{venue_name}</div>',
        '      </div>',
    ])


def service_card(href: str, image_path: str, alt: str, icon: str, title: str, tagline: str, chips: list[str]) -> str:
    chip_html = "\n".join(f"            <span>{esc(chip)}</span>" for chip in chips)
    return "\n".join([
        '    <div class="service-card">',
        f'      <a href="{href}" class="service-card-link">',
        '        <div class="image-container">',
        f'          <img src="{liquid_url(image_path)}" alt="{esc(alt)}" class="service-image">',
        '        </div>',
        '        <div class="service-card-text">',
        '          <div class="service-title-button">',
        icon_span(icon, "service-icon"),
        f'            <h3 class="service-title">{esc(title)}</h3>',
        '          </div>',
        f'          <p class="service-tagline">{esc(tagline)}</p>',
        '          <div class="service-chips">',
        chip_html,
        '          </div>',
        '        </div>',
        '      </a>',
        '    </div>',
    ])


def load_venue_rows() -> tuple[list[dict[str, str]], list[str]]:
    if not VENUE_CSV.exists():
        raise FileNotFoundError(f"Missing venue CSV: {VENUE_CSV}")
    with VENUE_CSV.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        fieldnames = list(reader.fieldnames or [])
    populate_empty_columns(rows, fieldnames)
    return rows, fieldnames


def save_venue_rows(rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    VENUE_CSV.parent.mkdir(parents=True, exist_ok=True)
    with VENUE_CSV.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def group_venues(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        slug = normalise_slug(row.get("location_slug", ""))
        if slug:
            row["location_slug"] = slug
            grouped.setdefault(slug, []).append(row)
    for slug in grouped:
        grouped[slug] = sorted(grouped[slug], key=lambda row: int(row.get("rank") or 999))
    return grouped


def load_location_copy() -> dict[str, dict[str, str]]:
    if not LOCATION_COPY_JSON.exists():
        return {}
    raw = json.loads(LOCATION_COPY_JSON.read_text(encoding="utf-8"))
    return {normalise_slug(slug): value for slug, value in raw.items()}


def default_location_copy(slug: str, rows: list[dict[str, str]]) -> dict[str, str]:
    location_name = ""
    for row in rows:
        location_name = str(row.get("location_name", "") or "").strip()
        if location_name:
            break
    if not location_name:
        location_name = display_name_from_slug(slug)
    return {
        "name": location_name,
        "county": location_name,
        "intro": f"Live saxophone and DJ sets for weddings, parties and private events in {location_name} and the surrounding area.",
        "angle": f"From relaxed venue arrivals to full evening dancefloors, {location_name} celebrations work well with flexible live sax and DJ options.",
    }


def location_page_copy(slug: str, rows: list[dict[str, str]], location_copy: dict[str, dict[str, str]]) -> dict[str, str]:
    fallback = default_location_copy(slug, rows)
    custom = location_copy.get(slug, {})
    return {
        "name": custom.get("name") or fallback["name"],
        "county": custom.get("county") or fallback["county"],
        "intro": custom.get("intro") or fallback["intro"],
        "angle": custom.get("angle") or fallback["angle"],
    }


def location_chips(slug: str, name: str, county: str) -> list[str]:
    return NEARBY_CHIPS.get(slug, [name, county, "Weddings", "Parties", "DJ & sax", "South West"])[:6]


def location_is_ready(rows: list[dict[str, str]]) -> bool:
    return len(rows) >= 1 and all(str(row.get("publish", "0")).strip() == "1" for row in rows)


def should_generate_location(rows: list[dict[str, str]], include_unpublished: bool) -> bool:
    return include_unpublished or location_is_ready(rows)


def inline_location_css() -> str:
    return """<style>
  .location-venue-wrapper { overflow: visible; }
  .location-venue-grid-static {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 1.5rem;
    overflow: visible;
  }
  .location-venue-grid-static .venue-card { min-width: 0; }
  .location-venue-grid-static .venue-card img {
    width: 100%;
    height: 260px;
    object-fit: cover;
    display: block;
  }
  @media (max-width: 640px) {
    .location-venue-grid-static { grid-template-columns: 1fr; }
    .location-venue-grid-static .venue-card img { height: 240px; }
  }
</style>"""


def reveal_script() -> str:
    return """<script>
  document.addEventListener('DOMContentLoaded', () => {
    const revealItems = document.querySelectorAll('.reveal-on-scroll');
    if (!revealItems.length) return;
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.14 });
    revealItems.forEach(item => observer.observe(item));
  });
</script>"""


def render_page(slug: str, rows: list[dict[str, str]], info: dict[str, str]) -> str:
    raw_name = info["name"]
    raw_county = info["county"]
    name = esc(raw_name)
    county = esc(raw_county)
    intro = esc(info["intro"])
    angle = esc(info["angle"])
    chips = location_chips(slug, raw_name, raw_county)
    chip_spans = "\n".join(f"    <span>{esc(chip)}</span>" for chip in chips)
    nearby_items = "".join(f"<li>{esc(chip)}</li>" for chip in chips)
    service_cards = "\n".join([
        service_card("/packages/wedding-packages/", SERVICE_WEDDINGS_IMAGE, f"Weddings in {raw_name}", "weddings", "Weddings", f"Ceremony, reception and evening music in {raw_name}.", ["Ceremony", "Drinks", "Evening"]),
        service_card("/packages/party-packages/", SERVICE_PARTIES_IMAGE, f"Parties in {raw_name}", "parties", "Parties", f"Big tunes, live sax and proper energy for {raw_name} celebrations.", ["Birthdays", "Private parties", "DJ & sax"]),
        service_card("/packages/events-packages/", SERVICE_EVENTS_IMAGE, f"Private events in {raw_name}", "events", "Private Events", f"Polished music for venues, functions and private events around {raw_name}.", ["Venues", "Functions", "Corporate"]),
        service_card("/packages/power-hour/", SERVICE_POWER_HOUR_IMAGE, f"Power Hour in {raw_name}", "power-hour", "Power Hour", "Ibiza classics, live sax and full-on dancefloor energy.", ["Ibiza classics", "Live sax", "Peak energy"]),
    ])
    venue_cards = "\n".join(venue_card(row) for row in rows)
    parts = [
        "---",
        "layout: default",
        f'title: "Wedding Saxophonist & DJ in {name} | Solo Studios"',
        f"permalink: /locations/{slug}/",
        f'description: "Live saxophone and DJ sets for weddings, parties and events in {name}, {county}."',
        "---",
        "",
        "<link rel=\"stylesheet\" href=\"{{ '/assets/css/home.css' | relative_url }}\">",
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">",
        "",
        inline_location_css(),
        "",
        '<section class="hero-section location-hero-section">',
        '  <video autoplay muted loop playsinline class="hero-video">',
        f'    <source src="{liquid_url(HOMEPAGE_VIDEO)}" type="video/mp4">',
        '    Your browser does not support the video tag.',
        '  </video>',
        '  <div class="hero-overlay"></div>',
        '  <div class="hero-content">',
        '    <div class="hero-title-image">',
        "      <img src=\"{{ '/assets/img/website-title-ivory.png' | relative_url }}\" alt=\"Solo Studios\" class=\"hero-title-img\">",
        '    </div>',
        '    <div class="hero-copy">',
        f'      <p class="hero-tagline">Wedding saxophonist &amp; DJ in {name}</p>',
        f'      <p class="hero-subtext">{intro}</p>',
        '      <div class="hero-actions" aria-label="Location page actions">',
        '        <a href="/#contact-us" class="hero-button hero-button--primary">Check availability</a>',
        '        <a href="/gallery/videos/" class="hero-button hero-button--secondary">Watch videos</a>',
        '      </div>',
        '    </div>',
        '  </div>',
        '</section>',
        "",
        '<section class="trust-strip" aria-label="Areas and event options">',
        '  <div class="trust-strip__inner">',
        chip_spans,
        '  </div>',
        '</section>',
        "",
        '<div class="services-cards-wrapper reveal-on-scroll">',
        f'  <h2 class="services-section-title">Live music for {name} weddings and events</h2>',
        '  <p class="services-section-intro">',
        f'    {angle} Choose a relaxed daytime sax set, a DJ and sax evening party, or a full package that carries the music through the whole day.',
        '  </p>',
        '  <div class="services-cards-section">',
        service_cards,
        '  </div>',
        '  <div class="services-help-cta">',
        '    <div class="services-help-cta__text">',
        f'      <h3>Planning an event in {name}?</h3>',
        '      <p>Tell us the venue, date and timings and we will point you towards the right live sax and DJ setup.</p>',
        '    </div>',
        '    <div class="services-help-cta__actions">',
        '      <a href="/#contact-us" class="mini-cta mini-cta--primary">Get a recommendation</a>',
        '      <a href="/gallery/videos/" class="mini-cta mini-cta--secondary">View videos</a>',
        '    </div>',
        '  </div>',
        '</div>',
        "",
        '<section class="venues-gallery reveal-on-scroll">',
        f'  <h2 class="section-title">Wedding venues around {name}</h2>',
        '  <p class="section-intro">',
        f'    A few useful venue ideas if you are planning a wedding, party or private event in {name} and the surrounding area.',
        '  </p>',
        '  <div class="auto-scroll-wrapper location-venue-wrapper">',
        '    <div class="gallery-scroll-container location-venue-grid-static">',
        venue_cards,
        '    </div>',
        '  </div>',
        '</section>',
        "",
        '<section class="location-seo-section reveal-on-scroll" aria-labelledby="location-seo-heading">',
        '  <div class="location-seo-section__inner">',
        '    <p class="location-seo-section__eyebrow">Local live music</p>',
        f'    <h2 id="location-seo-heading">Live Saxophone and DJ Sets in {name}</h2>',
        '    <div class="location-seo-section__grid">',
        '      <div class="location-seo-section__copy">',
        '        <p>',
        f'          Solo Studios provides live saxophone and DJ sets for weddings, parties and private events in <strong>{name}</strong> and across <strong>{county}</strong>. Sets can be shaped around relaxed arrivals, drinks receptions, wedding breakfasts, evening parties and full dancefloor moments.',
        '        </p>',
        '        <p>',
        f'          If you are planning a celebration near {name}, send over your venue, date and rough timings. We will help you choose the right live sax, DJ or combined sax and DJ option for the atmosphere you want.',
        '        </p>',
        '      </div>',
        f'      <div class="location-seo-section__areas" aria-label="Areas covered near {name}">',
        '        <h3>Popular nearby areas</h3>',
        f'        <ul>{nearby_items}</ul>',
        '      </div>',
        '    </div>',
        '  </div>',
        '</section>',
        "",
        '<section class="ibiza-promo-simple reveal-on-scroll">',
        '  <div class="container">',
        "    <img src=\"{{ '/assets/img/palm_tree.svg' | relative_url }}\" alt=\"\" class=\"palm-top-left\">",
        "    <img src=\"{{ '/assets/img/palm_tree.svg' | relative_url }}\" alt=\"\" class=\"palm-bottom-right\">",
        '    <h2>Want the big party moment?</h2>',
        f'    <p>The <strong>Power Hour</strong> package brings house favourites, live sax and full-energy party tracks for weddings and events in {name}.</p>',
        '    <a href="/packages/power-hour/" class="btn-ibiza-simple">See the Power Hour package</a>',
        '  </div>',
        '</section>',
        "",
        reveal_script(),
        "",
    ]
    return "\n".join(parts)


def populate_missing_images(rows: list[dict[str, str]], refresh: bool, single: str | None) -> int:
    cache = load_image_cache()
    updated = 0
    target_slug = normalise_slug(single) if single else None
    for row in rows:
        row_slug = normalise_slug(row.get("location_slug", ""))
        if target_slug and row_slug != target_slug:
            continue
        before_url = row.get("venue_image_url", "").strip()
        before_local = row.get("venue_image", "").strip()
        if is_real_image_url(before_url):
            ensure_local_image(row, before_url)
        elif is_not_found_marker(before_url) and not refresh:
            pass
        else:
            found = discover_image_for_venue(row, cache, refresh)
            if found and found != before_url:
                row["venue_image_url"] = found
            if is_real_image_url(found):
                ensure_local_image(row, found)
        if row.get("venue_image_url", "").strip() != before_url or row.get("venue_image", "").strip() != before_local:
            updated += 1
    save_image_cache(cache)
    return updated


def generate(include_unpublished: bool, single: str | None, refresh_image_cache: bool) -> None:
    location_copy = load_location_copy()
    venue_rows, fieldnames = load_venue_rows()
    target_slug = normalise_slug(single) if single else None

    populated = populate_empty_columns(venue_rows, fieldnames)
    updated_images = populate_missing_images(venue_rows, refresh_image_cache, target_slug)
    if populated or updated_images:
        save_venue_rows(venue_rows, fieldnames)
        print(f"Updated {populated + updated_images} CSV value group(s) in {VENUE_CSV}")

    grouped_venues = group_venues(venue_rows)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    made = 0
    skipped = 0

    for slug, rows in sorted(grouped_venues.items()):
        if target_slug and slug != target_slug:
            continue
        selected_rows = [row for row in rows if normalise_slug(row.get("location_slug", "")) == slug]
        selected_rows = sorted(selected_rows, key=lambda row: int(row.get("rank") or 999))
        if not should_generate_location(selected_rows, include_unpublished):
            skipped += 1
            continue
        info = location_page_copy(slug, selected_rows, location_copy)
        if slug not in location_copy:
            print(f"Using generated copy for new location slug: {slug}")
        venue_names = ", ".join(row.get("venue_name", "Venue") for row in selected_rows)
        print(f"Generating {slug} with {len(selected_rows)} venue(s): {venue_names}")
        output_file = OUTPUT_DIR / f"{slug}.html"
        output_file.write_text(render_page(slug, selected_rows, info), encoding="utf-8")
        made += 1

    print(f"Generated {made} page(s); skipped {skipped} unpublished location(s).")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Image cache: {IMAGE_CACHE_JSON}")
    print(f"Local image directory: {LOCAL_VENUE_IMAGE_DIR}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Solo Studios location pages")
    parser.add_argument("--include-unpublished", action="store_true", help="Generate pages even where publish is still 0")
    parser.add_argument("--single", help="Generate just one location slug, e.g. plymouth")
    parser.add_argument("--refresh-image-cache", action="store_true", help="Retry rows marked 'not found' and blank rows, but never overwrite real URLs")
    args = parser.parse_args()
    generate(args.include_unpublished, args.single, args.refresh_image_cache)


if __name__ == "__main__":
    main()
