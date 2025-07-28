---
layout: default
title: "Ibiza Tracklist"
---


<link rel="stylesheet" href="{{ '/assets/css/ibiza-tracklist.css' | relative_url }}">
<link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">



<div class="tracklist-icons">
  <img src="{{ '/assets/img/vinyl.png' | relative_url }}" alt="Spinning Vinyl" class="vinyl-icon" />
  <img src="{{ '/assets/img/palm_tree.svg' | relative_url }}" alt="Palm Tree" class="palm-icon" />
</div>



<div class="tracklist-container">
  <div class="tracklist-section">
    <h1 class="neon-title-ibiza">Ibiza Tracklist</h1>
      <table class="tracklist-table" id="tracklist-table">
        <thead>
          <tr>
            <th>Song</th>
            <th>Artist</th>
          </tr>
        </thead>
        <tbody>
        <!-- Tracklist data will be inserted here by JavaScript -->
      </tbody>
    </table>
  </div>
</div>


<script>
// Function to fetch CSV data
function loadTracklist() {
  fetch('/assets/tracklists/ibiza-sax.csv')
    .then(response => response.text())
    .then(csvData => {
      const rows = csvData.split('\n').slice(1); // Remove header row
      const tableBody = document.querySelector('#tracklist-table tbody');
      rows.forEach(row => {
        const cols = row.split(',');
        if (cols.length > 1) {
          const tr = document.createElement('tr');

          const artistTd = document.createElement('td');
          artistTd.textContent = cols[0].trim();
          artistTd.setAttribute('data-label', 'Artist');

          const songTd = document.createElement('td');
          songTd.textContent = cols[1].trim();
          songTd.setAttribute('data-label', 'Song');

          tr.appendChild(songTd);
          tr.appendChild(artistTd);

          tableBody.appendChild(tr);
        }
      });
    })
    .catch(error => console.error('Error loading tracklist:', error));
}

document.addEventListener('DOMContentLoaded', loadTracklist);
</script>



