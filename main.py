from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Name": "Sumon Roy",
            "Student id": "200922",
            "HomeSubDistrict" : "Dakop"}


         