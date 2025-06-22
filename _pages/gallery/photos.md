---
layout: default
title: Photo Gallery
permalink: /gallery/photos/
custom_css: photos.css
---

<link rel="stylesheet" href="{{ '/assets/css/photos.css' | relative_url }}">

<div class="wrapper">
  <h1>Photo Gallery</h1>

  <div class="gallery-grid">
    {% assign gallery_images = site.static_files | where_exp: "file", "file.path contains 'assets/img/photo_gallery'" %}
    {% for image in gallery_images %}
      <div class="gallery-item">
        <img 
          src="{{ site.baseurl }}{{ image.path }}" 
          alt="{{ image.name | replace: '-', ' ' | replace: '_', ' ' | replace: '.jpg', '' | replace: '.jpeg', '' | replace: '.png', '' | replace: '.gif', '' }}" 
          loading="lazy"
        >
        <div class="caption">
          <strong>{{ image.name | replace: '-', ' ' | replace: '_', ' ' | replace: '.jpg', '' | replace: '.jpeg', '' | replace: '.png', '' | replace: '.gif', '' }}</strong>
        </div>
      </div>
    {% endfor %}
  </div>
</div>

<!-- Lightbox Modal -->
<div id="lightbox-modal" class="lightbox">
  <span id="lightbox-close" class="close">&times;</span>
  <div class="lightbox-inner">
    <img class="lightbox-content" id="lightbox-img" alt="">
    <div id="lightbox-caption" class="lightbox-caption"></div>
  </div>
</div>

<script>
document.addEventListener("DOMContentLoaded", () => {
  const lightbox = document.getElementById("lightbox-modal");
  const lightboxImg = document.getElementById("lightbox-img");
  const lightboxCaption = document.getElementById("lightbox-caption");
  const closeBtn = document.getElementById("lightbox-close");
  const galleryItems = document.querySelectorAll('.gallery-item img');
  const images = Array.from(galleryItems);
  let currentIndex = -1;

  function openLightbox(index) {
    const img = images[index];
    lightbox.style.display = "flex";
    lightboxImg.src = img.src;
    lightboxCaption.textContent = img.alt || "";
    lightboxCaption.classList.remove("fade-in");
    void lightboxCaption.offsetWidth;
    lightboxCaption.classList.add("fade-in");
    currentIndex = index;
  }

  images.forEach((img, index) => {
    img.addEventListener('click', () => openLightbox(index));
    if (img.complete) {
      img.classList.add('loaded');
    } else {
      img.addEventListener('load', () => img.classList.add('loaded'));
    }
  });

  closeBtn.addEventListener('click', () => lightbox.style.display = "none");

  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) lightbox.style.display = "none";
  });

  document.addEventListener('keydown', e => {
    if (lightbox.style.display === "flex") {
      if (e.key === "ArrowRight" && currentIndex < images.length - 1) openLightbox(currentIndex + 1);
      else if (e.key === "ArrowLeft" && currentIndex > 0) openLightbox(currentIndex - 1);
      else if (e.key === "Escape") lightbox.style.display = "none";
    }
  });
});
</script>
