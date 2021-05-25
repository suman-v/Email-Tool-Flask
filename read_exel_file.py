

from datetime import datetime
import pandas as pd
import glob

def read_excel_sheets(excel_file_path):
        filename =  excel_file_path# use your folder path to read excel files
        li = []
        try:
            
                for i in range(0,5): # reading multiple sheets from one excel file
                    print (filename)
                    try:
                        
                        print (filename)
                        df = pd.read_excel(filename, index_col=None, header=0, sheet_name=i) #read excel file
                        
                        print (df.columns)
                        df = df[['Company', 'Contact Name',  'Email','Designation']]
                        
                        print ("Reading data")
                        last = df['Contact Name'].str.split(" ")
        
                        first_name= [i[0] for i in last]
                        last_name= [i[-1] for i in last]
                            
                        df['First Name'] = first_name
                        df['Last Name'] = last_name
                        print("created last namd and first name columns")
                        df= df.dropna() #dropping Nan values
                      

                        print ("Excel file name:",filename) 
                        print ("Sheet No:",i)
                        print ("Size of data:",df.shape)
                      
                        li.append(df) #append data from first sheet in list
              
                        print (len(li))
                        print ("*"*80)
                    except:
                        
                        print ("No sheet")
                
        except:
            
            print ("ERROR IN", filename)
            
        data = pd.DataFrame()
        
        try:
            #concat all files data in one dataframe
            data = pd.concat(li, axis=0, ignore_index=True)
            
            #creating last and first name column using contac_name
            last = data['Contact Name'].str.split(" ")
            
            first_name= [i[0] for i in last]
            last_name= [i[-1] for i in last]
            
            data['First Name'] = first_name
            data['Last Name'] = last_name
                
            data = data[['Company', 'First Name', 'Contact Name', 'Last Name', 'Email', 'Designation']] 
    
        except:
            data = pd.DataFrame()
            data = pd.read_excel(filename, index_col=None, header=0)
            print ("data issue")
       
            
       
        
            
        # make upper case to  lower case
        data['First Name'] = data['First Name'].str.lower()
       
        data['Last Name']= data['Last Name'].str.lower()
       
        data['Company']= data['Company'].str.lower()
     
        data['Email']= data['Email'].str.lower()
     
        data['Designation'] = data['Designation'].str.lower()
                                                  
        print ("converted upper case to lower case")   
        return data #return excel data in dataframe
    
# filename = r"E:\extraction_test.xlsx"
    
# df = pd.read_excel(filename, index_col=None, header=0) #read excel file

# print (df.columns)
# df = df[['Company', 'Contact Name',  'Email','Designation']]

# print ("Reading data")
# last = df['Contact Name'].str.split(" ")

# first_name= [i[0] for i in last]
# last_name= [i[-1] for i in last]

# df['First Name'] = first_name
# df['Last Name'] = last_name
