# data-cleaning-mysql-upload
# A mini data engineering project focusing on data cleaning using Python (Pandas) and uploading the processed data into a MySQL database.

from sqlalchemy import create_engine
import ast
import pandas as ps

A = ps.read_json(r"C:\Users\6327105\Downloads\project_2.json")
A.to_csv('rexx.csv')
print('success')
