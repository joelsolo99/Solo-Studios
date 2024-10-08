<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tracklist</title>
  <!-- Include Papa Parse library from CDN -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.0/papaparse.min.js"></script>
</head>
<body>
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
    // Function to fetch and parse CSV data
    function loadTracklist() {
      fetch('/assets/tracklists/classics.csv')
        .then(response => response.text())
        .then(csvData => {
          // Parse CSV data using Papa Parse
          Papa.parse(csvData, {
            header: true,  // Use header row
            skipEmptyLines: true,  // Skip empty lines
            complete: function (results) {
              const tableBody = document.querySelector('#tracklist-table tbody');
              
              // Loop through each row and populate the table
              results.data.forEach(row => {
                const tr = document.createElement('tr');
                
                // Create and append song and artist columns
                Object.values(row).forEach(col => {
                  const td = document.createElement('td');
                  td.textContent = col.trim();
                  tr.appendChild(td);
                });

                tableBody.appendChild(tr);
              });
            },
            error: function(error) {
              console.error('Error parsing CSV:', error);
            }
          });
        })
        .catch(error => console.error('Error loading tracklist:', error));
    }

    // Call the function on page load
    document.addEventListener('DOMContentLoaded', loadTracklist);
  </script>
</body>
</html>
