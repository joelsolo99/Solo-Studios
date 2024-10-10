<div class="tracklist-section">
  <h2>Classics Tracklist</h2>
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

<script>
// Function to fetch CSV data
function loadTracklist() {
  fetch('/assets/tracklists/classics.csv')
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
