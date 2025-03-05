---
layout: page
title: "Videos"
permalink: /videos/
---

<link rel="stylesheet" href="/assets/css/dark-theme.css">

<div class="hero-section">
  <h1>Solo Studios Videos</h1>
  <p>Explore our latest performances and projects.</p>
</div>

<section class="services-section" id="video-gallery">
  <!-- Videos will be loaded here -->
</section>

<div class="about-section">
  <h2>Subscribe for More</h2>
  <p>Stay updated with our latest content by subscribing to our <a href="https://www.youtube.com/@SoloStudiosPlymouth" target="_blank">YouTube channel</a>.</p>
</div>

<hr>

<footer>
  <p>&copy; {{ site.time | date: '%Y' }} Solo Studios. All rights reserved.</p>
</footer>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    const apiKey = 'AIzaSyDoCCWQiiix2fQ7FFgqta4NX19PIOgtbFk';
    const channelId = 'UCy7HLWwKq2PASi6DPd7OJdw';
    const maxResults = 5;
    const apiUrl = `https://www.googleapis.com/youtube/v3/search?key=${apiKey}&channelId=${channelId}&part=snippet,id&order=date&maxResults=${maxResults}`;

    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        const videoGallery = document.getElementById('video-gallery');
        if (data.items) {
          data.items.forEach(item => {
            if (item.id.videoId) {
              const videoId = item.id.videoId;
              const videoTitle = item.snippet.title;
              const videoElement = `
                <div class="service">
                  <h2>${videoTitle}</h2>
                  <iframe width="100%" height="315" src="https://www.youtube.com/embed/${videoId}" frameborder="0" allowfullscreen></iframe>
                </div>
              `;
              videoGallery.innerHTML += videoElement;
            }
          });
        } else {
          videoGallery.innerHTML = '<p>No videos found.</p>';
        }
      })
      .catch(error => {
        console.error('Error fetching videos:', error);
        document.getElementById('video-gallery').innerHTML = '<p>Failed to load videos.</p>';
      });
  });
</script>
