---
layout: default
title: Photo Gallery
permalink: /gallery/photos/
custom_css: photos.css
---

<link rel="stylesheet" href="{{ '/assets/css/photos.css' | relative_url }}">


<div class="gallery-wrapper">
  <h1>Photo Gallery</h1>

  <div class="photo-grid">
    {% assign gallery_images = site.static_files | where_exp: "file", "file.path contains 'assets/img/photo_gallery'" %}
    {% for image in gallery_images %}
      <figure class="photo-tile">
        <img
          src="{{ site.baseurl }}{{ image.path }}"
          alt="{{ image.name | replace: '-', ' ' | replace: '_', ' ' | replace: '.jpg', '' | replace: '.jpeg', '' | replace: '.png', '' | replace: '.gif', '' }}"
          loading="lazy"
        >
      </figure>
    {% endfor %}
  </div>
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

  let index = 0;

  const open = i => {
    index = i;
    lbImg.src = images[i].src;
    lbCaption.textContent = images[i].alt || "";
    lightbox.hidden = false;
    document.body.style.overflow = "hidden";
  };

  const close = () => {
    lightbox.hidden = true;
    lbImg.src = "";
    document.body.style.overflow = "";
  };

  images.forEach((img, i) => {
    img.addEventListener("click", () => open(i));
  });

  document.getElementById("lb-close").onclick = close;
  document.getElementById("lb-prev").onclick = () => index > 0 && open(index - 1);
  document.getElementById("lb-next").onclick = () => index < images.length - 1 && open(index + 1);

  document.addEventListener("keydown", e => {
    if (lightbox.hidden) return;
    if (e.key === "Escape") close();
    if (e.key === "ArrowLeft" && index > 0) open(index - 1);
    if (e.key === "ArrowRight" && index < images.length - 1) open(index + 1);
  });
});
</script>