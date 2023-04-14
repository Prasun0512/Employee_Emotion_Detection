from unittest import result
from cv2 import VideoCapture,imwrite,waitKey,destroyWindow
from deepface import DeepFace
import json
import xlsxwriter
import datetime as dt
import pandas as pd
from csv import writer
import csv
from time import sleep
import random
import os




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
def takePicture():
    
    try:
        cam = VideoCapture(0)
        result, image = cam.read()

        
        if result:    
            
            filename=generate_name(4)
            filename=os.path.join('cap_img',filename)   
            if os.path.exists(filename+".jpg"):            
                filename=filename+generate_name(1)
            
            filename=filename+".jpg"
            imwrite(filename, image)        
            

            mydict={"name":name_finder(filename)}

            captured_emotions = DeepFace.analyze(img_path = filename, actions = ['age', 'gender', 'race', 'emotion'])
            
            captured_emotions=dict(captured_emotions["emotion"])
            mydict.update(captured_emotions)

            append_list_as_row(mydict)   
            return "Picture Taken at: "  + str(dt.datetime.now())
        else:
            return "No image detected. Please! try again"
    except Exception as e:
        with open("log.txt","a") as f:
            f.write(str(e))

flag = True
while flag:    
    data=takePicture()
    with open("log.txt","a") as f:
            f.write(str(data))
    sleep(60)

    
    



