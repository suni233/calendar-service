# Calendar Service

## Introduction

This is a simple calendar service implemented using FastAPI. The service accepts calendar events comprised of a date-time and description in JSON format and saves them persistently. It provides endpoints to add events, fetch a specific event, and retrieve events within a specified date range.

## Features

- Add calendar events
- Retrieve events by ID
- List events within a date range
- Support for custom date-time formats

## Requirements

- Python 3.10+
- FastAPI
- Uvicorn

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/suni233/calendar-service.git
   cd calendar-service
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the FastAPI application:
   ```bash
   python app/main.py
   ```

2. Access the API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

- `GET /`: Welcome message.
- `POST /events`: Add a new event.
- `GET /events/{id}`: Retrieve an event by ID.
- `GET /events`: List events within a date range.



## Docker Setup

1. Build the Docker image:
   ```bash
   docker build -t calendar-service .
   ```

2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 calendar-service
   ```
   You can also override the host and port by passing environment variables:
   ```bash
   docker run -d -p 8000:8000 -e HOST="0.0.0.0" -e PORT="5000" calendar-service
   ```
