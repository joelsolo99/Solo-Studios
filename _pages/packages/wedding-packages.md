---
layout: default
title: Wedding DJ & Sax Packages in Devon & Cornwall | Solo Studios
permalink: /packages/wedding-packages/
---

<link rel="stylesheet" href="{{ '/assets/css/packages.css' | relative_url }}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<div class="wrapper">
  <h1>Wedding Packages</h1>
    <p class="packages-intro">
      Music for every part of your wedding day, from the first drinks to the last dance.
    </p>

  <section class="fade-in-section left-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/wedding_packages/drinks_reception.webp' | relative_url }}" alt="Wedding DJ and sax performance packages" class="package-image package-image--drinks">
      <div class="package-content">
        <h2>We want your dream wedding to come true!</h2>
        <p>Our DJ and saxophone packages are designed to cover every moment of your wedding, from relaxed daytime sets to high‑energy evening celebrations. Everything is planned around your timings, your taste, and the flow of your day.</p>
        <ul>
          <li>
            <strong>Grand Entrance:</strong> Kick off your reception in style with a personalized musical welcome. As the DJ announces, "Please welcome Mr and Mrs", your chosen song fills the room. Our saxophonist accompanies your entrance, wowing your guests from the start.
          </li>
          <li>
            <strong>The First Dance:</strong> Your first dance deserves to be unforgettable. We'll tailor a sax performance to your chosen song, complete with lighting and atmosphere to match. Give the DJ a nod, and we'll invite your loved ones to join you on the dance floor. If you want sax in your first dance song, we can record it for you to practice to so there are no surprises on the big day!
          </li>
          <li>
            <strong>Your Signature Set:</strong> Whether it's rock ballads, swinging soundtracks, or Ibiza bangers, your night should sound like you. Share your favourite tracks and we'll build a custom set, either woven throughout the evening or delivered as a high-energy, uninterrupted playlist.
          </li>
        </ul>
      </div>
    </div>
  </section>

  <section class="fade-in-section left-offset">
    <div class="package-section">
      <video
        class="package-image package-video-cropped"
        autoplay
        muted
        loop
        playsinline
        aria-label="Drinks reception saxophone performance video"
      >
        <source src="{{ '/assets/img/wedding_packages/drinks_reception_loop.mp4' | relative_url }}" type="video/mp4">
        Your browser does not support the video tag.
      </video>

      <div class="package-content">
        <h2>Drinks Reception</h2>
        <p>
          <strong>Set:</strong> 2 × 45 mins<br>
          <strong>Total Duration:</strong> 2 hours<br>
          <strong>Price:</strong> From £450
        </p>
        <p>
          Ideal for a drinks reception, arrival music, or relaxed background music during photos.
          Smooth live sax backed by professional tracks that sit perfectly in the atmosphere
          without overpowering the moment.
        </p>
        <p>
          This package is designed to add style, warmth, and a polished live feel to the earlier
          part of your day, helping guests settle in while keeping everything feeling special.
        </p>
      </div>
    </div>
  </section>

  <section class="fade-in-section right-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/wedding_packages/5.webp' | relative_url }}" alt="Sax and Tracks package" class="package-image">
      <div class="package-content">
        <h2>Sax &amp; Tracks</h2>
        <p>
          <strong>Set:</strong> Your favourite tunes for 5 hours, with sax!<br>
          <strong>Total Duration:</strong> 5 hours<br>
          <strong>Price:</strong> From £800
        </p>
        <p>
          A flexible option. Tell us your timings, and we’ll take care of the rest. Includes a professional PA, vibrant and customisable lighting and a live sax set at a time of your choosing. We'll be there for 5 hours.
        </p>
      </div>
    </div>
  </section>

  <section class="fade-in-section left-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/wedding_packages/combo_deal.webp' | relative_url }}" alt="Combo Deal Sax and DJ" class="package-image">
      <div class="package-content">
        <h2>Combo Deal (Sax + DJ)</h2>
        <p>
          <strong>Set:</strong> 5pm – Midnight<br>
          <strong>Total Duration:</strong> 7 hours<br>
          <strong>Price:</strong> From £1100
        </p>
        <p>
          Smooth sax for cocktails, background music over dinner, a first-dance performance, and a full DJ set to keep the party going. Stage lighting, high-tech equipment and only the finest tunes. If you want a talented duo with <strong>chemistry</strong> then this is the package for you. This is our most popular package for a reason.
        </p>
      </div>
    </div>
  </section>

  <section class="fade-in-section right-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/wedding_packages/6.webp' | relative_url }}" alt="The All-Day Package" class="package-image">
      <div class="package-content">
        <h2>The All-Day Package</h2>
        <p>
          <strong>Set:</strong> 12pm – Midnight<br>
          <strong>Total Duration:</strong> 12 hours<br>
          <strong>Price:</strong> From £1600
        </p>
        <p>
          Everything in the Combo Deal, plus ceremony music, travel between locations, and custom requests, like learning a special song just for your moment.
        </p>
      </div>
    </div>
  </section>

  <section class="packages-cta">
    <div class="packages-cta__inner">
      <p class="packages-cta__eyebrow">Let’s plan your wedding</p>
      <h2>Music that feels personal, polished, and full of energy</h2>
      <p class="packages-cta__text">
        Whether you want elegant daytime music, a seamless evening flow, or an all-day soundtrack tailored around your plans, we can help you choose the right package for your celebration.
      </p>

      <div class="packages-cta__actions">
        <a href="/contact" class="packages-cta__button">Get in touch</a>
        <a href="/packages/power-hour/" class="packages-cta__link">Looking for Ibiza energy? Try the Power Hour</a>
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