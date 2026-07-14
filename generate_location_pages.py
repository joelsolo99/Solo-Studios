#!/usr/bin/env python3

import csv
import html
from collections import defaultdict
from pathlib import Path


CSV_FILE = Path("assets/data/location_venues.csv")
OUTPUT_DIR = Path("_pages/locations")


OUTPUT_FILE = Path("_pages/locations/locations_index.html")

PAGE_TEMPLATE = r"""---
layout: default
title: Live Saxophone & DJ for Parties and Weddings in __LOCATION_NAME__ 
permalink: /locations/__LOCATION_SLUG__/
---


<link rel="stylesheet" href="{{ '/assets/css/home.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/reviews.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/form.css' | relative_url }}">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<div class="home-page-title-wrap">
  <h1 class="page-title home-page-title">Solo Studios</h1>
</div>



<section class="hero-section hero-section--split">

  <video autoplay muted loop playsinline class="hero-video">
    <source src="{{ '/assets/video/intro_loop.mp4' | relative_url }}" type="video/mp4">
    Your browser does not support the video tag.
  </video>


  <div class="hero-overlay"></div>

<div class="hero-title-image">
  <img src="{{ '/assets/img/website-title-ivory.png' | relative_url }}" alt="Solo Studios" class="hero-title-img">
</div>

  <div class="hero-inner">

    <div class="hero-copy">



      <p class="hero-tagline">
        Live Saxophone & DJ Entertainment
      </p>

      <h2 class="hero-main-heading">
        Weddings, Parties & Events in __LOCATION_NAME__
      </h2>

      
      <p class="hero-subtext">
        Packed dancefloors, Ibiza-inspired sax sets and music tailored around your event from the first guest arrival
        through to the final song.
      </p>

      <div class="hero-badges">
        <span>Weddings</span>
        <span>Private Parties</span>
        <span>Corporate Events</span>
      </div>

    </div>
<div class="hero-form-card">

  <h3>Check Availability</h3>

  <p>
    Tell us about your event and we'll get back to you quickly.
  </p>

  <form id="hero-contact-form" novalidate>

    <input type="text" name="from_name" placeholder="Your Name" required>

    <input type="email" name="from_email" placeholder="Email Address" required>

    <select name="event_type" required>
      <option value="" disabled selected>Type of Event</option>
      <option value="Wedding">Wedding</option>
      <option value="Birthday">Birthday</option>
      <option value="Corporate Event">Corporate Event</option>
      <option value="Charity Event">Charity Event</option>
      <option value="Private Party">Private Party</option>
      <option value="Other">Other</option>
    </select>

    <input type="text" name="event_date" placeholder="Date of Event">

    <input type="text" name="location" placeholder="Event Location or Venue">

    <textarea name="message" placeholder="Tell us about your event" required></textarea>

    <input type="hidden" name="subject" value="Homepage availability enquiry">

    <input type="text" name="website" style="display:none" tabindex="-1" autocomplete="off">

    <button type="submit">
      Check Availability
    </button>

  </form>

</div>


  <div class="hero-trust-carousel" aria-label="Solo Studios booking reassurance">
    <div class="hero-trust-track">
  
      <span class="hero-trust-item">
      <img src="{{ '/assets/img/icons/shield.svg' | relative_url }}" alt="Star">
        <span>PLI to £10 Million</span>
      </span>
  
      <span class="hero-trust-item">
      <img src="{{ '/assets/img/icons/star.svg' | relative_url }}" alt="Star">
      <span> 5 Star Reviews</span>
      </span>
  
      <span class="hero-trust-item">
      <img src="{{ '/assets/img/icons/map-pin.svg' | relative_url }}" alt="Star">
        <span>Travel Throughout The South West</span>
      </span>
  
      <span class="hero-trust-item">
      <img src="{{ '/assets/img/icons/price-tag.svg' | relative_url }}" alt="Star">
        <span>Clear Prices</span>
      </span>
  
      <span class="hero-trust-item">
      <img src="{{ '/assets/img/icons/speaker.svg' | relative_url }}" alt="Star">
        <span>Professional Sound Equipment</span>
      </span>
  
      <span class="hero-trust-item">
      <img src="{{ '/assets/img/icons/calendar-check.svg' | relative_url }}" alt="Star">
        <span>Easy Booking</span>
      </span>
  
      <span class="hero-trust-item">
      <img src="{{ '/assets/img/icons/saxophone.svg' | relative_url }}" alt="Star">
        <span>Live Sax Performances</span>
      </span>
  
      <span class="hero-trust-item">
      <img src="{{ '/assets/img/icons/sparkles.svg' | relative_url }}" alt="Star">
        <span>DJ Sets Available</span>
      </span>
  
      <span class="hero-trust-item">
      <img src="{{ '/assets/img/icons/headphones.svg' | relative_url }}" alt="Star">
        <span>Wedding and Party Specialists</span>
      </span>
  
      <span class="hero-trust-item">
        <img src="{{ '/assets/img/icons/shield.svg' | relative_url }}" alt="Star">
        <span>PLI to £10 Million</span>
      </span>
      
      <span class="hero-trust-item">
        <img src="{{ '/assets/img/icons/star.svg' | relative_url }}" alt="Star">
        <span> 5 Star Reviews</span>
      </span>
      
      <span class="hero-trust-item">
        <img src="{{ '/assets/img/icons/map-pin.svg' | relative_url }}" alt="Star">
        <span>Travel Throughout The South West</span>
      </span>
      
      <span class="hero-trust-item">
        <img src="{{ '/assets/img/icons/price-tag.svg' | relative_url }}" alt="Star">
        <span>Clear Prices</span>
      </span>
      
      <span class="hero-trust-item">
        <img src="{{ '/assets/img/icons/speaker.svg' | relative_url }}" alt="Star">
        <span>Professional Sound Equipment</span>
      </span>
      
      <span class="hero-trust-item">
        <img src="{{ '/assets/img/icons/calendar-check.svg' | relative_url }}" alt="Star">
        <span>Easy Booking</span>
      </span>
      
      <span class="hero-trust-item">
        <img src="{{ '/assets/img/icons/saxophone.svg' | relative_url }}" alt="Star">
        <span>Live Sax Performances</span>
      </span>
      
      <span class="hero-trust-item">
 <span class="hero-trust-item">
      <img src="{{ '/assets/img/icons/shield.svg' | relative_url }}" alt="Star">
        <span>PLI to £10 Million</span>
      </span>
  
      <span class="hero-trust-item">
      <img src="{{ '/assets/img/icons/star.svg' | relative_url }}" alt="Star">
      <span> 5 Star Reviews</span>
      </span>
  
      <span class="hero-trust-item">
      <img src="{{ '/assets/img/icons/map-pin.svg' | relative_url }}" alt="Star">
        <span>Travel Throughout The South West</span>
      </span>
  
      <span class="hero-trust-item">
      <img src="{{ '/assets/img/icons/price-tag.svg' | relative_url }}" alt="Star">
        <span>Clear Prices</span>
      </span>
  
      <span class="hero-trust-item">
      <img src="{{ '/assets/img/icons/speaker.svg' | relative_url }}" alt="Star">
        <span>Professional Sound Equipment</span>
      </span>
  
      <span class="hero-trust-item">
      <img src="{{ '/assets/img/icons/calendar-check.svg' | relative_url }}" alt="Star">
        <span>Easy Booking</span>
      </span>
  
      <span class="hero-trust-item">
      <img src="{{ '/assets/img/icons/saxophone.svg' | relative_url }}" alt="Star">
        <span>Live Sax Performances</span>
      </span>
  
      
      <span class="hero-trust-item">
        <img src="{{ '/assets/img/icons/headphones.svg' | relative_url }}" alt="Star">
        <span>Wedding and Party Specialists</span>
      </span>
  
    </div>
  </div>

</section>

<section class="services-showcase-wrapper reveal-on-scroll">
  <div class="services-showcase-header">
    <p class="services-showcase-eyebrow">Live music, your way</p>

    <h2 class="services-section-title">Choose the soundtrack for your event</h2>

    <p class="services-section-intro">
      From relaxed daytime sax sets to full evening parties, shape the music around the atmosphere you want to create.
    </p>
  </div>

  <div class="services-showcase">
    <div class="services-showcase__media" aria-hidden="true">
      <video autoplay muted loop playsinline class="services-showcase__video">
        <source
          src="{{ '/assets/video/services-loop.mp4' | relative_url }}"
          type="video/mp4"
        >
      </video>

      <div class="services-showcase__media-overlay"></div>

      <div class="services-showcase__media-caption">
        <span>Live saxophone and DJ entertainment</span>
      </div>
    </div>

    <div class="services-showcase__list">

      <a href="{{ '/packages/wedding-packages/' | relative_url }}" class="services-showcase__item">
        <span class="services-showcase__content">
          <span class="services-showcase__title">Weddings</span>
          <span class="services-showcase__text">From the ceremony to the last dance.</span>

          <span class="services-showcase__chips" aria-label="Wedding package options">
            <span>Ceremony</span>
            <span>Drinks</span>
            <span>Evening</span>
          </span>
        </span>

        <span class="services-showcase__arrow" aria-hidden="true">→</span>
      </a>

      <a href="{{ '/packages/party-packages/' | relative_url }}" class="services-showcase__item">
        <span class="services-showcase__content">
          <span class="services-showcase__title">Parties</span>
          <span class="services-showcase__text">Big tunes, live sax, proper energy.</span>

          <span class="services-showcase__chips" aria-label="Party package options">
            <span>Birthdays</span>
            <span>Hen dos</span>
            <span>Private parties</span>
          </span>
        </span>

        <span class="services-showcase__arrow" aria-hidden="true">→</span>
      </a>

      <a href="{{ '/packages/events-packages/' | relative_url }}" class="services-showcase__item">
        <span class="services-showcase__content">
          <span class="services-showcase__title">Private Events</span>
          <span class="services-showcase__text">Polished music for every kind of crowd.</span>

          <span class="services-showcase__chips" aria-label="Private event options">
            <span>Corporate</span>
            <span>Venues</span>
            <span>Brand events</span>
          </span>
        </span>

        <span class="services-showcase__arrow" aria-hidden="true">→</span>
      </a>

      <a href="{{ '/packages/power-hour/' | relative_url }}" class="services-showcase__item">
        <span class="services-showcase__content">
          <span class="services-showcase__title">Power Hour</span>
          <span class="services-showcase__text">Ibiza classics, live sax, full-on energy.</span>

          <span class="services-showcase__chips" aria-label="Power Hour options">
            <span>Ibiza classics</span>
            <span>Live sax</span>
            <span>Peak energy</span>
          </span>
        </span>

        <span class="services-showcase__arrow" aria-hidden="true">→</span>
      </a>

    </div>
  </div>

  <div class="services-help-cta">
    <div class="services-help-cta__text">
      <h3>Not sure what fits your event?</h3>
      <p>Tell us what you are planning and we will point you towards the right package.</p>
    </div>

    <div class="services-help-cta__actions">
      <a href="/contact" class="btn btn-primary">Get a recommendation</a>
      <a href="{{ '/gallery/videos/' | relative_url }}" class="btn btn-secondary">View videos</a>
    </div>
  </div>
</section>


<section class="video-showcase-section reveal-on-scroll">
  <div class="video-showcase-header">
    <p class="video-showcase-eyebrow">Real event moments</p>

    <h2 class="section-title">See the energy before you book</h2>

    <p class="section-intro">
      Watch a few live sax and DJ moments from weddings, parties and dancefloors across the South West.
    </p>
  </div>

  <div class="video-showcase">

    <a href="{{ '/gallery/videos/#video-jubel' | relative_url }}" class="video-showcase-feature">
      <img src="https://i.ytimg.com/vi/uuDLdVoHLs4/hqdefault.jpg" alt="Jubel live sax dancefloor performance thumbnail"
        class="video-showcase-img youtube-thumb crop-high">

      <div class="video-showcase-gradient"></div>

      <div class="video-showcase-badge">
        <span>Featured performance</span>
      </div>

      <div class="video-showcase-play" aria-hidden="true">
        <span>▶</span>
      </div>

      <div class="video-showcase-caption">
        <p class="video-showcase-kicker">Live sax dancefloor set</p>
        <h3>Jubel live performance</h3>
        <p>Ibiza-style sax energy built for a packed dancefloor.</p>
      </div>
    </a>

    <div class="video-showcase-list">

      <a href="{{ '/gallery/videos/#video-pitbull' | relative_url }}" class="video-showcase-row">
        <span class="video-showcase-row__thumb">
          <img src="https://i.ytimg.com/vi/uC-EWWkLyy0/hqdefault.jpg" alt="Fireball wedding entrance thumbnail"
            class="youtube-thumb crop-high">
          <span class="video-showcase-row__play" aria-hidden="true">▶</span>
        </span>

        <span class="video-showcase-row__content">
          <span class="video-showcase-row__label">Wedding entrance</span>
          <strong>Fireball live entrance</strong>
          <span>Big arrival energy for the start of the party.</span>
        </span>

        <span class="video-showcase-row__arrow" aria-hidden="true">→</span>
      </a>

      <a href="{{ '/gallery/videos/#video-club' | relative_url }}" class="video-showcase-row">
        <span class="video-showcase-row__thumb">
          <img src="https://i.ytimg.com/vi/xnP7DbxwX60/hqdefault.jpg" alt="Club Classics party highlights thumbnail"
            class="youtube-thumb crop-mid">
          <span class="video-showcase-row__play" aria-hidden="true">▶</span>
        </span>

        <span class="video-showcase-row__content">
          <span class="video-showcase-row__label">Party highlights</span>
          <strong>Club Classics</strong>
          <span>Dancefloor favourites with live sax over the top.</span>
        </span>

        <span class="video-showcase-row__arrow" aria-hidden="true">→</span>
      </a>

      <a href="{{ '/gallery/videos/#video-valerie' | relative_url }}" class="video-showcase-row">
        <span class="video-showcase-row__thumb">
          <img src="https://i.ytimg.com/vi/2Tvs8UwSdmw/hqdefault.jpg" alt="Valerie live drinks reception thumbnail"
            class="youtube-thumb crop-mid">
          <span class="video-showcase-row__play" aria-hidden="true">▶</span>
        </span>

        <span class="video-showcase-row__content">
          <span class="video-showcase-row__label">Drinks reception</span>
          <strong>Valerie live performance</strong>
          <span>A relaxed live moment for daytime celebrations.</span>
        </span>

        <span class="video-showcase-row__arrow" aria-hidden="true">→</span>
      </a>

    </div>
  </div>

  <div class="video-showcase-cta">

    <a href="{{ '/gallery/videos/' | relative_url }}" class="cta-button">
      <span class="cta-button__icon" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
          stroke-linejoin="round">
          <rect x="3" y="6" width="13" height="12" rx="2" ry="2"></rect>
          <polygon points="16 10 21 7 21 17 16 14 16 10"></polygon>
        </svg>
      </span>
      <span>Watch more performances</span>
    </a>

    <a href="{{ '/gallery/photos/' | relative_url }}" class="cta-button">
      <span class="cta-button__icon" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
          stroke-linejoin="round">
          <path d="M4 7h3l1.5-2h7L17 7h3a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V9a2 2 0 0 1 2-2z"></path>
          <circle cx="12" cy="13" r="4"></circle>
        </svg>
      </span>
      <span>View event photos</span>
    </a>

  </div>
</section>

{% include reviews.html %}

<section class="venues-gallery reveal-on-scroll"> 
<h2 class="section-title">We'll travel to  __LOCATION_NAME__'s Finest</h2> 
<p class="section-intro"> Some of the venues in __LOCATION_NAME__ that are suited to weddings, parties and private events. </p> 

    <div class="auto-scroll-wrapper"> 
        <div class="gallery-scroll-container"> 
        __VENUE_CARDS__ 
        </div> 
    </div> 
</section> 




<section class="location-seo-section reveal-on-scroll" aria-labelledby="location-seo-heading">
  <div class="location-seo-section__inner">
    <p class="location-seo-section__eyebrow">Local live music</p>
    <h2 id="location-seo-heading">Live Saxophone and DJ Sets in Plymouth, Cornwall and the South West</h2>

    <div class="location-seo-section__grid">
      <div class="location-seo-section__copy">
        <p>
          Solo Studios provides live saxophone and DJ sets for weddings, private parties and events in
          <strong>__LOCATION_NAME__</strong>, across <strong>Devon and Cornwall</strong>, and throughout the wider
          <strong>South West</strong>. Whether you are planning a wedding reception, a birthday party,
          a corporate event, a drinks reception or a full evening celebration, the music can be shaped
          around the atmosphere you want to create.
        </p>

        <p>
          Sets can be tailored for relaxed daytime moments, high-energy dancefloors, Ibiza-style party
          sets and polished private events. If you are planning an event in Plymouth, Cornwall, Devon
          or elsewhere in the South West, send over a few details and we will help you choose the right
          live sax and DJ option for the day.
        </p>
      </div>

      <div class="location-seo-section__areas" aria-label="Areas covered">
        <h3>Popular areas</h3>
        <ul>
          <li>Plymouth</li>
          <li>Cornwall</li>
          <li>Devon</li>
          <li>Exeter</li>
          <li>Newquay</li>
          <li>Truro</li>
          <li>South Hams</li>
          <li>The wider South West</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<script>
  document.addEventListener('DOMContentLoaded', () => {
    const container = document.querySelector('.gallery-scroll-container');

    if (!container) return;

    const children = Array.from(container.children);
    children.forEach(child => {
      const clone = child.cloneNode(true);
      container.appendChild(clone);
    });

    let scrollSpeed = 0.5;
    let isHovered = false;

    container.parentElement.addEventListener('mouseenter', () => {
      isHovered = true;
    });

    container.parentElement.addEventListener('mouseleave', () => {
      isHovered = false;
    });

    function step() {
      if (!isHovered) {
        container.scrollLeft += scrollSpeed;

        if (container.scrollLeft >= container.scrollWidth / 2) {
          container.scrollLeft = 0;
        }
      }

      requestAnimationFrame(step);
    }

    step();
  });
</script>

<section class="ibiza-promo-simple reveal-on-scroll">
  <div class="container">
    <img src="{{ '/assets/img/palm_tree.svg' | relative_url }}" alt="" class="palm-top-left">
    <img src="{{ '/assets/img/palm_tree.svg' | relative_url }}" alt="" class="palm-bottom-right">

    <h2>After something bigger?</h2>
    <p>
      If you want the Ibiza feel, our <strong>Power Hour</strong> package brings house favourites,
      live sax, and a full-energy set built to get the party going.
    </p>
    <a href="/packages/power-hour/" class="btn-ibiza-simple">See the Power Hour package</a>
  </div>
</section>



<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", () => {
    emailjs.init("brJTI5NcxOOq3ZeV3");

    const serviceId = "service_pdrbr2j";
    const templateId = "template_iw7f4ro";

    const heroForm = document.getElementById("hero-contact-form");
    const contactForm = document.getElementById("contact-form");

    function setSubmitState(form, isSending) {
      const submitButton = form.querySelector('button[type="submit"]');

      if (!submitButton) return;

      if (isSending) {
        submitButton.dataset.originalText = submitButton.textContent.trim();
        submitButton.disabled = true;
        submitButton.textContent = "Sending...";
      } else {
        submitButton.disabled = false;
        submitButton.textContent = submitButton.dataset.originalText || "Send Enquiry";
      }
    }

    function getFieldValue(form, fieldName) {
      const field = form.querySelector(`[name="${fieldName}"]`);
      return field ? field.value.trim() : "";
    }

    function ensureSubjectField(form) {
      let subjectField = form.querySelector('input[name="subject"]');

      if (!subjectField) {
        subjectField = document.createElement("input");
        subjectField.type = "hidden";
        subjectField.name = "subject";
        form.appendChild(subjectField);
      }

      return subjectField;
    }

    function handleEmailForm(form, options = {}) {
      if (!form) return;

      form.addEventListener("submit", function (event) {
        event.preventDefault();

        const honeypot = form.querySelector('input[name="website"]');

        if (honeypot && honeypot.value) {
          console.log("Honeypot triggered - not sending");
          return;
        }

        const eventType = getFieldValue(form, "event_type");
        const eventDate = getFieldValue(form, "event_date");
        const location = getFieldValue(form, "location");

        if (!eventType) {
          alert("Please select the type of event.");
          return;
        }

        const subjectField = ensureSubjectField(form);

        subjectField.value = [
          eventType,
          eventDate,
          location
        ].filter(Boolean).join(" - ");

        setSubmitState(form, true);

        emailjs
          .sendForm(serviceId, templateId, form)
          .then(() => {
            if (options.successType === "hero") {
              form.innerHTML = `
                <div class="hero-form-success">
                  <h3>Thank you</h3>
                  <p>Your enquiry has been sent. We will be in touch soon.</p>
                </div>
              `;
              return;
            }

            form.style.display = "none";

            const thankYouMessage = document.querySelector("#contact-us .thank-you-message");

            if (thankYouMessage) {
              thankYouMessage.style.display = "block";
            }
          })
          .catch((error) => {
            console.error("EmailJS error:", error);
            alert("Error sending message. Please try again later.");
            setSubmitState(form, false);
          });
      });
    }

    handleEmailForm(heroForm, {
      successType: "hero"
    });

    const wrapper = document.querySelector(".custom-select-wrapper");
    const selected = document.getElementById("custom-select-selected");
    const list = document.getElementById("custom-select-list");
    const nativeSelect = document.getElementById("event_type");

    if (wrapper && selected && list && nativeSelect) {
      const options = list.querySelectorAll("li");

      wrapper.addEventListener("click", () => {
        const expanded = wrapper.getAttribute("aria-expanded") === "true";
        wrapper.setAttribute("aria-expanded", String(!expanded));
        list.style.display = expanded ? "none" : "block";
      });

      options.forEach((option) => {
        option.addEventListener("click", (event) => {
          event.stopPropagation();

          selected.textContent = option.textContent;
          nativeSelect.value = option.dataset.value;

          options.forEach((opt) => opt.setAttribute("aria-selected", "false"));
          option.setAttribute("aria-selected", "true");

          wrapper.setAttribute("aria-expanded", "false");
          list.style.display = "none";
        });
      });

      document.addEventListener("click", (event) => {
        if (!wrapper.contains(event.target)) {
          wrapper.setAttribute("aria-expanded", "false");
          list.style.display = "none";
        }
      });
    }

    handleEmailForm(contactForm, {
      successType: "contact"
    });
  });
</script>


<script src="{{ '/assets/js/reviews-carousel.js' | relative_url }}"></script>


<script>
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
    }, {
      threshold: 0.14
    });

    revealItems.forEach(item => observer.observe(item));
  });
</script>"""

