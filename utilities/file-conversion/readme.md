# File Conversion Utilities

This folder contains utilities for converting JSON files to CSV format.

## Files Included

1. **`jsontocsv.js`**: A script that converts JSON files into CSV format. It supports custom delimiters and optional header inclusion.

2. **`input.json`**: A sample JSON file used as input for the conversion. The expected format is an array of objects, like so:

   ```json
   [
     {
       "name": "John Doe",
       "age": 28,
       "email": "john@example.com"
     },
     {
       "name": "Jane Doe",
       "age": 25,
       "email": "jane@example.com"
     }
   ]

3. **`output.csv`**: The generated CSV file that results from running the conversion script. It will be created after executing jsontocsv.js.