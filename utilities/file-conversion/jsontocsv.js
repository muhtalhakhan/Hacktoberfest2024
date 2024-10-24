const fs = require('fs');
const { program } = require('commander');
const path = require('path');

function convertJsonToCsv(inputFile, outputFile, options) {
  const jsonData = JSON.parse(fs.readFileSync(inputFile, 'utf-8'));

  // Check if jsonData is an array of objects
  if (!Array.isArray(jsonData) || typeof jsonData[0] !== 'object') {
    throw new Error('Input JSON must be an array of objects');
  }

  const delimiter = options.delimiter || ',';
  const includeHeaders = options.includeHeaders !== false;

  const headers = Object.keys(jsonData[0]);
  const csvData = jsonData.map(row => headers.map(header => JSON.stringify(row[header])).join(delimiter));

  if (includeHeaders) {
    csvData.unshift(headers.join(delimiter));
  }

  fs.writeFileSync(outputFile, csvData.join('\n'));
  console.log(`CSV file saved as ${outputFile}`);
}

// Set up CLI
program
  .version('1.0.0')
  .description('Convert JSON to CSV')
  .argument('<inputFile>', 'Input JSON file')
  .argument('<outputFile>', 'Output CSV file')
  .option('-d, --delimiter <char>', 'Specify the delimiter (default is ,)', ',')
  .option('-H, --no-headers', 'Exclude headers in the CSV output')
  .action((inputFile, outputFile, options) => {
    const inputFilePath = path.resolve(__dirname, inputFile);
    const outputFilePath = path.resolve(__dirname, outputFile);
    convertJsonToCsv(inputFilePath, outputFilePath, options);
  });

program.parse(process.argv);