def is_published(value: str) -> bool:
    """Return True when a CSV row is marked for publication."""
    return value.strip().lower() in {"1", "true", "yes", "y"}


def parse_rank(value: str) -> int:
    """Convert a CSV rank to an integer, placing invalid ranks last."""
    try:
        return int(value.strip())
    except (AttributeError, ValueError):
        return 999999


def load_venues_by_location(
    csv_file: Path,
) -> dict[str, list[dict[str, str]]]:
    """
    Load published venues and group them by location slug.

    Venues within each location are ordered by rank and then venue name.
    """
    if not csv_file.is_file():
        raise FileNotFoundError(f"Location venue CSV file not found: {csv_file}")

    venues_by_location: dict[str, list[dict[str, str]]] = defaultdict(list)

    with csv_file.open(
        mode="r",
        newline="",
        encoding="utf-8-sig",
    ) as file:
        reader = csv.DictReader(file)

        required_columns = {
            "location_slug",
            "location_name",
            "publish",
            "rank",
            "venue_name",
            "venue_url",
            "venue_image",
        }

        available_columns = set(reader.fieldnames or [])
        missing_columns = required_columns - available_columns

        if missing_columns:
            missing = ", ".join(sorted(missing_columns))
            raise ValueError(f"The CSV file is missing required columns: {missing}")

        for row in reader:
            if not is_published(row.get("publish", "")):
                continue

            slug = row.get("location_slug", "").strip()
            location_name = row.get("location_name", "").strip()
            venue_name = row.get("venue_name", "").strip()

            if not slug:
                print("Skipped a published venue with no location_slug.")
                continue

            if not location_name:
                print(f"Skipped a published venue in {slug!r} with no location_name.")
                continue

            if not venue_name:
                print(f"Skipped a published venue in {slug!r} with no venue_name.")
                continue

            venues_by_location[slug].append(row)

    for venues in venues_by_location.values():
        venues.sort(
            key=lambda venue: (
                parse_rank(venue.get("rank", "")),
                venue.get("venue_name", "").strip().casefold(),
            )
        )

    return dict(venues_by_location)


