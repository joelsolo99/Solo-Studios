---
layout: default
title: Power Hour
permalink: /packages/power-hour/
---

<link rel="stylesheet" href="{{ '/assets/css/packages.css' | relative_url }}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<section class="fade-in-section left-offset">
  <div class="package-section">
    <img src="{{ '/assets/img/power_hour/power_hour.webp' | relative_url }}" alt="Power Hour Ibiza classics package" class="package-image">
    <div class="package-content">
      <h2>Power Hour</h2>
      <p><strong>Set:</strong> 1 hour of solid Ibiza classics<br>
         <strong>Total Duration:</strong> 1 hour<br>
         <strong>Price:</strong> From £350</p>
      <p>The ultimate way to get the party started. The <strong>Power Hour</strong> is a high-energy hour of Ibiza classics, designed to raise the atmosphere fast and get people on the dance floor from the very first tune.</p>
      <p>Perfect for weddings, birthdays, private parties, opening events, and all kinds of celebrations. It can stand alone as a big-impact set, or lead seamlessly into another package if you want to keep the energy going.</p>
      <ul>
        <li><strong>Big Ibiza anthems:</strong> A sharp, crowd-pleasing set packed with proven favourites.</li>
        <li><strong>Made for any event:</strong> Ideal wherever you want a quick hit of energy and a full dance floor.</li>
        <li><strong>Discount available:</strong> Book the Power Hour and you can get a discount on selected additional packages or follow-on sets.</li>
      </ul>
    </div>
  </div>
</section>


<div style="text-align: center; margin-top: 3rem;">
  <a href="/packages/terms/" style="font-size: 0.8rem; opacity: 0.6;">See terms and conditions</a><br>
  <a href="mailto:events@solostudios.uk" style="font-size: 0.8rem; opacity: 0.6;">Get in touch to book Power Hour</a>
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
