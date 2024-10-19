# NYC Taxi Trip Data API

This project provides a FastAPI-based API for retrieving New York City taxi trip data. It allows users to query trip information based on a given timestamp and retrieve a specified number of results.

## Features

- Retrieve taxi trip data for a specific time range
- Configurable number of results
- Data caching for improved performance
- Dockerized application for easy deployment

## Technologies Used

- Python 3.10
- FastAPI
- Pandas
- PyArrow
- Docker

## Getting Started

### Prerequisites

- Docker
- Docker Compose (optional, for easier management)

### Installation and Running

1. Clone this repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Build the Docker image:
   ```
   docker build -t nyc-taxi-api .
   ```

3. Run the container:
   ```
   docker run -p 8000:8000 nyc-taxi-api
   ```

The API will be available at `http://localhost:8000`.

## API Endpoints

### GET /trips

Retrieve taxi trip data.

Query Parameters:
- `from_ms`: Unix timestamp in milliseconds (required)
- `n_results`: Number of results to return (default: 100)

Example:


GET /trips?from_ms=1674561748000&n_results=50

### GET /health

Check the health status of the API.

### GET /

Root endpoint that confirms the application is running.

## Project Structure

- `src/main.py`: Main application file that defines the FastAPI app and routes
- `src/backend.py`: Contains the business logic for data processing and retrieval
- `src/utils.py`: Utility functions
- `Dockerfile`: Defines the Docker image build process
- `requirements.txt`: Lists the Python dependencies

## Data Source

This API uses data from the NYC Taxi and Limousine Commission, available at:
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

## Caching

The application caches downloaded Parquet files in the `/tmp/taxiDataApi/` directory (configurable via the `CACHE_DIR` environment variable).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your chosen license here]
