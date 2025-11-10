---
layout: default
title: Party Packages
permalink: /packages/party-packages/
---

<link rel="stylesheet" href="{{ '/assets/css/packages.css' | relative_url }}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<div class="wrapper">
  <h1>Party Packages</h1>

  <p>Take a look at the core packages we offer for parties. Whether it's a milestone birthday, anniversary, celebration or just an excuse to get everyone you know together, we've got a package for you!</p>

  <section class="fade-in-section left-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/party_packages/1.webp' | relative_url }}" alt="The Classic" class="package-image">
      <div class="package-content">
        <h2>The Classic</h2>
        <p><strong>Set:</strong> 2 x 45 mins<br>
           <strong>Total Duration:</strong> 2 hours<br>
           <strong>Price:</strong> From £450</p>
        <p>Perfect for setting the mood at a birthday or celebration. We' tailor a playlist to your preferred genres and decades of music.</p>
      </div>
    </div>
  </section>

  <section class="fade-in-section right-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/party_packages/2.webp' | relative_url }}" alt="The Party Starter" class="package-image">
      <div class="package-content">
        <h2>The Party Starter</h2>
        <p><strong>Set:</strong> 2 x 45 mins (sax) + DJ throughout<br>
           <strong>Total Duration:</strong> 2 hours<br>
           <strong>Price:</strong> From £800</p>
        <p>A step up for those who want a more dynamic party atmosphere. Includes a full DJ set alongside sax and a stage lighting rig to get people on the dance floor.</p>
      </div>
    </div>
  </section>

  <section class="fade-in-section left-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/party_packages/3.webp' | relative_url }}" alt="The Dancefloor Experience" class="package-image">
      <div class="package-content">
        <h2>The Dancefloor Experience</h2>
        <p><strong>Set:</strong> 4 hours (latest finish 10pm)<br>
           <strong>Total Duration:</strong> 4 hours<br>
           <strong>Price:</strong> From £1200</p>
        <p>An extended session with live sax and DJ to keep the energy up throughout the evening. Ideal for milestone birthdays and lively celebrations.</p>
      </div>
    </div>
  </section>

  <section class="fade-in-section right-offset">
    <div class="package-section">
      <img src="{{ '/assets/img/party_packages/4.webp' | relative_url }}" alt="The All-Night Party" class="package-image">
      <div class="package-content">
        <h2>The All-Night Party</h2>
        <p><strong>Set:</strong> From start to finish<br>
           <strong>Total Duration:</strong> Full party duration<br>
           <strong>Price:</strong> From £1500</p>
        <p>We' provide music from the moment your party starts until the last guest leaves. Includes request-taking (if provided in advance) for a truly personal experience.</p>
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
