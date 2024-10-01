from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from PIL import Image
from io import BytesIO
import numpy as np
import onnxruntime as ort

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load ONNX model
ort_session = ort.InferenceSession('model.onnx')

@app.get("/", response_class=FileResponse)
async def read_index():
    return FileResponse("index.html")

@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    image_data = await image.read()
    image = Image.open(BytesIO(image_data))
    image = image.resize((28, 28)).convert('L')
    image.save("image.png")
    image = np.frombuffer(image.tobytes(), dtype=np.uint8)
    image = image.reshape(1, 784)
    image = image.astype(np.float32) / 255.0
    # Run inference
    ort_inputs = {ort_session.get_inputs()[0].name: image}
    ort_outs = ort_session.run(None, ort_inputs)
    predicted_digit = np.argmax(ort_outs[0])
    return {"prediction": f"{predicted_digit}"}