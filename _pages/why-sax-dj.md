---
title: "Why Sax and DJ?"
permalink: /why-sax-and-dj/
layout: default
---

<link rel="stylesheet" href="{{ '/assets/css/why-sax-dj.css' | relative_url }}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<div class="wrapper">
  <h1>Why Sax and DJ?</h1>

  {% assign points = 
    [
      {
        "title": "Best of Both Worlds",
        "text": "The DJ brings the beats and the energy, while the saxophone adds that live, expressive edge. In our experience, it's the fusion of electronic sound and real-time musicality that gets people up on the floor.",
        "image": "/assets/img/why-sax-dj/1.png"
      },
      {
        "title": "Versatility",
        "text": "Whether it's Ibiza-style house, classic soul or chart-topping pop, this setup adapts easily to your vibe, no matter if it's a beach wedding, marquee party or evening reception in a country manor.",
        "image": "/assets/img/why-sax-dj/2.png"
      },
      {
        "title": "High-Energy Performance",
        "text": "A good sax player doesn't just stand still...  They get right up in the crowd, respond to the moment, and interact with guests, giving the night a dynamic, electric feel.",
        "image": "/assets/img/why-sax-dj/3.png"
      },
      {
        "title": "Memorable Moments",
        "text": "From your first dance to that big drop when the sax cuts through with a solo, this combo delivers moments that people remember.",
        "image": "/assets/img/why-sax-dj/4.png"
      },
      {
        "title": "All-Day Entertainment, No Interruptions",
        "text": "Unlike traditional bands who need regular breaks, a sax and DJ duo can keep the music flowing all night. No awkward silences, no playlist filler: just live energy and expert control of the mood.",
        "image": "/assets/img/why-sax-dj/5.png"
      },
      {
        "title": "Tailored To You",
        "text": "You can personalise everything. Want your entrance song to hit just right? Fancy a romantic sax moment during the meal or a crowd-hyping solo at midnight? We'll make it happen.",
        "image": "/assets/img/why-sax-dj/6.png"
      },
      {
        "title": "Incredible Value",
        "text": "For a fraction of the cost of a full band, but still delivers the feeling of live music. That makes it ideal for couples or party organisers looking for unforgettable entertainment on a realistic budget.",
        "image": "/assets/img/why-sax-dj/7.png"
      }
    ]
  %}

  {% for point in points %}
    <section class="point-section fade-in-section {% if forloop.index0 | modulo: 2 == 0 %}left-offset{% else %}right-offset{% endif %}" 
             style="background-image: url('{{ point.image | relative_url }}')">
      <div class="overlay"></div>
      <div class="text-content">
        <h2>{{ point.title }}</h2>
        <p>{{ point.text }}</p>
      </div>
    </section>
  {% endfor %}
</div>

<script>
  // Fade in on scroll
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
