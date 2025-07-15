---
layout: default
title: "Jazz Tracklist"
---

<link rel="stylesheet" href="{{ '/assets/css/jazz-playlist.css' | relative_url }}">
<link href="https://fonts.googleapis.com/css2?family=Monoton&display=swap" rel="stylesheet">


<h1 class="neon-title">Jazz Setlist</h1>


<div class="tracklist-container">
  <div class="tracklist-section">
    <table class="tracklist-table" id="tracklist-table">
      <thead>
        <tr>
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
  fetch('/assets/tracklists/jazz.csv')
    .then(response => response.text())
    .then(csvData => {
      const rows = csvData.split('\n').slice(1); // Remove header row
      const tableBody = document.querySelector('#tracklist-table tbody');
      rows.forEach(row => {
        const cols = row.split(',').map(col => col.replace(/(^"|"$)/g, '').trim()); // Remove quotes and trim

        if (cols.length > 0) {  // Only check for the song column
          const tr = document.createElement('tr');
          const songTd = document.createElement('td');

          // Set text content for song cell
          songTd.textContent = cols[0]; // Only one column for song

          // Add data-label attributes for responsive design
          songTd.setAttribute('data-label', 'Song');

          // Append cell to the row
          tr.appendChild(songTd);
          tableBody.appendChild(tr);
        }
      });
    })
    .catch(error => console.error('Error loading tracklist:', error));
}

// Call the function on page load
document.addEventListener('DOMContentLoaded', loadTracklist);
</script>
