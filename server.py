# -*- coding: utf-8 -*-
import os
from flask import Flask, request 
import json

UPLOAD_FILE_PATH = '/home/shared/upload/'
app = Flask(__name__)

@app.route('/api/python', methods=['POST'])
def upload():
    file_name = request.form['file_name']
    file_path = request.form['file_path']
    # save file
    while os.path.exists(UPLOAD_FILE_PATH+file_name):
        file_name = "1_"+file_name
        if not os.path.exists(UPLOAD_FILE_PATH+file_name):
            break
    os.system("mv "+file_path+" "+UPLOAD_FILE_PATH+file_name)
    return "http://10.41.12.246/upload/"+file_name

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=9528)