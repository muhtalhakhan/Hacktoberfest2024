// Select the form and file input elements
const form = document.getElementById('csvUploadForm');
const responseMessage = document.getElementById('uploadResponse');

// Add an event listener to handle form submission
form.addEventListener('submit', function(event) {
  event.preventDefault();  // Prevent default form submission

  const fileInput = document.getElementById('csvFile');
  const file = fileInput.files[0];

  if (!file) {
    responseMessage.innerText = 'Please upload a CSV file.';
    return;
  }

  // Read and process the CSV file
  const reader = new FileReader();
  reader.onload = async function(e) {
    const csvContent = e.target.result;
    const parsedData = processCSV(csvContent);

    // Send the parsed data to a mock API endpoint
    try {
      const response = await fetch('https://mockapi.example.com/upload-csv', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(parsedData),
      });

      if (!response.ok) {
        throw new Error('Failed to submit CSV data');
      }

      const result = await response.json();
      responseMessage.innerText = 'File uploaded and processed successfully: ' + result.message;
    } catch (error) {
      responseMessage.innerText = 'Error: ' + error.message;
    }
  };

  reader.readAsText(file);  // Read the CSV file
});

// Function to process the CSV content
function processCSV(csvContent) {
  const rows = csvContent.split('\n');
  const data = rows.map(row => row.split(','));

  // Example cleaning: Remove rows with empty cells
  const cleanedData = data.filter(row => row.every(cell => cell.trim() !== ''));

  return cleanedData;  // Return cleaned CSV data
}
