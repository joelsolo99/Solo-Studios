---
layout: default
title: Photo Gallery
permalink: /gallery/photos/
custom_css: photos.css
---

<div class="wrapper">
  <div class="gallery-heading">Photo Gallery</div>

  <div class="masonry-gallery">
    {% assign gallery_images = site.static_files | where_exp: "file", "file.path contains 'assets/img/photo_gallery'" %}
    {% for image in gallery_images %}
      {% assign filename = image.path | split: '/' | last %}
      {% assign alt_text = filename | remove: '.jpg' | remove: '.jpeg' | remove: '.png' | replace: '_', ' ' %}
      <div class="masonry-item">
        <img src="{{ image.path | relative_url }}" alt="{{ alt_text }}" loading="lazy" onload="this.classList.add('loaded');">
        <div class="caption">{{ alt_text }}</div>
      </div>
    {% endfor %}
  </div>
</div>

<!-- Lightbox modal -->
<div id="lightbox-modal" class="lightbox" onclick="closeLightbox()">
  <span class="close">&times;</span>
  <img class="lightbox-content" id="lightbox-img">
  <div id="lightbox-caption" class="lightbox-caption"></div>
</div>

<script>
  // Lightbox open
  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll('.masonry-item img').forEach(img => {
      img.addEventListener('click', function () {
        const modal = document.getElementById("lightbox-modal");
        const modalImg = document.getElementById("lightbox-img");
        const captionText = document.getElementById("lightbox-caption");
        modal.style.display = "block";
        modalImg.src = this.src;
        captionText.innerText = this.alt;
      });
    });
  });

  function closeLightbox() {
    document.getElementById("lightbox-modal").style.display = "none";
  }
</script>