def make_liquid_image_path(image_path: str) -> str:
    """
    Convert a repository-relative image path into a Jekyll relative_url tag.

    Example input:
        assets/img/locations/venues/ash-barton-estate.webp

    Example output:
        {{ '/assets/img/locations/venues/ash-barton-estate.webp' | relative_url }}
    """
    cleaned_path = image_path.strip()

    if not cleaned_path:
        return ""

    if not cleaned_path.startswith("/"):
        cleaned_path = "/" + cleaned_path

    return "{{ '" + cleaned_path + "' | relative_url }}"


def build_venue_card(venue: dict[str, str]) -> str:
    """
    Generate one linked venue card.
    """
    venue_name = venue.get("venue_name", "").strip()
    venue_url = venue.get("venue_url", "").strip()
    venue_image = venue.get("venue_image", "").strip()
    location_name = venue.get("location_name", "").strip()

    if not venue_name:
        raise ValueError("A published venue has no venue_name.")

    if not venue_url:
        raise ValueError(f"Published venue {venue_name!r} has no venue_url.")

    if not venue_image:
        raise ValueError(f"Published venue {venue_name!r} has no venue_image.")

    safe_name = html.escape(venue_name, quote=True)
    safe_location = html.escape(location_name, quote=True)

    safe_url = html.escape(
        html.unescape(venue_url),
        quote=True,
    )

    liquid_image_path = make_liquid_image_path(venue_image)

    if safe_location:
        caption = f"{safe_name}, {safe_location}"
        alt_text = f"{safe_name}, {safe_location}"
    else:
        caption = safe_name
        alt_text = safe_name

    return (
        f'      <a class="venue-card" href="{safe_url}" target="_blank" rel="noopener">\n'
        f'        <img src="{liquid_image_path}" alt="{alt_text}" loading="lazy">\n'
        f'        <div class="venue-caption">{caption}</div>\n'
        f"      </a>"
    )


