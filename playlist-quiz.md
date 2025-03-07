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

  if (!vibe || !decade || !meme) {
    alert('Please answer all questions!');
    return;
  }

  let playlist = '<h2>Your Sample Playlist</h2><ul>';

  if (vibe === 'romantic') playlist += '<li>Endless Love - Lionel Richie & Diana Ross</li><li>Young Hearts Run Free - Candi Staton</li><li>You've Got The Love - Florence + The Machine</li><li>The Way You Look Tonight - Frank Sinatra</li><li>Sexual Healing - Marvin Gaye</li>';
  if (vibe === 'rock') playlist += '<li>Livin' On A Prayer - Bon Jovi</li><li>Sweet Child O' Mine - Guns N' Roses</li><li>Sex on Fire - Kings of Leon</li><li>White Wedding - Billy Idol</li><li>I Believe in a Thing Called Love - The Darkness</li>';
  if (vibe === 'jazzy') playlist += '<li>Roxanne - The Police</li><li>Car Wash - Rose Royce</li><li>Respect - Aretha Franklin</li><li>Karma Chameleon - Culture Club</li><li>Celebration - Kool & The Gang</li>';
  if (vibe === 'meme') playlist += '<li>All Star - Smash Mouth</li><li>Mambo No. 5 - Lou Bega</li><li>It Wasn't Me - Shaggy</li><li>Dirty Cash - Adventures Of Stevie V.</li><li>Push It - Salt-N-Pepa</li>';

  if (decade === '80s') playlist += '<li>Footloose - Kenny Loggins</li><li>Girls Just Want to Have Fun - Cyndi Lauper</li><li>Love Shack - The B-52's</li><li>Crocodile Rock - Elton John</li><li>Video Killed The Radio Star - The Buggles</li>';
  if (decade === '90s') playlist += '<li>You've Got The Love - Florence + The Machine</li><li>Sex on Fire - Kings of Leon</li><li>Livin' On A Prayer - Bon Jovi</li><li>Twist And Shout - The Beatles</li><li>Poker Face - Lady Gaga</li>';
  if (decade === '2000s') playlist += '<li>Levitating - Dua Lipa</li><li>Yeah! - Usher</li><li>Symphony - Clean Bandit ft. Zara Larsson</li><li>Cake By The Ocean - DNCE</li><li>Ain't Nobody (Loves Me Better) - Felix Jaehn</li>';
  if (decade === 'current') playlist += '<li>Symphony - Clean Bandit ft. Zara Larsson</li><li>Ain't Nobody (Loves Me Better) - Felix Jaehn</li><li>Levitating - Dua Lipa</li><li>Cake By The Ocean - DNCE</li><li>Dirty Cash - Adventures Of Stevie V.</li>';

  if (meme === 'love') playlist += '<li>Poker Face - Lady Gaga</li><li>It Wasn't Me - Shaggy</li><li>All Star - Smash Mouth</li><li>Mambo No. 5 - Lou Bega</li><li>Push It - Salt-N-Pepa</li>';
  if (meme === 'some') playlist += '<li>Dirty Cash - Adventures Of Stevie V.</li><li>Twist And Shout - The Beatles</li>';

  playlist += '</ul>';

  document.getElementById('playlist-result').innerHTML = playlist;
}
</script>
