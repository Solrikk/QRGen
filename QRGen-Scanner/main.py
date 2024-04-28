from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import HTMLResponse
import io
from PIL import Image
from pyzbar.pyzbar import decode
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def form():
  return """
    <html>
        <head>
            <title>QRCodeScanner</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; padding-top: 50px; }
                h1 { color: #333; }
                form {
                    margin: 20px auto;
                    padding: 20px;
                    border: 1px solid #ccc;
                    display: inline-block;
                    border-radius: 10px;
                }
                input[type=file] {
                    padding: 10px;
                    margin: 10px 0;
                    width: 300px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                input[type=submit] {
                    padding: 10px 20px;
                    background-color: #007bff;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                input[type=submit]:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <h1>QRCodeScanner</h1>
            <form action="/scan/" method="post" enctype="multipart/form-data">
                <input type="file" name="file" accept="image/*"/>
                <input type="submit"/>
            </form>
        </body>
    </html>
    """

@app.post("/scan/")
async def scan_qr(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400,
                            detail="No file uploaded")

    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    decoded_objects = decode(image)
    if not decoded_objects:
        raise HTTPException(status_code=404,
                            detail="No QR Code found")

    decoded_contents = [obj.data.decode("utf-8") for obj in decoded_objects]
    return jsonable_encoder({"decoded_contents": decoded_contents})