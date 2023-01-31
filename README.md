# EduNext Test
## Hello!
I'm Alvaro8317, I created this code to present a technical test for EduNext (January, 2023), this code is going to call the micro service of EduNext, extract the data and store this data into a python list to manage this data, using only the method PATCH
## Getting Started
Easy! Are you in **Windows**? Use these commands: 
```bash
python -m venv env
.\env\Scripts\activate.bat
pip install -r requirements.txt
uvicorn main:app --reload --port 8011
```
Or maybe... Are you in **Linux** or WSL? You can these commands:
```bash
python3 -m venv env
source .\env\bin\activate
pip3 install -r requirements.txt
uvicorn main:app --reload --port 8011
```
If the port gives you any issue, you can change it from the command! Now, please open a ***browser***, go to the next URL: `http://127.0.0.1:8012/docs` and play with the **API**!

Created by Alvaro Garzón <eduardo831_@hotmail.com>, 31 January, 2023