# -*- coding: utf-8 -*-
"""
Created on Mon May  3 00:08:53 2021

@author: User
"""



from flask import Flask, render_template, request,  redirect,url_for
from datetime import date
import sys,os
# from database_training_test import database_test
from datetime import datetime
from read_Excel_file import read_excel_file, read_excel_file_input_file
from generate_Email import generate_email

import pandas as pd
app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

# File extension
file_extension = ['csv']


database_path = r'E:\Data Files'
output = 'E:\Email_tool\output'


import pickle

def load_obj(name ):
  with open( name + '.pkl', 'rb') as f:
      return pickle.load(f)


@app.route('/', methods=['GET', 'POST'])
def login():
    print ("step 1")
    error = None
    
    if request.method == 'POST':
        print ("step 2")
        
        
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            print ("error")
            error = 'Invalid Credentials. Please try again.'
        else:
            print ("step else")
            return redirect(url_for('home'))
    return render_template('login.html', error=error)



@app.route('/', methods=['GET', 'POST'])
def contact():
    error = None
    if request.method == 'POST':
        if request.form['submit_button'] == 'Do Something':
            print ("LL")
        elif request.form['submit_button'] == 'Do Something Else':
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('contact.html',error=error)





@app.route('/home', methods=['GET', 'POST'])
def home():
    import time

    start = time.time()
    print ("step 4")
    if request.method == 'POST':
        # if request.form['fi1le-1']
            # get the uploaded file
            
            select_database_path = r"E:\Email_tool\Data Files\test"
            
            # name = request.form['submit_button'] == database_test(select_database_path)
            
            uploaded_file2 = request.files['file-2']
            
            file_name= uploaded_file2.filename
            print ("File_name: ",uploaded_file2.filename)
            

            import pathlib
            print (pathlib.Path(__file__).parent.absolute())
                           
            if uploaded_file2.filename != '':
                if uploaded_file2.filename.split('.')[1] == 'xlsx':
 
                    """
                    Your Logic with 2 files

                   """
                          
                    input_data = read_excel_file_input_file(uploaded_file2)
                    # input_data = pd.read_excel(uploaded_file2, index_col=None, header=0)
                    print ("data", input_data.head())
                    input_data = generate_email(input_data )
                    try:
                        del input_data["temp"]
                    except:
                        print ("temp column not present")
                    
          
                    import datetime as dt

                    today = dt.datetime.today().strftime('%Y-%m-%d %H-%M-%S')
                    
                    # datetime object containing current date and time
                    now = datetime.now()
                    s = str(now).split(".")
                   
                    
                    missing_data = input_data[input_data['email'] == "NA"]
                    missing_data.to_csv(f"{output}\{file_name[:15]}_Missing_file{today}.csv" , index = False)
                    status = f"{missing_data.shape[0]} Missing Email Found"

                    input_data = input_data[input_data['email'] != "NA"]
                    
                    
                    name  = f"output_file_{str(s[0])}"
                    
                    
                    print (name+".csv")
                   
                    input_data.to_csv(f"{output}\{file_name[:15]}_Output_file{today}.csv" , index = False)
                 
                    end = time.time()
                    print(f"Runtime of the program is {end - start}")
                  
                    files_path = [os.path.abspath(x) for x in os.listdir()]
                    print(files_path)               
                    
               
                    cwd = os.getcwd()                
                    print (cwd)

            
                    return render_template('home.html', output=files_path, as_attachment=True, file_name =status, file_path = status)
                
                else:
                    context = {
                        "error" : "Upload only CSV files!"   # If you want to pass anything to FrontEnd
                    }
                    return render_template('error.html', context=context)  # Check error.html for any changes
       
    return render_template('home.html')


if __name__ == "__main__":
  app.run()
  
  #11.58 - 12.28