# API Gateway

This is a basic Node.js and Express.js server that responds with "Hello, World!".

## Prerequisites

- Node.js (v14 or higher)
- npm (v6 or higher)

## Installation

1. Clone the repository:

```sh
git clone https://github.com/username/Hacktoberfest2024
cd api-gateway
```

2. Install dependencies:

```sh
npm install
```

## Usage

1. Start the server:

```sh
npm start
```

2. Open your browser and navigate to `http://localhost:3000` to see the "Hello, World!" message.

## Code Overview

### `index.js`

```javascript
const express = require("express");
const app = express();
const port = 3000;

app.get("/", (req, res) => {
  res.send("Hello, World!");
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
```

## Contributing

Feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License.
