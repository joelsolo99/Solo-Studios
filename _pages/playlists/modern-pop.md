---
layout: default
title: "Modern Pop Tracklist"
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ '/assets/css/tracklist.css' | relative_url }}">

<div class="tracklist-page modern-pop-tracklist-page">
  <header class="tracklist-hero" aria-labelledby="modern-pop-tracklist-title">
    <p class="tracklist-hero__eyebrow">Contemporary favourites</p>
    <h1 id="modern-pop-tracklist-title">Modern Pop Tracklist</h1>

    <div class="tracklist-hero__intro">
      <p class="tracklist-hero__text">
        A guide to the newer pop tracks we can draw from when you want the set to feel current,
        upbeat, and easy for a crowd to get into.
      </p>

      <div class="tracklist-hero__meta" aria-label="Modern pop tracklist details">
        <span class="tracklist-hero__pill">Evening parties</span>
        <span class="tracklist-hero__pill">Current pop and chart tracks</span>
        <span class="tracklist-hero__pill">Upbeat but flexible</span>
      </div>
    </div>
  </header>

  <section class="tracklist-card" aria-label="Modern pop tracklist">
    <p class="sr-only" id="tracklist-status" aria-live="polite">Loading tracks...</p>

    <div class="tracklist-table-wrap">
      <table class="tracklist-table" id="tracklist-table">
        <caption class="sr-only">Modern pop tracklist showing song title and artist</caption>
        <thead>
          <tr>
            <th scope="col">Song</th>
            <th scope="col">Artist</th>
          </tr>
        </thead>
        <tbody>
          <tr class="is-placeholder">
            <td colspan="2">Loading tracklist...</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</div>

<script>
(function () {
  const csvUrl = "{{ '/assets/tracklists/modern-pop.csv' | relative_url }}";
  const tableBody = document.querySelector('#tracklist-table tbody');
  const statusEl = document.getElementById('tracklist-status');

  function parseCSVLine(line) {
    const result = [];
    let current = '';
    let inQuotes = false;

    for (let i = 0; i < line.length; i++) {
      const char = line[i];
      const next = line[i + 1];

      if (char === '"' && inQuotes && next === '"') {
        current += '"';
        i++;
      } else if (char === '"') {
        inQuotes = !inQuotes;
      } else if (char === ',' && !inQuotes) {
        result.push(current.trim());
        current = '';
      } else {
        current += char;
      }
    }

    result.push(current.trim());
    return result;
  }

  function cleanCell(value) {
    return value.replace(/(^"|"$)/g, '').trim();
  }

  function setMessageRow(message, className = '') {
    tableBody.innerHTML = '';

    const row = document.createElement('tr');
    if (className) {
      row.className = className;
    }

    const cell = document.createElement('td');
    cell.colSpan = 2;
    cell.textContent = message;

    row.appendChild(cell);
    tableBody.appendChild(row);
  }

  function createTrackRow(song, artist) {
    const row = document.createElement('tr');

    const songCell = document.createElement('td');
    songCell.className = 'song-cell';
    songCell.setAttribute('data-label', 'Song');
    songCell.textContent = song;

    const artistCell = document.createElement('td');
    artistCell.className = 'artist-cell';
    artistCell.setAttribute('data-label', 'Artist');
    artistCell.textContent = artist;

    row.appendChild(songCell);
    row.appendChild(artistCell);

    return row;
  }

  async function loadTracklist() {
    try {
      const response = await fetch(csvUrl);

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }

      const csvText = await response.text();
      const lines = csvText
        .split(/\r?\n/)
        .map(line => line.trim())
        .filter(Boolean);

      if (lines.length <= 1) {
        setMessageRow('No tracks available right now.', 'is-empty');
        statusEl.textContent = '0 tracks available';
        return;
      }

      const rows = lines.slice(1);
      const fragment = document.createDocumentFragment();
      let count = 0;

      rows.forEach(line => {
        const cols = parseCSVLine(line);

        if (cols.length >= 2) {
          const song = cleanCell(cols[0]);
          const artist = cleanCell(cols[1]);

          if (song || artist) {
            fragment.appendChild(createTrackRow(song, artist));
            count += 1;
          }
        }
      });

      tableBody.innerHTML = '';

      if (count === 0) {
        setMessageRow('No tracks available right now.', 'is-empty');
        statusEl.textContent = '0 tracks available';
        return;
      }

      tableBody.appendChild(fragment);
      statusEl.textContent = `${count} ${count === 1 ? 'track' : 'tracks'} loaded`;
    } catch (error) {
      console.error('Error loading tracklist:', error);
      setMessageRow('Sorry, the tracklist could not be loaded.', 'is-error');
      statusEl.textContent = 'Tracklist unavailable';
    }
  }

  document.addEventListener('DOMContentLoaded', loadTracklist);
})();
</script>