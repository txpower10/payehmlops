# from fastapi import FastAPI
# from pydantic import BaseModel
# from transformers import AutoTokenizer, AutoModelWithLMHead

# # Initialize FastAPI app
# app = FastAPI()

# # Load the Hugging Face tokenizer and model
# tokenizer = AutoTokenizer.from_pretrained("model")
# model = AutoModelWithLMHead.from_pretrained("model")

# # Request schema
# class PredictRequest(BaseModel):
#     text: str

# @app.get("/")
# def health_check():
#     return {"status": "Model is running"}

# @app.post("/predict")
# def predict(request: PredictRequest):
#     try:
#         # Process input text and make a prediction
#         input_ids = tokenizer.encode(request.text + '</s>', return_tensors='pt')
#         output = model.generate(input_ids=input_ids, max_length=2)
#         prediction = tokenizer.decode(output[0])
#         return {"prediction": prediction.strip()}
#     except Exception as e:
#         return {"error": str(e)}



from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelWithLMHead

# Initialize FastAPI app
app = FastAPI()

# Initialize Prometheus Instrumentator
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

# Load the Hugging Face tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("model")
model = AutoModelWithLMHead.from_pretrained("model")

# Request schema
class PredictRequest(BaseModel):
    text: str

@app.get("/")
def health_check():
    return {"status": "Model is running"}

@app.post("/predict")
def predict(request: PredictRequest):
    try:
        # Process input text and make a prediction
        input_ids = tokenizer.encode(request.text + '</s>', return_tensors='pt')
        output = model.generate(input_ids=input_ids, max_length=2)
        prediction = tokenizer.decode(output[0])
        return {"prediction": prediction.strip()}
    except Exception as e:
        return {"error": str(e)}

