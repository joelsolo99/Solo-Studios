---
layout: default
title: Ibiza Sax & DJ Set for Weddings and Parties | Solo Studios
permalink: /packages/power-hour/
---

<link rel="stylesheet" href="{{ '/assets/css/packages.css' | relative_url }}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<div class="wrapper">
  <h1>Power Hour</h1>

  <p class="packages-intro">
    A focused, high-energy Ibiza sax set designed to lift the room fast.
    Power Hour is built for weddings, parties, private events, and celebrations where you want a big dancefloor moment.
  </p>

  <section class="fade-in-section left-offset" aria-labelledby="power-hour-main">
    <div class="package-section">
      <img
        src="{{ '/assets/img/power_hour/power_hour.webp' | relative_url }}"
        alt="Power Hour Ibiza sax package"
        class="package-image"
        loading="eager"
        decoding="async"
      >

      <div class="package-content">
        <h2 id="power-hour-main">Power Hour</h2>

        <p>
          <strong>Set:</strong> 1 hour of Ibiza classics and party anthems<br>
          <strong>Total duration:</strong> 1 hour<br>
          <strong>Price:</strong> From £350
        </p>

        <p>
          Power Hour is a sharp, high-impact live sax set built around big Ibiza classics,
          house favourites, and dancefloor-ready tracks. It is designed to raise the atmosphere quickly
          and get people moving from the first tune.
        </p>

        <p>
          It works brilliantly as a standalone party set, a surprise moment during a wedding reception,
          or a high-energy lead-in to a longer DJ or DJ and sax package.
        </p>

        <ul>
          <li>
            <strong>Big Ibiza energy:</strong>
            A concentrated hour of uplifting tracks, live sax hooks, and proven crowd favourites.
          </li>
          <li>
            <strong>Easy to fit into your event:</strong>
            Drop it into the evening party, after the first dance, during a birthday celebration,
            or as a headline moment at a private event.
          </li>
          <li>
            <strong>Can be added to other packages:</strong>
            Power Hour can work on its own or be paired with selected longer packages if you want
            the energy to continue.
          </li>
        </ul>
      </div>
    </div>
  </section>

  <section class="fade-in-section right-offset" aria-labelledby="power-hour-best-for">
    <div class="package-section">
      <img
        src="{{ '/assets/img/homepage/blur.webp' | relative_url }}"
        alt="Live saxophone party energy"
        class="package-image"
        loading="lazy"
        decoding="async"
      >

      <div class="package-content">
        <h2 id="power-hour-best-for">Best For Big Party Moments</h2>

        <p>
          Power Hour is ideal when you want a clear shift in energy. It gives the room a focal point,
          brings live performance into the party, and creates a memorable section of the night without
          needing a full evening booking.
        </p>

        <ul>
          <li>
            <strong>Weddings:</strong>
            A perfect post-first-dance lift, evening reception feature, or late-night surprise.
          </li>
          <li>
            <strong>Birthdays and private parties:</strong>
            A fast way to create a proper party atmosphere and get guests onto the dancefloor.
          </li>
          <li>
            <strong>Corporate and venue events:</strong>
            A polished live feature set that feels exciting without taking over the whole schedule.
          </li>
        </ul>
      </div>
    </div>
  </section>

  <section class="fade-in-section left-offset" aria-labelledby="power-hour-how-it-works">
    <div class="package-section">
      <img
        src="{{ '/assets/img/wedding_packages/combo_deal.webp' | relative_url }}"
        alt="DJ and sax evening package"
        class="package-image"
        loading="lazy"
        decoding="async"
      >

      <div class="package-content">
        <h2 id="power-hour-how-it-works">How It Fits Into the Night</h2>

        <p>
          The set can be timed around the part of the evening where you want the biggest impact.
          Some clients use it to start the dancefloor properly, while others save it for a peak-time moment.
        </p>

        <p>
          If you are already booking a wedding, party, or event package, Power Hour can often be added
          as a feature set. Tell us your timings, venue, and the kind of music you like, and we can suggest
          where it will work best.
        </p>

        <ul>
          <li>
            <strong>After the first dance:</strong>
            Shift straight into party mode.
          </li>
          <li>
            <strong>Mid-evening feature set:</strong>
            Give the night a live performance highlight.
          </li>
          <li>
            <strong>Standalone set:</strong>
            Add a compact, high-energy sax performance to a shorter event.
          </li>
        </ul>
      </div>
    </div>
  </section>

  <section class="packages-cta" aria-labelledby="power-hour-cta-title">
    <div class="packages-cta__inner">
      <p class="packages-cta__eyebrow">Bring the energy up fast</p>

      <h2 id="power-hour-cta-title">A sharp, high-impact set for weddings, parties, and events</h2>

      <p class="packages-cta__text">
        If you want a concentrated burst of Ibiza energy, Power Hour is the quickest way to lift the room.
        It can work as a standalone booking or as the perfect lead-in to a longer evening package.
      </p>

      <div class="packages-cta__actions">
        <a href="/#contact-us" class="packages-cta__button">Get in touch</a>
        <a href="/playlists/ibiza/" class="packages-cta__link">See the Ibiza tracklist</a>
      </div>
    </div>
  </section>

  <div class="package-footer-links">
    <a href="/packages/terms/">See terms and conditions</a><br>
    <a href="/#contact-us">Get in touch to book Power Hour</a>
  </div>
</div>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    const faders = document.querySelectorAll(".fade-in-section");

    const appearOptions = {
      threshold: 0.1,
      rootMargin: "0px 0px -100px 0px"
    };

    const appearOnScroll = new IntersectionObserver(function (entries, observer) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("visible");
        observer.unobserve(entry.target);
      });
    }, appearOptions);

    faders.forEach(function (fader) {
      appearOnScroll.observe(fader);
    });
  });
</script>