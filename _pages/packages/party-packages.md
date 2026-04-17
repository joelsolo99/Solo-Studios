---
layout: default
title: Ibiza Sax & DJ Set for Parties | Solo Studios
permalink: /packages/party-packages/
---

<link rel="stylesheet" href="{{ '/assets/css/packages.css' | relative_url }}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<div class="wrapper">
  <h1>Party Packages</h1>

  <p>
    Explore our core party packages. Whether you are planning a milestone birthday,
    anniversary, private celebration, or simply a great night with friends and family,
    we have an option to suit the atmosphere you want to create.
  </p>

  <section class="fade-in-section left-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/party_packages/1.webp' | relative_url }}" alt="The Classic party package" class="package-image">
      <div class="package-content">
        <h2>The Classic</h2>
        <p>
          <strong>Set:</strong> 2 × 45 mins<br>
          <strong>Total Duration:</strong> 2 hours<br>
          <strong>Price:</strong> From £450
        </p>
        <p>
          Perfect for setting the mood at a birthday or celebration. We will tailor a playlist
          around your preferred genres and favourite decades, creating a relaxed live set that
          feels personal and polished.
        </p>
      </div>
    </div>
  </section>

  <section class="fade-in-section right-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/jovan-decks.jpg' | relative_url }}" alt="The Party Starter package" class="package-image">
      <div class="package-content">
        <h2>The Party Starter</h2>
        <p>
          <strong>Set:</strong> 2 × 45 mins (sax) + DJ throughout<br>
          <strong>Total Duration:</strong> 2 hours<br>
          <strong>Price:</strong> From £800
        </p>
        <p>
          A step up for hosts who want a more dynamic party atmosphere. This package includes a full
          DJ set alongside live sax and stage lighting to help lift the energy and get guests onto
          the dance floor.
        </p>
      </div>
    </div>
  </section>

  <section class="fade-in-section left-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/party_packages/3.webp' | relative_url }}" alt="The Dancefloor Experience package" class="package-image">
      <div class="package-content">
        <h2>The Dancefloor Experience</h2>
        <p>
          <strong>Set:</strong> 4 hours (latest finish 10pm)<br>
          <strong>Total Duration:</strong> 4 hours<br>
          <strong>Price:</strong> From £1200
        </p>
        <p>
          An extended live sax and DJ session designed to keep the momentum building across the
          evening. Ideal for milestone birthdays and lively celebrations where you want a full,
          high-energy party atmosphere.
        </p>
      </div>
    </div>
  </section>

  <section class="fade-in-section right-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/party_packages/4.webp' | relative_url }}" alt="The All-Night Party package" class="package-image">
      <div class="package-content">
        <h2>The All-Night Party</h2>
        <p>
          <strong>Set:</strong> From start to finish<br>
          <strong>Total Duration:</strong> Full party duration<br>
          <strong>Price:</strong> From £1500
        </p>
        <p>
          We provide the music from the moment your party begins until the final track of the night.
          This is the best option for hosts who want full evening coverage, a seamless flow, and a
          soundtrack shaped around the people in the room.
        </p>
      </div>
    </div>
  </section>

  <section class="packages-cta">
    <div class="packages-cta__inner">
      <p class="packages-cta__eyebrow">Let's plan your party</p>
      <h2>Bring live energy to your celebration</h2>
      <p class="packages-cta__text">
        Whether you want a laid-back atmosphere, a lively dance floor, or music from the first guest
        to the final song, we can help shape the right package around your event.
      </p>

      <div class="packages-cta__actions">
        <a href="/contact" class="packages-cta__button">Get in touch</a>
        <a href="/packages/power-hour/" class="packages-cta__link">Looking for an Ibiza Power Hour?</a>
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