<div align="center">
  <img src="https://github.com/Solrikk/QRGen/blob/main/assets/QRGen.png" width="30%"/>
</div>

<div align="center">
  <h3> <a href="https://github.com/Solrikk/QRGen/blob/main/README.md"> English | <a href="https://github.com/Solrikk/QRGen/blob/main/README_RU.md">Русский</a> | <a href="https://github.com/Solrikk/QRGen/blob/main/README_GE.md"> Deutsch </a> | <a href="https://github.com/Solrikk/QRGen/blob/main/README_JP.md"> 日本語 </a> | <a href="README_KR.md">한국어</a> | <a href="README_CN.md">中文</a> </h3>
</div>

-----------------

# QRGen ⚡️

_**QRGen**_ это веб-приложение на базе FastAPI, предназначенное для генерации QR-кодов из любых текстовых данных, включая ссылки, которые пользователи могут легко сканировать с помощью мобильных устройств. Он предлагает простое, но мощное решение для генерации QR-кодов "на лету".

**Features:**
- _**Простота использования:**_ - QRGen предлагает простой веб-интерфейс, что делает процесс генерации QR-кодов быстрым и беспроблемным.
- _**Гибкость:**_ - Генерирация QR-кодов для любых данных - текста, URL-адресов, идентификаторов продуктов и многого другого.
- _**Customization:**_ The application provides options to customize the QR code parameters, including error correction level, size, and borders.

**Technologies:**
This application is developed with the following technologies:
- FastAPI: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- QRCode: A library for generating QR codes in Python.
- HTML/CSS: Fundamentals of web design for crafting the user interface.

Getting Started
To get QRGen running locally, you'll need Python 3.7+ and the installed dependencies. Follow these steps:
1. Clone the repository:
``git clone your_repository_url``
2. Install dependencies:
``pip install fastapi uvicorn qrcode[pil]``
3. Launch the development server:
``uvicorn main:app --reload``

After starting the server, navigate to http://127.0.0.1:8000 in your browser to start using the application.

