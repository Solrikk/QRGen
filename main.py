from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import StreamingResponse, HTMLResponse
import qrcode
from io import BytesIO

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
                input[type=text] {
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
            <h1>QR Code Generator</h1>
            <form action="/qr/" method="post">
                <input type="text" name="data" placeholder="Enter text or link here"/>
                <input type="submit"/>
            </form>
        </body>
    </html>
    """


@app.post("/qr/")
def create_qr(data: str = Form(...)):
  if not data:
    raise HTTPException(status_code=400, detail="Data parameter is required")

  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=4,
  )
  qr.add_data(data)
  qr.make(fit=True)
  img = qr.make_image(fill_color="black", back_color="white")
  img_bytes = BytesIO()
  img.save(img_bytes, format="PNG")
  img_bytes.seek(0)

  return StreamingResponse(img_bytes, media_type="image/png")
