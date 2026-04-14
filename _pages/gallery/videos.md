---
layout: page
title: Videos
permalink: gallery/videos/
---

<link rel="stylesheet" href="{{ '/assets/css/videos.css' | relative_url }}">

Take a look at some of our latest performances and highlights!

---

### Have a look at:
- [Party Vibes](#party-vibes) (perfect for your evening party)
- [Chilled Vibes](#chilled-vibes) (perfect for a drinks reception)

---

## <a id="party-vibes"></a>Party Vibes

<div class="video-grid">
  <div class="service" id="video-jubel">
    <h3 class="song-title">Jubel (LIVE)</h3>
    <p class="artist-name">Klingande</p>
    <div class="video-wrapper">
      <iframe src="https://youtube.com/embed/uuDLdVoHLs4" 
              title="Jubel Live!"
              frameborder="0" allowfullscreen></iframe>
    </div>
  </div>
  
  <div class="service" id="video-madness">
    <h3 class="song-title">One Step Beyond (LIVE)</h3>
    <p class="artist-name">Madness</p>
    <div class="video-wrapper">
      <iframe src="https://www.youtube.com/embed/uAOytebiu8E" 
              title="Madness: One Step Beyond"
              frameborder="0" allowfullscreen></iframe>
    </div>
  </div>
  

  <div class="service" id="video-pitbull">
    <h3 class="song-title">Fireball (LIVE Wedding Entrance)</h3>
    <p class="artist-name">Pitbull</p>
    <div class="video-wrapper">
      <iframe src="https://www.youtube.com/embed/uC-EWWkLyy0" 
              title="Fireball Wedding Entrance"
              frameborder="0" allowfullscreen></iframe>
    </div>
  </div>

  <div class="service" id="video-club">
    <h3 class="song-title">Club Classics</h3>
    <p class="artist-name">Party Vibes</p>
    <div class="video-wrapper">
      <iframe src="https://www.youtube.com/embed/xnP7DbxwX60" 
              title="18th Birthday Party"
              frameborder="0" allowfullscreen></iframe>
    </div>
  </div>
  
</div>

## <a id="chilled-vibes"></a>Chilled Vibes 

<div class="video-grid">
  <div class="service" id="video-valerie">
    <h3 class="song-title">Valerie</h3>
    <p class="artist-name">Mark Ronson Ft. Amy Winehouse</p>
    <div class="video-wrapper">
      <iframe src="https://www.youtube.com/embed/2Tvs8UwSdmw" 
              title="Valerie"
              frameborder="0" allowfullscreen></iframe>
    </div>
  </div>

  <div class="service" id="video-honky-tonk">
    <h3 class="song-title">Christmas Party</h3>
    <p class="artist-name">Chilled set at the Honky Tonk Wine Library</p>
    <div class="video-wrapper">
      <iframe src="https://www.youtube.com/embed/ZieWvyfOLJw" 
              title="Honky Tonk Set"
              frameborder="0" allowfullscreen></iframe>
    </div>
  </div>

  <div class="service" id="outdoor-pop">
    <h3 class="song-title">Garden Party Pop Collection</h3>
    <p class="artist-name">A collection of footage from a hen party</p>
    <div class="video-wrapper">
      <iframe src="https://www.youtube.com/embed/vPPcldkjnSk" 
              title="Madness: One Step Beyond"
              frameborder="0" allowfullscreen></iframe>
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


<script>
document.addEventListener("DOMContentLoaded", () => {
  const url = new URL(window.location.href);
  const autoplay = url.searchParams.get("autoplay");
  const targetID = url.hash;

  if (autoplay && targetID) {
    const wrapper = document.querySelector(targetID);
    if (wrapper && wrapper.querySelector("iframe")) {
      const iframe = wrapper.querySelector("iframe");
      const src = iframe.getAttribute("src");
      if (!src.includes("autoplay=1")) {
        const newSrc = src.includes("?") ? `${src}&autoplay=1` : `${src}?autoplay=1`;
        iframe.setAttribute("src", newSrc);

        // Scroll smoothly to video
        wrapper.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    }
  }
});
</script>


