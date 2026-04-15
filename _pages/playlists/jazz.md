---
layout: default
title: Jazz Tracklist"
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ '/assets/css/jazz-playlist.css' | relative_url }}">

<div class="jazz-tracklist-page">
  <header class="tracklist-hero" aria-labelledby="jazz-tracklist-title">
    <h1 id="jazz-tracklist-title">Jazz Setlist</h1>
  </header>

  <section class="tracklist-card" aria-label="Jazz tracklist">
    <p class="sr-only" id="tracklist-status" aria-live="polite">Loading tracks...</p>

    <div class="tracklist-table-wrap">
      <table class="tracklist-table" id="tracklist-table">
        <caption class="sr-only">Jazz setlist showing song titles</caption>
        <thead>
          <tr>
            <th scope="col">Song</th>
          </tr>
        </thead>
        <tbody>
          <tr class="is-placeholder">
            <td>Loading setlist...</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</div>

<script>
(function () {
  const csvUrl = "{{ '/assets/tracklists/jazz.csv' | relative_url }}";
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
    if (className) row.className = className;

    const cell = document.createElement('td');
    cell.textContent = message;

    row.appendChild(cell);
    tableBody.appendChild(row);
  }

  function createTrackRow(song) {
    const row = document.createElement('tr');

    const songCell = document.createElement('td');
    songCell.className = 'song-cell';
    songCell.setAttribute('data-label', 'Song');
    songCell.textContent = song;

    row.appendChild(songCell);

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

        if (cols.length >= 1) {
          const song = cleanCell(cols[0]);

          if (song) {
            fragment.appendChild(createTrackRow(song));
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
      setMessageRow('Sorry, the setlist could not be loaded.', 'is-error');
      statusEl.textContent = 'Setlist unavailable';
    }
  }

  document.addEventListener('DOMContentLoaded', loadTracklist);
})();
</script>