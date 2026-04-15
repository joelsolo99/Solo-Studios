---
title: "About Us"
permalink: /about/
layout: default
---

<link rel="stylesheet" href="{{ '/assets/css/about.css' | relative_url }}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<div class="about-page">
  <div class="wrapper">
    <h1 class="page-title">About Us</h1>
    <p class="page-intro">
      Live saxophone, DJ sets, and tailored event music across Plymouth and the South West.
      We bring the energy of a great party with the flexibility to shape the soundtrack around your day.
    </p>

    <section class="about-section fade-in-section left-offset">
      <div class="about-image-wrapper">
        <img src="{{ '/assets/img/about/1.webp' | relative_url }}" alt="Joel Solomons playing saxophone" class="about-image">
      </div>
      <div class="about-overlay">
        <h2>Hi, I'm Joel Solomons</h2>
        <p>I run Solo Studios. I'm a Royal College of Music-trained saxophonist and clarinettist, and I've spent years bringing live music to weddings, parties, and events across the South West. Based in Plymouth, I love getting people up on the dancefloor, singing along, and dancing to some of my favourite music.</p>
      </div>
    </section>

    <section class="about-section fade-in-section right-offset">
      <div class="about-image-wrapper">
        <img src="{{ '/assets/img/dj-dancefloor.webp' | relative_url }}" alt="DJ performance at an event" class="about-image about-image--dj-focus">
      </div>
      <div class="about-overlay">
        <h2>Meet Our DJ</h2>
        <p>Our DJ Jovan Allen has over five years of experience behind the decks and was previously a house DJ at a local venue. He has performed at weddings, private parties, and corporate events, always matching the music to the energy of the room.</p>
      </div>
    </section>

    <section class="about-section fade-in-section left-offset">
      <div class="about-image-wrapper">
        <img src="{{ '/assets/img/inflatable.webp' | relative_url }}" alt="DJ and saxophone performance at an event" class="about-image">
      </div>
      <div class="about-overlay">
        <h2>What We Offer</h2>
        <p>If you're looking for a sax for hire in Plymouth, Devon, or Cornwall, you're in the right place. Whether it is an intimate sax set for a wedding ceremony, a party sax set to get guests dancing, or a DJ and sax combo to keep the dancefloor full all night, Solo Studios can deliver.</p>
        <p>We are regularly booked for wedding sax hire, event musicians, and mobile DJs across the South West, and we tailor every performance to suit your day properly.</p>
      </div>
    </section>

    <section class="about-cta">
      <div class="about-cta__inner">
        <p class="about-cta__eyebrow">Let's plan your event</p>
        <h2>Music that feels personal, polished, and full of energy</h2>
        <p class="about-cta__text">
          We are flexible and always happy to learn new music to personalise your event.
          If you are looking for a top-tier saxophonist, DJ, or both, we would love to hear about your plans.
        </p>

        <div class="about-cta__actions">
          <a href="mailto:events@solostudios.uk" class="about-cta__button">Get in touch</a>
          <a href="/packages/wedding-packages/" class="about-cta__link">See our wedding packages</a>
        </div>
      </div>
    </section>
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
