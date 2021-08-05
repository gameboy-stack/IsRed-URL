from flask import Flask,render_template,request,redirect
import requests as req
from urllib.parse import urlparse
from requests.utils import requote_uri
from form import UrlInput
from datetime import datetime
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env_sample')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("secret_key")

app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route("/",methods=["GET"])
def home():
    formvar = UrlInput()
    return render_template("home.html",year=datetime.today().year,form=formvar)

async def tracingfunc(givenURL):
    formvar = UrlInput()
    headers ={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
        }
    try:
        response =  req.get(str(givenURL),headers=headers)
        if response.history:
            responseHistory = [[str(i.url),str(i.status_code)] for i in response.history] + [[str(response.url),str(response.status_code)]] 
        elif(not response.history):
            responseHistory = [[str(response.url),str(response.status_code)]]
    except:
        pass
    finally:
        responseHistory =[[str(givenURL),"None"]]
    return responseHistory

@app.route("/trace/",methods=["POST","GET"])
async def trace():
    formvar=UrlInput()
    if request.method == "POST": 
        givenURL = formvar.Urlinp.data 
        parsedUrl = urlparse(givenURL)
        if (not len(parsedUrl[0])):
            givenURL = "http://" + str(givenURL)
        encodedURL = requote_uri(str(givenURL))
        responseHistory = await tracingfunc(encodedURL)
        dictres = {str(i):urldetails for i,urldetails in enumerate(responseHistory)} 
        return render_template("home.html",form=formvar ,year=datetime.today().year,tracedurls=dictres,encurl=encodedURL)  
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
