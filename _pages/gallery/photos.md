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
        <div class="caption">{{ image.name | replace: '-', ' ' | replace: '_', ' ' | replace: '.jpg', '' | replace: '.jpeg', '' | replace: '.png', '' | replace: '.gif', '' }}</div>
      </div>
    {% endfor %}
  </div>
</div>

<!-- Lightbox Modal -->
<div id="lightbox-modal" class="lightbox">
  <span id="lightbox-close" class="close">&times;</span>
  <img class="lightbox-content" id="lightbox-img" alt="">
  <div id="lightbox-caption" class="lightbox-caption"></div>
</div>

<script>
document.addEventListener("DOMContentLoaded", () => {
  const lightbox = document.getElementById("lightbox-modal");
  const lightboxImg = document.getElementById("lightbox-img");
  const lightboxCaption = document.getElementById("lightbox-caption");
  const closeBtn = document.getElementById("lightbox-close");

  // Lightbox open on image click
  document.querySelectorAll('.gallery-item img').forEach(img => {
    img.addEventListener('click', () => {
      lightbox.style.display = "block";
      lightboxImg.src = img.src;
      lightboxCaption.textContent = img.alt || "";
    });
  });

  // Close lightbox on close button click
  closeBtn.addEventListener('click', () => {
    lightbox.style.display = "none";
  });

  // Close lightbox if clicking outside the image
  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) {
      lightbox.style.display = "none";
    }
  });

  // Fade in images on load
  document.querySelectorAll('.gallery-item img').forEach(img => {
    if (img.complete) {
      img.classList.add('loaded');
    } else {
      img.addEventListener('load', () => {
        img.classList.add('loaded');
      });
    }
  });
});
</script>
