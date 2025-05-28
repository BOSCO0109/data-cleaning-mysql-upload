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

engine = create_engine('mysql+mysqlconnector://root:###@###@localhost/dummy_1')  #hide the password using '####' for privacy

D.to_sql('Rexx',con=engine,if_exists='replace',index=False)         #and upload the clean file to sql

print('sucessfuly update')
