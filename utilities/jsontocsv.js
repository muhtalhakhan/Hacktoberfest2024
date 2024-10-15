const fs = require("fs");
const path = require("path");

/**
 * Converts a JSON file to CSV format
 * @param {string} inputFile - Path to the input JSON file
 * @param {string} outputFile - Path to the output CSV file
 * @param {Object} options - Conversion options
 * @param {string} options.delimiter - CSV delimiter (default: ',')
 * @param {boolean} options.includeHeaders - Whether to include headers in CSV (default: true)
 */
function convertJsonToCsv(inputFile, outputFile, options = {}) {
  const delimiter = options.delimiter || ",";
  const includeHeaders = options.includeHeaders !== false;

  try {
    const jsonData = JSON.parse(fs.readFileSync(inputFile, "utf8"));

    if (!Array.isArray(jsonData)) {
      throw new Error("Input JSON must be an array of objects");
    }

    const headers = Object.keys(jsonData[0]);

    let csvContent = "";
    if (includeHeaders) {
      csvContent += headers.join(delimiter) + "\n";
    }

    jsonData.forEach((obj) => {
      const row = headers.map((header) => {
        const value = obj[header];
        return typeof value === "string" ? `"${value}"` : value;
      });
      csvContent += row.join(delimiter) + "\n";
    });

    fs.writeFileSync(outputFile, csvContent, "utf8");

    console.log(`Conversion complete. CSV file saved as ${outputFile}`);
  } catch (error) {
    console.error("Error during conversion:", error.message);
  }
}

const inputFile = path.join(__dirname, "input.json");
const outputFile = path.join(__dirname, "output.csv");

convertJsonToCsv(inputFile, outputFile, {
  delimiter: ",",
  includeHeaders: true,
});

module.exports = { convertJsonToCsv };
