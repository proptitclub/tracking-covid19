from flask import Flask, jsonify, render_template, request
from flask import Response
import os
import logging
logging.basicConfig(format='%(asctime)s\t%(levelname)s\t%(message)s', level=logging.DEBUG)
import config
import requests
import json
from datetime import datetime
from api_covid import API

# Flask
template_dir = os.path.abspath('views')
app = Flask(__name__, template_folder=template_dir)

@app.route("/", methods=["GET"])
def index():
    data = API()
    now = datetime.now()
 
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    time = time[:-3] + ":00"
    return render_template("index.html", all_min=data.all_min, vn=data.vietnam,
                            all_max=data.all_max, result=data.result, time=time)

if __name__ == "__main__":
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT, debug=True)
    