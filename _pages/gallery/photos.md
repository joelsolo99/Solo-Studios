---
layout: default
title: "Photo Gallery"
permalink: /gallery/photos/
---

<link rel="stylesheet" href="{{ '/assets/css/photos.css' | relative_url }}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<div class="gallery-page">
  <div class="gallery-wrapper">
    <header class="gallery-hero">
      <p class="gallery-hero__eyebrow">Recent moments</p>
      <h1>Photo Gallery</h1>

      <p class="gallery-hero__intro">
        A selection of moments from weddings, parties, and live sets across the South West.
        Tap any image to open it larger, then swipe through the gallery.
      </p>

      <div class="gallery-hero__meta" aria-label="Photo gallery details">
        <span class="gallery-hero__pill">Weddings</span>
        <span class="gallery-hero__pill">Private parties</span>
        <span class="gallery-hero__pill">Live event moments</span>
      </div>
    </header>

    <section class="gallery-grid-section" aria-label="Photo gallery">
      <div class="photo-grid">
        {% assign gallery_images = site.static_files | where_exp: "file", "file.path contains 'assets/img/photo_gallery'" | sort: "path" %}
        {% for image in gallery_images %}
          {% assign image_alt = image.name
            | replace: '-', ' '
            | replace: '_', ' '
            | replace: '.jpg', ''
            | replace: '.jpeg', ''
            | replace: '.png', ''
            | replace: '.gif', ''
            | replace: '.webp', ''
          %}

          <figure
            class="photo-tile"
            role="button"
            tabindex="0"
            aria-label="Open photo: {{ image_alt }}"
          >
            <img
              src="{{ image.path | relative_url }}"
              alt="{{ image_alt }}"
              loading="lazy"
              decoding="async"
            >
          </figure>
        {% endfor %}
      </div>
    </section>

    <section class="gallery-cta" aria-labelledby="gallery-cta-title">
      <div class="gallery-cta__inner">
        <p class="gallery-cta__eyebrow">Planning something?</p>

        <h2 id="gallery-cta-title">Tell us what you have in mind</h2>

        <p class="gallery-cta__text">
          If you are planning a wedding, private party, or event, send over a few details and we will point you in the right direction.
        </p>

        <div class="gallery-cta__actions">
          <a href="/#contact-us" class="gallery-cta__button">Tell us about your event</a>
          <a href="https://www.youtube.com/@SoloStudiosPlymouth" target="_blank" rel="noopener noreferrer" class="gallery-cta__link">YouTube</a>
          <a href="https://www.instagram.com/solo_studios_plymouth" target="_blank" rel="noopener noreferrer" class="gallery-cta__link">Instagram</a>
        </div>
      </div>
    </section>
  </div>
</div>

<div
  id="lightbox"
  role="dialog"
  aria-modal="true"
  aria-label="Photo viewer"
  hidden
>
  <button id="lb-close" type="button" aria-label="Close photo viewer">×</button>
  <button id="lb-prev" type="button" aria-label="Previous photo">‹</button>

  <div class="lightbox-stage">
    <img id="lb-image" alt="">
  </div>

  <button id="lb-next" type="button" aria-label="Next photo">›</button>

  <div id="lb-caption" aria-live="polite"></div>
  <div id="lb-counter" aria-live="polite"></div>
