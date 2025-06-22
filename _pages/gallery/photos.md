---
layout: default
title: Photo Gallery
permalink: /gallery/photos/
custom_css: photos.css
---

<link rel="stylesheet" href="{{ '/assets/css/photos.css' | relative_url }}">

<div class="wrapper">
  <div class="gallery-heading">Photo Gallery</div>

  <div class="gallery-grid">
    {% assign gallery_images = site.static_files | where_exp: "file", "file.path contains 'assets/img/photo_gallery'" %}
    {% for image in gallery_images %}
      <img src="{{ site.baseurl }}{{ image.path }}" alt="Gallery image" loading="lazy">
    {% endfor %}
  </div>
</div>
