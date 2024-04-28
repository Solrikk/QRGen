from fastapi import FastAPI, HTTPException, Form, File, UploadFile
from fastapi.responses import StreamingResponse, HTMLResponse
import qrcode
from io import BytesIO
from PIL import Image
import requests
from fastapi.encoders import jsonable_encoder

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def form():
    return """
    <html>
        <head>
            <title>QRGen</title>
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
                input[type=text], input[type=file] {
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
            <h1>QRGen</h1>
            <form action="/qr/" method="post" enctype="multipart/form-data">
                <input type="text" name="data" placeholder="Enter text or link here"/>
                <input type="file" name="file" accept="image/*"/>
                <input type="submit"/>
            </form>
        </body>
    </html>
    """


@app.post("/qr/")
async def create_qr(data: str = Form(None), file: UploadFile = File(None)):
    if not data and not file:
        raise HTTPException(status_code=400, detail="Data parameter or file is required")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    if file:
        try:
            image_contents = await file.read()
            image = Image.open(BytesIO(image_contents))
            output = BytesIO()
            image.save(output, format='PNG')
            img_data = output.getvalue()
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid image file: {e}")
        qr.add_data(data)
    else:
        qr.add_data(data)

    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_bytes = BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    return StreamingResponse(img_bytes, media_type="image/png")
