from typing import Union

from fastapi import FastAPI

app = FastAPI()

countries = ["South Africa", "Zimbabwe"]

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/countries/{country_name}")
def get_country(country_name: str):

    return country_name in countries

@app.get("/countries/")
def get_countries():

    return countries