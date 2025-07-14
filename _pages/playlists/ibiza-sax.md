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
    <table class="tracklist-table" id="tracklist-table">
      <thead>
        <tr>
          <th>Artist</th>
          <th>Song</th>
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
        if (cols.length > 1) {  // To avoid empty rows
          const tr = document.createElement('tr');
          const songTd = document.createElement('td');
          const artistTd = document.createElement('td');

          // Set text content for song and artist cells
          songTd.textContent = cols[0].trim();
          artistTd.textContent = cols[1].trim();

          // Add data-label attributes for responsive design
          songTd.setAttribute('data-label', 'Song');
          artistTd.setAttribute('data-label', 'Artist');

          // Append cells to the row
          tr.appendChild(songTd);
          tr.appendChild(artistTd);
          tableBody.appendChild(tr);
        }
      });
    })
    .catch(error => console.error('Error loading tracklist:', error));
}

// Call the function on page load
document.addEventListener('DOMContentLoaded', loadTracklist);
</script>
