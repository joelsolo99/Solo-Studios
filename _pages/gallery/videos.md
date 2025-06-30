---
layout: page
title: Videos
permalink: gallery/videos/
---

<link rel="stylesheet" href="{{ '/assets/css/videos.css' | relative_url }}">

Take a look at some of our latest performances and highlights!

---

### Jump to:
- [Party Vibes](#party-vibes)
- [Solo Sax](#solo-sax)

---

## <a id="party-vibes"></a>Party Vibes

<div class="video-grid">
  <div class="service">
    <h3 class="song-title">Highlights</h3>
    <p class="artist-name">Wedding: Roswarne House, Cornwall</p>
    <div class="video-wrapper">
      <iframe src="https://www.youtube.com/embed/XGTYujEmczU?si=jIdW3ApMs0UtlcEi" 
              title="June 2025 Wedding: Highlight Reel"
              frameborder="0" allowfullscreen></iframe>
    </div>
  </div>

  <div class="service">
    <h3 class="song-title">Highlights</h3>
    <p class="artist-name">Hen Party: Bristol</p>
    <div class="video-wrapper">
      <iframe src="https://www.youtube.com/embed/vPPcldkjnSk?si=9YRIcF2sx0zfqsNB" 
              title="June 2025 Hen Party: Highlight Reel"
              frameborder="0" allowfullscreen></iframe>
    </div>
  </div>

  <div class="service">
    <h3 class="song-title">Highlights</h3>
    <p class="artist-name">Wedding: Palhawn Fort, Cornwall</p>
    <div class="video-wrapper">
      <iframe src="https://www.youtube.com/embed/P2BvXQ27y0o?si=j9mLojFEGp5L0NWA" 
              title="June 2025 DJ Demo"
              frameborder="0" allowfullscreen></iframe>
    </div>
  </div>
</div>

## <a id="solo-sax"></a>Solo Sax

<div class="video-grid">
  <div class="service">
    <h3 class="song-title">Jubel</h3>
    <p class="artist-name">Klingande</p>
    <div class="video-wrapper">
      <iframe src="https://www.youtube.com/embed/8h6FA_lBQIQ" 
              title="Klingande: Jubel"
              frameborder="0" allowfullscreen></iframe>
    </div>
  </div>

  <div class="service">
    <h3 class="song-title">Can't Help Falling in Love</h3>
    <p class="artist-name">Elvis Presley</p>
    <div class="video-wrapper">
      <iframe src="https://www.youtube.com/embed/7wbCDQSyBmc" 
              title="Elvis: Can't Help Falling in Love"
              frameborder="0" allowfullscreen></iframe>
    </div>
  </div>

  <div class="service">
    <h3 class="song-title">One Step Beyond</h3>
    <p class="artist-name">Madness</p>
    <div class="video-wrapper">
      <iframe src="https://www.youtube.com/embed/V9XAYfDN2Gs" 
              title="Madness: One Step Beyond"
              frameborder="0" allowfullscreen></iframe>
    </div>
  </div>
</div>

---

For more performances, follow us on [YouTube](https://www.youtube.com/@SoloStudiosPlymouth) and [Instagram](https://www.instagram.com/solo_studios_plymouth).

<script src="https://unpkg.com/masonry-layout@4/dist/masonry.pkgd.min.js"></script>
<script src="https://unpkg.com/imagesloaded@4/imagesloaded.pkgd.min.js"></script>

<script>
document.addEventListener("DOMContentLoaded", () => {
  const gridContainers = document.querySelectorAll('.video-grid');
  
  gridContainers.forEach(grid => {
    const masonry = new Masonry(grid, {
      itemSelector: '.service',
      percentPosition: true,
      gutter: 20
    });

    imagesLoaded(grid, () => {
      masonry.layout();
    });
  });
});
</script>
