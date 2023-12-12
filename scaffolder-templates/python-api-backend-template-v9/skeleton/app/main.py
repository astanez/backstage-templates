from typing import Union
from fastapi import FastAPI

import math

app = FastAPI()

# Basic example of a REST call without parameters
@app.get("/")
async def root():
    return {'example': 'This is an example', 'data': 0}

# Echo example
@app.get("/echo/")
async def echo(text: str):
    return {'echo': text}

# Haversine formula example in Python
def distance(origin, destination):
    return 0

# REST API call for geo distance
@app.get("/distance/")
async def get_distance(lat1: float = 0.0, long1: float = 0.0,
                       lat2:float = 0.0 , long2: float = 0.0):
    d = distance((lat1, long1), (lat2, long2))
    return{'distance':  d}

