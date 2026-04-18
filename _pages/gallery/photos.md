---
layout: default
title: "Photo Gallery"
permalink: /gallery/photos/
---

<link rel="stylesheet" href="{{ '/assets/css/photos.css' | relative_url }}">

<div class="gallery-page">
  <div class="gallery-wrapper">
    <header class="gallery-hero">
      <p class="gallery-hero__eyebrow">Recent moments</p>
      <h1>Photo Gallery</h1>
      <p class="gallery-hero__intro">
        A selection of moments from weddings, parties, and live sets across the South West.
        Click any image to open it larger.
      </p>

      <div class="gallery-hero__meta" aria-label="Photo gallery details">
        <span class="gallery-hero__pill">Weddings</span>
        <span class="gallery-hero__pill">Private parties</span>
        <span class="gallery-hero__pill">Live event moments</span>
      </div>
    </header>

    <section class="gallery-grid-section" aria-label="Photo gallery">
      <div class="photo-grid">
        {% assign gallery_images = site.static_files | where_exp: "file", "file.path contains 'assets/img/photo_gallery'" %}
        {% for image in gallery_images %}
          <figure class="photo-tile">
            <img
              src="{{ site.baseurl }}{{ image.path }}"
              alt="{{ image.name | replace: '-', ' ' | replace: '_', ' ' | replace: '.jpg', '' | replace: '.jpeg', '' | replace: '.png', '' | replace: '.gif', '' | replace: '.webp', '' }}"
              loading="lazy"
            >
          </figure>
        {% endfor %}
      </div>
    </section>


  <section class="gallery-cta">
    <div class="gallery-cta__inner">
      <p class="gallery-cta__eyebrow">Planning something?</p>
      <h2>Tell us what you have in mind</h2>
      <p class="gallery-cta__text">
        If you are planning a wedding, private party, or event, send over a few details and we will point you in the right direction.
      </p>

      <div class="gallery-cta__actions">
        <a href="/contact/" class="gallery-cta__button">Tell us about your event</a>
        <a href="https://www.youtube.com/@SoloStudiosPlymouth" target="_blank" rel="noopener noreferrer" class="gallery-cta__link">YouTube</a>
        <a href="https://www.instagram.com/solo_studios_plymouth" target="_blank" rel="noopener noreferrer" class="gallery-cta__link">Instagram</a>
      </div>
    </div>
  </section>

</div>

<!-- Lightbox -->
<div id="lightbox" hidden>
  <button id="lb-close" aria-label="Close">×</button>
  <button id="lb-prev" aria-label="Previous">‹</button>
  <img id="lb-image" alt="">
  <button id="lb-next" aria-label="Next">›</button>
  <div id="lb-caption"></div>
</div>

<script>
document.addEventListener("DOMContentLoaded", () => {
  const images = [...document.querySelectorAll(".photo-tile img")];
  const lightbox = document.getElementById("lightbox");
  const lbImg = document.getElementById("lb-image");
  const lbCaption = document.getElementById("lb-caption");
  const lbClose = document.getElementById("lb-close");
  const lbPrev = document.getElementById("lb-prev");
  const lbNext = document.getElementById("lb-next");

  let index = 0;

  const open = (i) => {
    index = i;
    lbImg.src = images[i].src;
    lbImg.alt = images[i].alt || "";
    lbCaption.textContent = images[i].alt || "";
    lightbox.hidden = false;
    document.body.style.overflow = "hidden";
  };

  const close = () => {
    lightbox.hidden = true;
    lbImg.src = "";
    lbImg.alt = "";
    document.body.style.overflow = "";
  };

  images.forEach((img, i) => {
    img.addEventListener("click", () => open(i));
  });

  lbClose.addEventListener("click", close);
  lbPrev.addEventListener("click", () => {
    if (index > 0) open(index - 1);
  });
  lbNext.addEventListener("click", () => {
    if (index < images.length - 1) open(index + 1);
  });

  lightbox.addEventListener("click", (e) => {
    if (e.target === lightbox) close();
  });

  document.addEventListener("keydown", (e) => {
    if (lightbox.hidden) return;
    if (e.key === "Escape") close();
    if (e.key === "ArrowLeft" && index > 0) open(index - 1);
    if (e.key === "ArrowRight" && index < images.length - 1) open(index + 1);
  });
});
</script>