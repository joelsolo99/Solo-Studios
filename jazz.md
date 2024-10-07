<div class="tracklist-section">
  <h2>Jazz Tracklist</h2>
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


<script>
// Function to fetch CSV data
function loadTracklist() {
  fetch('/assets/tracklists/modern-pop.csv')
    .then(response => response.text())
    .then(csvData => {
      const rows = csvData.split('\n').slice(1); // Remove header row
      const tableBody = document.querySelector('#tracklist-table tbody');
      rows.forEach(row => {
        const cols = row.split(',');
        if (cols.length > 1) {  // To avoid empty rows
          const tr = document.createElement('tr');
          cols.forEach(col => {
            const td = document.createElement('td');
            td.textContent = col.trim();
            tr.appendChild(td);
          });
          tableBody.appendChild(tr);
        }
      });
    })
    .catch(error => console.error('Error loading tracklist:', error));
}

// Call the function on page load
document.addEventListener('DOMContentLoaded', loadTracklist);
</script>
