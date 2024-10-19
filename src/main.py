
# main application file that runs/serves/exposes/hosts/defines the FastAPI app & routes

from typing import Optional

from fastapi import FastAPI, Query
from loguru import logger
from pydantic import BaseModel

from src.backend import Trip, get_trips # import the Trip model and the get_trips function from the backend module

app = FastAPI() # create the FastAPI app instance


class TripsResponse(BaseModel): # response model for the trips endpoint
    trips: Optional[list[Trip]] = None # optional list of trips
    next_from_ms: Optional[int] = None # optional next from timestamp
    message: Optional[str] = None # optional message


@app.get('/trips', response_model=TripsResponse) # endpoint that returns a list of trips based on a given timestamp and a number of results
def get_trip(
    from_ms: int = Query(..., description='Unix milliseconds'),
    n_results: int = Query(100, description='Number of results to output'),
):
    # Log the received parameters
    logger.info(
        f'Received request with params from_ms: {from_ms}, n_results: {n_results}'
    )

    # get the trips from the backend
    trips: list[Trip] = get_trips(from_ms, n_results)

    # format the response object TripsResponse
    if len(trips) > 0:
        return TripsResponse(
            trips=trips,
            next_from_ms=trips[-1].tpep_pickup_datetime_ms,
            message=f'Success. Returned {len(trips)} trips.',
        )
    else:
        return TripsResponse(message='No trips found for the given time range.')


@app.get('/health') # endpoint that returns the health status/check (of the API) response
def health_check(): 
    return {'status': 'healthy'}

@app.get("/") # root endpoint
def root():
    return {"message": "Application is running"}

if __name__ == "__main__": # entrypoint for the application (when running locally)
    import uvicorn
    uvicorn.run(
        app, host="0.0.0.0", 
        port=8000
    )