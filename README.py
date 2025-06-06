# data-cleaning-mysql-upload
# A mini data engineering project focusing on data cleaning using Python (Pandas) and uploading the processed data into a MySQL database.

from sqlalchemy import create_engine
import ast
import pandas as ps

A = ps.read_json(r"C:\Users\6327105\Downloads\project_2.json")
A.to_csv('rexx.csv')
print('success')

#########################################################################

from sqlalchemy import create_engine
import ast
import pandas as ps

# This will help us to change the Json to csv file so it will be easy for us to clean the data and to upload in the sql

A = ps.read_csv(r"C:\Bosco\Study\Don SQL\rexx.csv",header=None,names=['AA','BB']) #we read the file and name the column as 'AA','BB'
A = A.dropna(subset=['BB'])    #This will drop the null value from A

def B(x):
    try:                            #try and except to avoid the errors
        return ast.literal_eval(x)  #convert the strings into python objects
    except (ValueError,SyntaxError): #if value and syntax error return none
        return None
A['CC']=A['BB'].apply(B)             #and we applying the values into A['CC']
A = A.dropna(subset=['CC'])          #Again we drop the null values in A['CC']

normal= ps.json_normalize(A['CC'])    #Normalizing the json file 

def C(y):
    if isinstance(y,str) and ':' in y: #checking the string values and sperate it by ":"
        return y.split(':')[-1]         #and returning the last values using [-1]
    else:
        return y                        #else only y

normal = normal.applymap(C)             #applying it to normal variable

D = ps.concat([A['AA'],normal],axis=1)  

engine = create_engine('mysql+mysqlconnector://root<password>localhost/dummy_1')  #hide the password using '####' for privacy

D.to_sql('Rexx',con=engine,if_exists='replace',index=False)         #and upload the clean file to sql

print('sucessfuly update')

#################################################################

#Write a function to check if a number is prime
import pandas as ps
import plotly.express as ex
import ast
from sqlalchemy import create_engine as cg 
import seaborn as se
import matplotlib.pyplot as py
import numpy as nm

A = ps.read_csv(r'C:\Bosco\Study\Don SQL\project.csv')  #read the csv from the path

A['OrderID'] = A['OrderID'].astype(int)                  #scling each columns
A['Date'] = ps.to_datetime(A['Date'])                    #scling each columns
A['Customer'] = A['Customer'].astype(str)                #scling each columns
A['Product'] = A['Product'].astype(str)                    #scling each columns
A['Quantity'] = A['Quantity'].astype(int)                #scling each columns
A['Price'] = A['Price'].astype(float)                    #scling each columns
A['Region'] = A['Region'].astype(str)                    #scling each columns
A['TotalPrice'] = A['Quantity'] * A['Price']               #scling each columns

engine = cg('mysql+mysqlconnector://root:<password>@localhost/dummy_1')         

query = '''
select Customer, count(Customer) from project group by Customer order by Customer desc
'''
df = ps.read_sql(query,con=engine)

print(df)

################################################################

#Write a function to check if a number is prime
import pandas as ps
import plotly.express as ex
from sqlalchemy import create_engine as cg 
import seaborn as se
import matplotlib.pyplot as py
import numpy as nm
from plotly.subplots import make_subplots as ms

A = ps.read_csv(r'C:\Bosco\Study\Don SQL\project.csv')

A['OrderID'] = A['OrderID'].astype(int)
A['Date'] = ps.to_datetime(A['Date'])
A['Customer'] = A['Customer'].astype(str)
A['Product'] = A['Product'].astype(str)
A['Quantity'] = A['Quantity'].astype(int)
A['Price'] = A['Price'].astype(float)
A['Region'] = A['Region'].astype(str)
A['TotalPrice'] = A['Quantity'] * A['Price']

engine = cg('mysql+mysqlconnector://root:<password>@localhost/dummy_1')

query = '''
select Customer, count(Customer) from project group by Customer order by Customer desc
'''
df = ps.read_sql(query,con=engine)
B = ex.bar(A,x=A['TotalPrice'],y=A['Region'])
C = ex.line(A,x=A['Date'],y=A['Quantity'])
D = ex.pie(A,names=A['Region'],values=A['Quantity'])
B.show()
C.show()
D.show()

print('super ')
