# HTTP Health Check Program

## Overview

This program monitors the health of HTTP endpoints specified in a configuration file (YAML format). It sends periodic requests (every 15 seconds) to each endpoint, evaluates their health based on response time and HTTP status codes, and logs the availability percentage of each domain to the console.

## Features

- Supports GET and POST HTTP methods.
- Evaluates health based on:
  - HTTP status codes (`2xx` is considered "UP").
  - Response latency (must be under 500ms).
- Logs the status (`UP`/`DOWN`) of each request.
- Calculates and logs cumulative availability percentages for each domain.

## Requirements

- **Python 3.7+**
- Required Python packages:
  - `requests`
  - `PyYAML`

## Installation

1. Clone the repository or download the project files.
   ```bash
   git clone https://github.com/DivyamArora22/fetch-project.git
   cd fetch-project
   ```
2. Install the required dependencies:
   ```bash
   pip3 install pyyaml requests
   ```
3. Ensure you have a valid YAML configuration file (e.g., endpoints.yaml).

## Configuration File

The configuration file must be in YAML format and include details about HTTP endpoints. Each endpoint should have the following fields:

- `name` (required): A descriptive name for the endpoint.
- `url` (required): The HTTP/HTTPS address of the endpoint.
- `method` (optional): The HTTP method to use (default is `GET`).
- `headers` (optional): A dictionary of HTTP headers to include in the request.
- `body` (optional): JSON-encoded string for the request body (for POST requests).

### Example Configuration File

```yaml
- headers:
    user-agent: fetch-synthetic-monitor
  method: GET
  name: fetch index page
  url: https://fetch.com/

- headers:
    user-agent: fetch-synthetic-monitor
  method: GET
  name: fetch careers page
  url: https://fetch.com/careers

- body: '{"foo":"bar"}'
  headers:
    content-type: application/json
    user-agent: fetch-synthetic-monitor
  method: POST
  name: fetch some fake post endpoint
  url: https://fetch.com/some/post/endpoint

- name: fetch rewards index page
  url: https://www.fetchrewards.com/
```

## Usage

Run the program by providing the path to your configuration file as a command-line argument. The configuration file must be in YAML format and specify the HTTP endpoints to monitor.

```bash
python3 main.py <path-to-config-file>
```
### Example

Assuming your configuration file is named `endpoints.yaml`, you can run the program as follows:

```bash
python3 main.py endpoints.yaml
```
### Notes

- The program continuously monitors the specified HTTP endpoints every 15 seconds until manually stopped (e.g., by pressing `CTRL+C`).
- Ensure the configuration file path provided is correct and the file is well-formed.
- If the configuration file is invalid or missing required fields, the program may not function as expected.
- The program assumes:
  - The YAML file follows the specified schema.
  - All URLs provided are valid HTTP or HTTPS addresses.
- No persistent storage is used. All availability statistics are kept in memory and reset when the program is restarted.



