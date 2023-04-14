from fileinput import filename
from unittest import result
from cv2 import VideoCapture,imwrite,waitKey,destroyWindow
from deepface import DeepFace
import json
import xlsxwriter
import datetime as dt
import uvicorn
from fastapi import FastAPI,Request
import pandas as pd
from csv import writer
import csv
from time import sleep
import random
import os


app = FastAPI()


def generate_name(n):
    string_set="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    filename= random.sample(string_set, int(n))
    filename="".join(filename)
    return str(filename)





def append_list_as_row(dict):     
    list_element=[]

    for v in dict.values():
        list_element.append(v)


    with open('empdata.csv', 'a') as file:
        writer_object = writer(file)
        writer_object.writerow(list_element)
  


def name_finder(filename):
    res= DeepFace.find(img_path = filename, db_path = os.path.join("database"))    
    for _,v in res.items():
        if str(v).__contains__("database"):
            str_val=str(v[0])            
            break
    

    _,name,_=str_val.split("/")
        
    return name
    

    

#taking Picture
@app.post('/emotionDetect')
async def takePicture(request:Request):

    request.headers['Content-Type'] == 'application/json'
    userinput = await request.json()
    filename= userinput.get('filepath')
    if filename is None:        
            return "{'Error': 'Please privide filepath .. filepath parameter is required'}" 
    
    if not os.path.exists(filename):
        return "{'Error': 'Path does not found'}"
    if not os.path.isfile(filename):
        return "{'Error': 'File does not found'}"


    mydict={"name":name_finder(filename)}
    captured_emotions = DeepFace.analyze(img_path = filename, actions = ['age', 'gender', 'race', 'emotion'])            
    captured_emotions=dict(captured_emotions["emotion"])
    mydict.update(captured_emotions)
    append_list_as_row(mydict)
    with open("log.txt","a") as f:
        f.write(str("Picture Taken at: "  + str(dt.datetime.now()))) 
    return "{'data':"+str(mydict)+",'status': 'File Sucessfully Processed'}"
        
  


if __name__ == '__main__':
   uvicorn.run("capture_Api:app", debug = True)


    
    