def build_venue_cards(
    venues: list[dict[str, str]],
) -> str:
    """Generate all venue cards for one location."""
    if not venues:
        return """      <p class="venues-gallery-empty">
        Venue information for this area will be added soon.
      </p>"""

    return "\n\n".join(build_venue_card(venue) for venue in venues)


def render_page(
    template: str,
    location_slug: str,
    location_name: str,
    venues: list[dict[str, str]],
) -> str:
    """
    Render one location page without using str.format().

    Explicit placeholder replacement preserves Jekyll Liquid expressions,
    JavaScript braces, template literals, and other brace-based syntax.
    """
    if template.count("__LOCATION_SLUG__") == 0:
        raise ValueError(
            "The __LOCATION_SLUG__ placeholder was not found in PAGE_TEMPLATE."
        )

    if template.count("__LOCATION_NAME__") == 0:
        raise ValueError(
            "The __LOCATION_NAME__ placeholder was not found in PAGE_TEMPLATE."
        )

    if template.count("__VENUE_CARDS__") != 1:
        raise ValueError(
            "PAGE_TEMPLATE must contain exactly one __VENUE_CARDS__ placeholder."
        )

    rendered = template.replace("__LOCATION_SLUG__", location_slug).replace(
        "__LOCATION_NAME__", location_name
    )

    # Find the closing delimiter of the YAML front matter.
    front_matter_end = rendered.find("---", 3)

    if front_matter_end == -1:
        raise ValueError("Could not find the closing '---' for the YAML front matter.")

    front_matter_end += 3

    front_matter = rendered[:front_matter_end]
    page_body = rendered[front_matter_end:]

    # Preserve entities in the YAML front matter, but turn the escaped page
    # body into functional HTML and JavaScript.
    decoded_page_body = html.unescape(page_body)

    # The cards are already functional HTML, so insert them after unescaping
    # the static portion of the template.
    venue_cards = build_venue_cards(venues)

    decoded_page_body = decoded_page_body.replace(
        "__VENUE_CARDS__",
        venue_cards,
        1,
    )

    return front_matter + decoded_page_body


