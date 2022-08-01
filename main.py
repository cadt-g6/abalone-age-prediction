from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from libs.services.abalone import AbaloneModelService


app = FastAPI(title="Abalone Model Service", description="Abalone Model Service")
service = AbaloneModelService()

# Allow cors for all origins
@app.middleware("http")
async def allow_cors(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response


@app.post("/predict-age", response_model=dict)
async def predict_age(body: dict):
    # Validate request body
    if not body:
        return {"error": "Request body is empty"}
    if not body.get("Sex"):
        return {"error": "Sex is required"}
    if not body.get("Length"):
        return {"error": "Length is required"}
    if not body.get("Diameter"):
        return {"error": "Length is required"}
    if not body.get("Height"):
        return {"error": "Height is required"}
    if not body.get("Whole weight"):
        return {"error": "Whole weight is required"}
    if not body.get("Shucked weight"):
        return {"error": "Shucked weight is required"}
    if not body.get("Viscera weight"):
        return {"error": "Viscera weight is required"}
    if not body.get("Shell weight"):
        return {"error": "Shell weight is required"}

    # Predict age
    age = service.predict(body)

    return {"age": age}


app.mount("/", StaticFiles(directory="client/build", html=True), name="client")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)
