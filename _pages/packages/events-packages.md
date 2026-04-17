---
layout: default
title: Ibiza Sax & DJ Set for Events | Solo Studios
permalink: /packages/events-packages/
---

<link rel="stylesheet" href="{{ '/assets/css/packages.css' | relative_url }}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<div class="wrapper">
  <h1>Events Packages</h1>

  <p>
    Make your event unforgettable with live saxophone and DJ entertainment. Whether it is a corporate gathering,
    gala dinner, product launch, or lively work party, we have a package to suit the occasion.
  </p>

  <section class="fade-in-section left-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/events_packages/1.webp' | relative_url }}" alt="Background Sax package" class="package-image">
      <div class="package-content">
        <h2>Background Sax</h2>
        <p>
          <strong>Set:</strong> 2 × 45 mins<br>
          <strong>Total Duration:</strong> 2 hours<br>
          <strong>Price:</strong> From £450
        </p>
        <p>
          Perfect for networking events, drinks receptions, or black-tie dinners. Smooth, elegant saxophone
          playing to set the right atmosphere.
        </p>
      </div>
    </div>
  </section>

  <section class="fade-in-section right-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/events_packages/2.webp' | relative_url }}" alt="Sax and DJ Energiser package" class="package-image">
      <div class="package-content">
        <h2>Sax &amp; DJ Energiser</h2>
        <p>
          <strong>Set:</strong> 2 × 45 mins (sax) + DJ throughout<br>
          <strong>Total Duration:</strong> 2 hours<br>
          <strong>Price:</strong> From £800
        </p>
        <p>
          Designed to get the energy up. Great for product launches, networking after-parties, and team celebrations.
          Includes a stage lighting rig for a professional setup.
        </p>
      </div>
    </div>
  </section>

  <section class="fade-in-section left-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/events_packages/3.webp' | relative_url }}" alt="Evening Entertainment package" class="package-image">
      <div class="package-content">
        <h2>Evening Entertainment</h2>
        <p>
          <strong>Set:</strong> 4 hours (latest finish 10pm)<br>
          <strong>Total Duration:</strong> 4 hours<br>
          <strong>Price:</strong> From £1200
        </p>
        <p>
          A longer set for awards ceremonies, gala nights, and end-of-year parties. Live saxophone with a DJ to keep
          the vibe going all evening.
        </p>
      </div>
    </div>
  </section>

  <section class="fade-in-section right-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/events_packages/4.webp' | relative_url }}" alt="The Main Event package" class="package-image">
      <div class="package-content">
        <h2>The Main Event</h2>
        <p>
          <strong>Set:</strong> From start to finish<br>
          <strong>Total Duration:</strong> Full event duration<br>
          <strong>Price:</strong> From £1200
        </p>
        <p>
          We will provide music throughout your entire event, from the welcome drinks to the final song. Includes
          request-taking, if provided in advance, for a fully tailored experience.
        </p>
      </div>
    </div>
  </section>

  <section class="packages-cta">
    <div class="packages-cta__inner">
      <p class="packages-cta__eyebrow">Let’s plan your event</p>
      <h2>Music that feels polished, flexible, and memorable</h2>
      <p class="packages-cta__text">
        Whether you need elegant background music, a stronger evening atmosphere, or full event coverage,
        we can help shape the right package around your plans.
      </p>

      <div class="packages-cta__actions">
        <a href="/contact" class="packages-cta__button">Get in touch</a>
        <a href="/why-sax-and-dj/" class="packages-cta__link">Why choose sax and DJ?</a>
      </div>
    </div>
  </section>

  <div class="package-footer-links">
    <a href="/packages/terms/">See terms and conditions</a><br>
    <a href="/contact">Get in touch to tailor your package</a>
  </div>
</div>

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
  });
</script>