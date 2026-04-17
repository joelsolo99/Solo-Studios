---
layout: default
title: Christmas Party Packages
permalink: /packages/christmas-party-packages/
---

<link rel="stylesheet" href="{{ '/assets/css/packages.css' | relative_url }}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<div class="wrapper">
  <h1>Christmas Party Packages</h1>

  <p>
    Celebrate the festive season in style with our Christmas party packages. Whether you are after
    smooth background jazz or a high-energy dancefloor experience, we have the perfect option for your event.
  </p>

  <section class="fade-in-section left-offset">
    <div class="package-section">
      <div class="package-content">
        <h2>Stay Frosty</h2>
        <p>
          <strong>Set:</strong> 1 × 60 mins<br>
          <strong>Total Duration:</strong> 1 hour<br>
          <strong>Price:</strong> From £300
        </p>
        <p>
          A calm and traditional sax performance with backing tracks. Ideal for setting the perfect
          Christmas atmosphere.
        </p>
      </div>
    </div>
  </section>

  <section class="fade-in-section right-offset">
    <div class="package-section">
      <div class="package-content">
        <h2>All I Want for Christmas is Sax</h2>
        <p>
          <strong>Set:</strong> 2 × 45 mins<br>
          <strong>Total Duration:</strong> 2 hours<br>
          <strong>Price:</strong> From £500
        </p>
        <p>
          A mix of festive classics and party favourites, performed live on sax with backing tracks.
          Great for drinks receptions or dinner entertainment.
        </p>
      </div>
    </div>
  </section>

  <section class="fade-in-section left-offset">
    <div class="package-section">
      <div class="package-content">
        <h2>Deck the Dancefloor</h2>
        <p>
          <strong>Set:</strong> 2 × 45 mins (sax) + DJ throughout<br>
          <strong>Total Duration:</strong> 2 hours<br>
          <strong>Price:</strong> From £800
        </p>
        <p>
          A lively option combining live sax with a full DJ set to get your guests dancing.
          Includes stage lighting for added atmosphere.
        </p>
      </div>
    </div>
  </section>

  <section class="fade-in-section right-offset">
    <div class="package-section">
      <div class="package-content">
        <h2>Sleigh My Name</h2>
        <p>
          <strong>Set:</strong> 4 hours (sax + DJ)<br>
          <strong>Total Duration:</strong> 4 hours<br>
          <strong>Price:</strong> From £1200
        </p>
        <p>
          A full evening of entertainment with live sax and DJ, featuring a mix of Christmas
          favourites and party anthems to keep the energy up all night.
        </p>
      </div>
    </div>
  </section>

  <section class="packages-cta">
    <div class="packages-cta__inner">
      <p class="packages-cta__eyebrow">Plan your Christmas party</p>
      <h2>Festive music with the right balance of atmosphere and energy</h2>
      <p class="packages-cta__text">
        From relaxed background sax to full festive dancefloor sets, we can tailor the perfect
        package to suit your venue, guests, and schedule.
      </p>

      <div class="packages-cta__actions">
        <a href="/contact" class="packages-cta__button">Get in touch</a>
        <a href="/packages/terms/" class="packages-cta__link">See terms and conditions</a>
      </div>
    </div>
  </section>

  <div class="package-footer-links">
    <a href="/packages/terms/">See terms and conditions</a><br>
    <a href="/contact">Get in touch to tailor your Christmas package</a>
  </div>
</div>

<script src="{{ '/assets/js/snowstorm.js' | relative_url }}"></script>

<script>
  document.addEventListener("DOMContentLoaded", function() {
    const faders = document.querySelectorAll('.fade-in-section');

    const appearOptions = {
      threshold: 0.1,
      rootMargin: "0px 0px -100px 0px"
    };

    const appearOnScroll = new IntersectionObserver(function(entries, observer) {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      });
    }, appearOptions);

    faders.forEach(fader => {
      appearOnScroll.observe(fader);
    });

    if (typeof snowStorm !== 'undefined') {
      snowStorm.snowColor = '#008080';
      snowStorm.flakesMax = 500;
      snowStorm.animationInterval = 40;
      snowStorm.flakeWidth = 16;
      snowStorm.flakeHeight = 16;
    }
  });
</script>