---
layout: default
title: Wedding Packages
permalink: /packages/wedding-packages/
---

<link rel="stylesheet" href="{{ '/assets/css/packages.css' | relative_url }}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">



<section class="fade-in-section left-offset">
  <div class="package-section">
    <img src="{{ '/assets/img/wedding_packages/sax_lift_cropped.webp' | relative_url }}" alt="Wedding DJ & Sax Performance Packages" class="package-image">
    <div class="package-content">
      <h2>We want your dream wedding to come true!</h2>
      <p>Our DJ and saxophone packages are designed to elevate your celebration with unforgettable musical moments. Here's what we offer to make your big day truly spectacular:</p>
      <ul>
        <li>
          <strong>Grand Entrance:</strong> Kick off your reception in style with a personalized musical welcome. As the DJ announces, "Please welcome Mr and Mrs", your chosen song fills the room. Our saxophonist accompanies your entrance, wowing your guests from the start.
        </li>
        <li>
          <strong>The First Dance:</strong> Your first dance deserves to be unforgettable. We'll tailor a sax performance to your chosen song, complete with lighting and atmosphere to match. Give the DJ a nod, and we'll invite your loved ones to join you on the dance floor.
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
      <img src="{{ '/assets/img/wedding_packages/1.webp' | relative_url }}" alt="Sax + Backings Only – 2x45min" class="package-image">
      <div class="package-content">
        <h2>Sax + Backings Only</h2>
        <p><strong>Set:</strong> 2 × 45 mins<br>
           <strong>Total Duration:</strong> 2 hours<br>
           <strong>Price:</strong> From £450</p>
        <p>Ideal for a drinks reception or relaxed background music during photos — smooth sax backed by pro tracks that blend perfectly into the vibe of your afternoon.</p>
      </div>
    </div>
  </section>

  <section class="fade-in-section right-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/wedding_packages/2.webp' | relative_url }}" alt="Sax + Backings Only – 5x45min" class="package-image">
      <div class="package-content">
        <h2>Sax + Playlist Service</h2>
        <p><strong>Set:</strong> Your favourite tunes for 5 hours, with sax!<br>
           <strong>Total Duration:</strong> 5 hours<br>
           <strong>Price:</strong> From £800</p>
        <p>A flexible option. Tell us your timings, and we’ll take care of the rest. Includes a professional PA, vibrant and customisable lighting and a live sax set at a time of your choosing. We'll be there for 5 hours and you .exi</p>
      </div>
    </div>
  </section>

  <section class="fade-in-section left-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/wedding_packages/5.webp' | relative_url }}" alt="Combo Deal Sax + DJ" class="package-image">
      <div class="package-content">
        <h2>Combo Deal (Sax + DJ)</h2>
        <p><strong>Set:</strong> 5pm – Midnight<br>
           <strong>Total Duration:</strong> 7 hours<br>
           <strong>Price:</strong> From £1100</p>
        <p>Smooth sax for cocktails, background music over dinner, a first-dance performance, and a full DJ set to keep the party going. Stage lighting, high-tech equipment and only the finest tunes. If you want a talented duo with *chemistry* then this is the package for you. This is our most popular package for a reason.</p>
      </div>
    </div>
  </section>

  <section class="fade-in-section right-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/wedding_packages/6.webp' | relative_url }}" alt="All-Day Package" class="package-image">
      <div class="package-content">
        <h2>The All-Day Package</h2>
        <p><strong>Set:</strong> 12pm – Midnight<br>
           <strong>Total Duration:</strong> 12 hours<br>
           <strong>Price:</strong> From £1600</p>
        <p>Everything in the Combo Deal, plus ceremony music, travel between locations, and custom requests, like learning a special song just for your moment.</p>
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
