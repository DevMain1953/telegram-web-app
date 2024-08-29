# Overview
Simple Telegram Web App

# Installation
Install venv tool for Python3:
```
sudo apt install python3-venv
```
Create and activate virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
Install all dependencies to run backend:
```
pip install -r requirements.txt
```
Install ```node.js``` and ```npm``` to run frontend, you need ```node.js 18.19.0``` => ```npm 9.2.0```:
```
sudo apt install npm
```
Then
```
cd frontend

# To install node modules
npm install

# To install TailwindCSS
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init
```