</div>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    const tiles = Array.from(document.querySelectorAll(".photo-tile"));
    const images = tiles
      .map(function (tile) {
        return tile.querySelector("img");
      })
      .filter(Boolean);

    const lightbox = document.getElementById("lightbox");
    const lbImg = document.getElementById("lb-image");
    const lbCaption = document.getElementById("lb-caption");
    const lbCounter = document.getElementById("lb-counter");
    const lbClose = document.getElementById("lb-close");
    const lbPrev = document.getElementById("lb-prev");
    const lbNext = document.getElementById("lb-next");

    let index = 0;
    let lastFocusedElement = null;

    let touchStartX = 0;
    let touchStartY = 0;
    let touchEndX = 0;
    let touchEndY = 0;

    const minSwipeDistance = 45;
    const maxVerticalDrift = 70;

    function updateButtons() {
      const isFirst = index <= 0;
      const isLast = index >= images.length - 1;

      lbPrev.disabled = isFirst;
      lbNext.disabled = isLast;

      lbPrev.setAttribute("aria-disabled", String(isFirst));
      lbNext.setAttribute("aria-disabled", String(isLast));
    }

    function updateCounter() {
      if (!lbCounter) return;
      lbCounter.textContent = images.length ? `${index + 1} of ${images.length}` : "";
    }

    function showPhoto(newIndex) {
      if (!images.length) return;

      index = Math.max(0, Math.min(newIndex, images.length - 1));

      const image = images[index];
      const imageSrc = image.currentSrc || image.src;
      const altText = image.alt || "Gallery photo";

      lbImg.src = imageSrc;
      lbImg.alt = altText;
      lbCaption.textContent = altText;

      updateButtons();
      updateCounter();
    }

    function openLightbox(newIndex) {
      if (!images.length) return;

      lastFocusedElement = document.activeElement;

      showPhoto(newIndex);

      lightbox.hidden = false;
      document.body.style.overflow = "hidden";

      lbClose.focus();
    }

    function closeLightbox() {
      lightbox.hidden = true;

      lbImg.src = "";
      lbImg.alt = "";
      lbCaption.textContent = "";

      if (lbCounter) {
        lbCounter.textContent = "";
      }

      document.body.style.overflow = "";

      if (lastFocusedElement && typeof lastFocusedElement.focus === "function") {
        lastFocusedElement.focus();
      }
    }

    function showPreviousPhoto() {
      if (index > 0) {
        showPhoto(index - 1);
      }
    }

    function showNextPhoto() {
      if (index < images.length - 1) {
        showPhoto(index + 1);
      }
    }

    function handleSwipe() {
      const horizontalDistance = touchEndX - touchStartX;
      const verticalDistance = Math.abs(touchEndY - touchStartY);

      if (verticalDistance > maxVerticalDrift) return;
      if (Math.abs(horizontalDistance) < minSwipeDistance) return;

      if (horizontalDistance < 0) {
        showNextPhoto();
      } else {
        showPreviousPhoto();
      }
    }

    tiles.forEach(function (tile, tileIndex) {
      tile.addEventListener("click", function () {
        openLightbox(tileIndex);
      });

      tile.addEventListener("keydown", function (event) {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          openLightbox(tileIndex);
        }
      });
    });

    lbClose.addEventListener("click", closeLightbox);
    lbPrev.addEventListener("click", showPreviousPhoto);
    lbNext.addEventListener("click", showNextPhoto);

    lightbox.addEventListener("click", function (event) {
      if (event.target === lightbox) {
        closeLightbox();
      }
    });

    lightbox.addEventListener(
      "touchstart",
      function (event) {
        if (!event.changedTouches || event.changedTouches.length === 0) return;

        touchStartX = event.changedTouches[0].screenX;
        touchStartY = event.changedTouches[0].screenY;
      },
      { passive: true }
    );

    lightbox.addEventListener(
      "touchend",
      function (event) {
        if (!event.changedTouches || event.changedTouches.length === 0) return;

        touchEndX = event.changedTouches[0].screenX;
        touchEndY = event.changedTouches[0].screenY;

        handleSwipe();
      },
      { passive: true }
    );

    document.addEventListener("keydown", function (event) {
      if (lightbox.hidden) return;

      if (event.key === "Escape") {
        closeLightbox();
      }

      if (event.key === "ArrowLeft") {
        showPreviousPhoto();
      }

      if (event.key === "ArrowRight") {
        showNextPhoto();
      }

      if (event.key === "Tab") {
        const focusableElements = Array.from(
          lightbox.querySelectorAll("button:not([disabled])")
        );

        if (!focusableElements.length) return;

        const firstElement = focusableElements[0];
        const lastElement = focusableElements[focusableElements.length - 1];

        if (event.shiftKey && document.activeElement === firstElement) {
          event.preventDefault();
          lastElement.focus();
        } else if (!event.shiftKey && document.activeElement === lastElement) {
          event.preventDefault();
          firstElement.focus();
        }
      }
    });

    updateButtons();
    updateCounter();
  });
</script>