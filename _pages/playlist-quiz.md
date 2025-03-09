---
layout: page
title: "Wedding Playlist Quiz"
permalink: /playlist-quiz/
---

<link rel="stylesheet" href="/assets/css/dark-theme.css">

<section class="hero-section">
  <h1>Find Your Perfect Wedding Vibes</h1>
  <p>Answer a few fun questions and we'll create a sample playlist tailored to your day.</p>
</section>

<section class="about-section">
  <form id="playlist-quiz">
    <h2>1. What's your ideal party setting?</h2>
    <label><input type="radio" name="vibe" value="romantic"> Candlelit and dreamy</label><br>
    <label><input type="radio" name="vibe" value="rock"> Loud and energetic</label><br>
    <label><input type="radio" name="vibe" value="jazzy"> Cool and sophisticated</label><br>
    <label><input type="radio" name="vibe" value="meme"> Silly and unforgettable</label><br>

    <h2>2. Pick a decade to time travel to:</h2>
    <label><input type="radio" name="decade" value="80s"> 80s - Big hair, bigger tunes</label><br>
    <label><input type="radio" name="decade" value="90s"> 90s - Throwback bangers</label><br>
    <label><input type="radio" name="decade" value="2000s"> 2000s - Early noughties classics</label><br>
    <label><input type="radio" name="decade" value="current"> Current chart hits</label><br>

    <h2>3. How do you feel about 'meme' songs?</h2>
    <label><input type="radio" name="meme" value="love"> The more the better!</label><br>
    <label><input type="radio" name="meme" value="some"> A couple for a laugh</label><br>
    <label><input type="radio" name="meme" value="none"> Not at my wedding</label><br>

    <h2>4. What type of first dance are you imagining?</h2>
    <label><input type="radio" name="first_dance" value="slow"> A classic slow dance</label><br>
    <label><input type="radio" name="first_dance" value="fun"> Something upbeat and fun</label><br>
    <label><input type="radio" name="first_dance" value="unique"> A unique or mashup moment</label><br>

    <h2>5. What's your must-have genre?</h2>
    <label><input type="radio" name="genre" value="disco"> Disco Fever</label><br>
    <label><input type="radio" name="genre" value="indie"> Indie Anthems</label><br>
    <label><input type="radio" name="genre" value="garage"> UK Garage</label><br>
    <label><input type="radio" name="genre" value="rnb"> R&B Classics</label><br>

    <h2>6. What's the ultimate vibe for the late-night set?</h2>
    <label><input type="radio" name="latenight" value="chill"> Chill and soulful</label><br>
    <label><input type="radio" name="latenight" value="house"> Pumping house tracks</label><br>
    <label><input type="radio" name="latenight" value="karaoke"> Big singalong anthems</label><br>
    <label><input type="radio" name="latenight" value="cheese"> Pure cheese, please!</label><br>

    <br>
    <button type="button" onclick="generatePlaylist()" class="cta-button">Get Your Playlist</button>
  </form>

  <div id="playlist-result" style="margin-top:40px;"></div>
</section>

<script>
function generatePlaylist() {
  const vibe = document.querySelector('input[name="vibe"]:checked')?.value;
  const decade = document.querySelector('input[name="decade"]:checked')?.value;
  const meme = document.querySelector('input[name="meme"]:checked')?.value;
  const firstDance = document.querySelector('input[name="first_dance"]:checked')?.value;
  const genre = document.querySelector('input[name="genre"]:checked')?.value;
  const lateNight = document.querySelector('input[name="latenight"]:checked')?.value;

  if (!vibe || !decade || !meme || !firstDance || !genre || !lateNight) {
    alert('Please answer all questions!');
    return;
  }

  let playlist = '<h2>Your Sample Playlist</h2><ul>';

  if (vibe === 'romantic') playlist += '<li>Endless Love - Diana Ross & Lionel Richie</li><li>Young Hearts Run Free - Candi Staton</li>';
  if (vibe === 'rock') playlist += '<li>Livin\' On A Prayer - Bon Jovi</li><li>Sweet Child O\' Mine - Guns N\' Roses</li>';
  if (vibe === 'jazzy') playlist += '<li>Sexual Healing - Marvin Gaye</li><li>Roxanne - The Police</li>';
  if (vibe === 'meme') playlist += '<li>All Star - Smash Mouth</li><li>Mambo No. 5 - Lou Bega</li>';

  if (decade === '80s') playlist += '<li>Footloose - Kenny Loggins</li><li>Girls Just Want to Have Fun - Cyndi Lauper</li>';
  if (decade === '90s') playlist += '<li>You\'ve Got The Love - Florence + The Machine</li><li>Sex on Fire - Kings of Leon</li>';
  if (decade === '2000s') playlist += '<li>Levitating - Dua Lipa</li><li>Yeah! - Usher</li>';
  if (decade === 'current') playlist += '<li>Symphony - Clean Bandit ft. Zara Larsson</li><li>Ain\'t Nobody (Loves Me Better) - Felix Jaehn</li>';

  if (meme === 'love') playlist += '<li>Poker Face - Lady Gaga</li><li>It Wasn\'t Me - Shaggy</li>';
  if (meme === 'some') playlist += '<li>Dirty Cash - Adventures Of Stevie V.</li>';

  if (firstDance === 'slow') playlist += '<li>The Way You Look Tonight - Frank Sinatra</li>';
  if (firstDance === 'fun') playlist += '<li>Twist And Shout - The Beatles</li>';
  if (firstDance === 'unique') playlist += '<li>Pencil Full Of Lead - Paolo Nutini</li>';

  if (genre === 'disco') playlist += '<li>Stayin\' Alive - Bee Gees</li>';
  if (genre === 'indie') playlist += '<li>Take Me Out - Franz Ferdinand</li>';
  if (genre === 'garage') playlist += '<li>Flowers - Sweet Female Attitude</li>';
  if (genre === 'rnb') playlist += '<li>No Scrubs - TLC</li>';

  if (lateNight === 'chill') playlist += '<li>Redbone - Childish Gambino</li>';
  if (lateNight === 'house') playlist += '<li>One More Time - Daft Punk</li>';
  if (lateNight === 'karaoke') playlist += '<li>Mr. Brightside - The Killers</li>';
  if (lateNight === 'cheese') playlist += '<li>Cha Cha Slide - DJ Casper</li>';

  playlist += '</ul>';

  document.getElementById('playlist-result').innerHTML = playlist;
}
</script>
