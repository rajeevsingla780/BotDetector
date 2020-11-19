from flask import Flask, Response,render_template,redirect,request,url_for
import cv2
import time
import random
import os
import main
from top1 import Camera 
app = Flask(__name__)

n=1
@app.route('/')
@app.route('/',methods=['GET', 'POST'])
def api():
   global system
   if request.method=="POST":
          a=request.form.get('First')
          print(a)
          main.fun("NOW YOU WILL LISTEN A FOUR DIGIT NUMBER .YOU HAVE TO GESTURE ACCORDINGLY TO SHOW YOUR IDENTITY u will get only 7 sec for a particular number")
         
          list1=[0,0,0,0]
          for i in range(0,4):
              num=random.randint(0,4)
              main.fun(num)
              
              list1[i]=num
          print(list1)    
          main.fun("Show the First Number ")
          s=Camera(list1)
          if s==False:
                 main.fun("Wrong Capatcha ")
                 return (render_template('aa.html'))
          else:
                 main.fun("Form Submitted ")
                 
   return (render_template('aa.html'))
           
if __name__ == "__main__":
    app.run()