def main() -> None:
    venues_by_location = load_venues_by_location(CSV_FILE)

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    generated_pages = 0

    for slug, venues in sorted(venues_by_location.items()):
        if not venues:
            continue

        location_name = venues[0].get("location_name", "").strip()

        if not location_name:
            print(f"Skipped location {slug!r} because it has no location_name.")
            continue

        # Ensure all venues grouped under a slug have the same displayed
        # location name.
        location_names = {
            venue.get("location_name", "").strip()
            for venue in venues
            if venue.get("location_name", "").strip()
        }

        if len(location_names) > 1:
            names = ", ".join(sorted(location_names))

            raise ValueError(
                f"Location slug {slug!r} has multiple location names: {names}"
            )

        output_file = OUTPUT_DIR / f"{slug}.html"

        page_content = render_page(
            template=PAGE_TEMPLATE,
            location_slug=slug,
            location_name=location_name,
            venues=venues,
        )

        output_file.write_text(
            page_content,
            encoding="utf-8",
            newline="\n",
        )

        generated_pages += 1

        print(
            f"Created {output_file} with "
            f"{len(venues)} published venue card(s) "
            f"and permalink /locations/{slug}/"
        )

    print(f"Generated {generated_pages} location page(s).")


if __name__ == "__main__":
    main()