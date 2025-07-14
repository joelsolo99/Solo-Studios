---
layout: default
title: Wedding Packages
permalink: /packages/wedding-packages/
---

<link rel="stylesheet" href="{{ '/assets/css/packages.css' | relative_url }}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<div class="wrapper">
  <h1>Wedding Packages</h1>

  <p>If you're planning a wedding in the South West, Solo Studios offers live saxophone music and DJ services that feel personal, professional, and completely tailored to your day. Whether it's a relaxed ceremony in Devon, a lively evening party in Cornwall, or a full wedding celebration in Plymouth, our sax and DJ packages are designed to create the perfect vibe, and memories that last.</p>

  <section class="fade-in-section left-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/wedding_packages/1.webp' | relative_url }}" alt="Sax + Backings Only – 2x45min" class="package-image">
      <div class="package-content">
        <h2>Sax + Backings Only</h2>
        <p><strong>Set:</strong> 2 × 45 mins<br>
           <strong>Total Duration:</strong> 2 hours<br>
           <strong>Price:</strong> From £500</p>
        <p>Ideal for a drinks reception or relaxed background music during photos — smooth sax backed by pro tracks that blend perfectly into the vibe of your afternoon.</p>
      </div>
    </div>
  </section>

  <section class="fade-in-section right-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/wedding_packages/2.webp' | relative_url }}" alt="Sax + Backings Only – 5x45min" class="package-image">
      <div class="package-content">
        <h2>Sax + Backings Only (Full Day Flex)</h2>
        <p><strong>Set:</strong> 5 × 45 mins (any time)<br>
           <strong>Total Duration:</strong> 5 hours<br>
           <strong>Price:</strong> From £1000</p>
        <p>A flexible option — tell us your timings, and we’ll take care of the rest. Perfect if you want music across multiple parts of the day without going full DJ.</p>
      </div>
    </div>
  </section>

  <section class="fade-in-section left-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/wedding_packages/3.webp' | relative_url }}" alt="Combo Deal Sax + DJ" class="package-image">
      <div class="package-content">
        <h2>Combo Deal (Sax + DJ)</h2>
        <p><strong>Set:</strong> 5pm – Midnight<br>
           <strong>Total Duration:</strong> 7 hours<br>
           <strong>Price:</strong> From £1200</p>
        <p>Smooth sax for cocktails, background music over dinner, a first-dance performance, and a full DJ set to keep the party going. This is our most popular package for a reason.</p>
      </div>
    </div>
  </section>

  <section class="fade-in-section right-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/wedding_packages/4.webp' | relative_url }}" alt="All-Day Package" class="package-image">
      <div class="package-content">
        <h2>The All-Day Package</h2>
        <p><strong>Set:</strong> 12pm – Midnight<br>
           <strong>Total Duration:</strong> 12 hours<br>
           <strong>Price:</strong> From £1600</p>
        <p>Everything in the Combo Deal, plus ceremony music, travel between locations, and a custom request, like learning a special song just for your moment.</p>
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
