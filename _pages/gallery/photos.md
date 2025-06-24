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
        <div class="caption"><strong>{{ image.name | replace: '-', ' ' | replace: '_', ' ' | replace: '.jpg', '' | replace: '.jpeg', '' | replace: '.png', '' | replace: '.gif', '' }}</strong></div>
      </div>
    {% endfor %}
  </div>
</div>

<!-- Lightbox Modal -->
<div id="lightbox-modal" class="lightbox">
  <div class="lightbox-inner">
    <span id="lightbox-close" class="close">&times;</span>
    <button id="lightbox-prev" class="nav-arrow left">&#10094;</button>
    <button id="lightbox-next" class="nav-arrow right">&#10095;</button>
    <div class="lightbox-content">
      <img id="lightbox-img" alt="">
      <div id="lightbox-caption" class="lightbox-caption"></div>
    </div>
  </div>
</div>

<script src="https://unpkg.com/masonry-layout@4/dist/masonry.pkgd.min.js"></script>
<script src="https://unpkg.com/imagesloaded@4/imagesloaded.pkgd.min.js"></script>

<script>
document.addEventListener("DOMContentLoaded", () => {
  const lightbox = document.getElementById("lightbox-modal");
  const lightboxImg = document.getElementById("lightbox-img");
  const lightboxCaption = document.getElementById("lightbox-caption");
  const closeBtn = document.getElementById("lightbox-close");
  const prevBtn = document.getElementById("lightbox-prev");
  const nextBtn = document.getElementById("lightbox-next");

  const grid = document.querySelector('.gallery-grid');

  const masonry = new Masonry(grid, {
    itemSelector: '.gallery-item',
    percentPosition: true,
    gutter: 12
  });

  imagesLoaded(grid, () => {
    masonry.layout();
  });

  const images = Array.from(document.querySelectorAll('.gallery-item img'));
  let currentIndex = -1;

  const showImageAt = (index) => {
    const img = images[index];
    if (!img) return;
    lightboxImg.src = img.src;
    lightboxCaption.textContent = img.alt || "";
    currentIndex = index;
  };

  images.forEach((img, index) => {
    const parent = img.closest('.gallery-item');

    // Orientation class
    const setOrientation = () => {
      if (img.naturalWidth >= img.naturalHeight) {
        parent.classList.add('landscape');
      } else {
        parent.classList.add('portrait');
      }
    };

    if (img.complete) {
      setOrientation();
      img.classList.add('loaded');
    } else {
      img.addEventListener('load', () => {
        setOrientation();
        img.classList.add('loaded');
      });
    }

    // Lightbox open
    img.addEventListener('click', () => {
      lightbox.style.display = "flex";
      showImageAt(index);
    });
  });

  // Close lightbox
  closeBtn.addEventListener('click', () => lightbox.style.display = "none");
  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) lightbox.style.display = "none";
  });
  document.addEventListener('keydown', e => {
    if (e.key === "Escape") lightbox.style.display = "none";
  });

  // Arrow buttons
  prevBtn.addEventListener("click", () => {
    if (currentIndex > 0) showImageAt(currentIndex - 1);
  });

  nextBtn.addEventListener("click", () => {
    if (currentIndex < images.length - 1) showImageAt(currentIndex + 1);
  });

  // Keyboard arrow support
  document.addEventListener("keydown", e => {
    if (lightbox.style.display === "flex") {
      if (e.key === "ArrowLeft" && currentIndex > 0) {
        showImageAt(currentIndex - 1);
      } else if (e.key === "ArrowRight" && currentIndex < images.length - 1) {
        showImageAt(currentIndex + 1);
      }
    }
  });

  // Touch swipe support
  let touchStartX = 0;
  lightbox.addEventListener("touchstart", e => {
    touchStartX = e.changedTouches[0].screenX;
  });

  lightbox.addEventListener("touchend", e => {
    const touchEndX = e.changedTouches[0].screenX;
    const deltaX = touchEndX - touchStartX;

    if (Math.abs(deltaX) > 50) {
      if (deltaX > 0 && currentIndex > 0) {
        showImageAt(currentIndex - 1);
      } else if (deltaX < 0 && currentIndex < images.length - 1) {
        showImageAt(currentIndex + 1);
      }
    }
  });
});
</script>
