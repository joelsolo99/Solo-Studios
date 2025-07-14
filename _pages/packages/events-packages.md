---
layout: default
title: Events Packages
permalink: /packages/events-packages/
---

<link rel="stylesheet" href="{{ '/assets/css/packages.css' | relative_url }}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<div class="wrapper">
  <h1>Events Packages</h1>

  <p>Make your event unforgettable with live saxophone and DJ entertainment. Whether it's a corporate gathering, a gala dinner, or a lively work party, we've got a package to suit the occasion.</p>

  <section class="fade-in-section left-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/events_packages/1.webp' | relative_url }}" alt="Background Sax" class="package-image">
      <div class="package-content">
        <h2>Background Sax</h2>
        <p><strong>Set:</strong> 2 x 45 mins</p>
        <p><strong>Total Duration:</strong> 2 hours</p>
        <p><strong>Price:</strong> From £500</p>
        <p>Perfect for networking events, drinks receptions, or black-tie dinners. Smooth, elegant saxophone playing to set the right atmosphere.</p>
      </div>
    </div>
  </section>

  <section class="fade-in-section right-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/events_packages/2.webp' | relative_url }}" alt="Sax & DJ Energiser" class="package-image">
      <div class="package-content">
        <h2>Sax & DJ Energiser</h2>
        <p><strong>Set:</strong> 2 x 45 mins (sax) + DJ throughout</p>
        <p><strong>Total Duration:</strong> 2 hours</p>
        <p><strong>Price:</strong> From £1000</p>
        <p>Designed to get the energy up! Great for product launches, networking after-parties, and team celebrations. Includes a stage lighting rig for a professional setup.</p>
      </div>
    </div>
  </section>

  <section class="fade-in-section left-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/events_packages/3.webp' | relative_url }}" alt="Evening Entertainment" class="package-image">
      <div class="package-content">
        <h2>Evening Entertainment</h2>
        <p><strong>Set:</strong> 4 hours (latest finish 10pm)</p>
        <p><strong>Total Duration:</strong> 4 hours</p>
        <p><strong>Price:</strong> From £1200</p>
        <p>A longer set for awards ceremonies, gala nights, and end-of-year parties. Live saxophone with a DJ to keep the vibe going all evening.</p>
      </div>
    </div>
  </section>

  <section class="fade-in-section right-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/events_packages/4.webp' | relative_url }}" alt="The Main Event" class="package-image">
      <div class="package-content">
        <h2>The Main Event</h2>
        <p><strong>Set:</strong> From start to finish</p>
        <p><strong>Total Duration:</strong> Full event duration</p>
        <p><strong>Price:</strong> From £1500</p>
        <p>We'll provide music throughout your entire event, from the welcome drinks to the final song. Includes request-taking (if provided in advance) for a fully tailored experience.</p>
      </div>
    </div>
  </section>

  <div style="text-align: center; margin-top: 3rem;">
    <a href="/packages/terms/" style="font-size: 0.8rem; opacity: 0.6;">See terms and conditions</a><br>
    <a href="mailto:events@solostudios.uk" style="font-size: 0.8rem; opacity: 0.6;">Get in touch to tailor your package</a>
  </div>
</div>

<script>
  document.addEventListener("DOMContentLoaded", function() {
    const faders = document.querySelectorAll('.fade-in-section');

    const appearOptions = {
      threshold: 0.1,
      rootMargin: "0px 0px -100px 0px"
    };

    const appearOnScroll = new IntersectionObserver(function(entries, appearOnScroll) {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('visible');
        appearOnScroll.unobserve(entry.target);
      });
    }, appearOptions);

    faders.forEach(fader => {
      appearOnScroll.observe(fader);
    });
  });
</script>
