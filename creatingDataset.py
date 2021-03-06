import pandas as pd
from sqlalchemy import create_engine,MetaData,  Table, Column, Integer, String, DateTime

#this program create a database with the 'csvHeader' file.

#csv file with the column names
path = 'dataset_speedtest/csvHeader.csv'

#reading the csv and transforming it into a data frame, ignoring the last column with the iloc function.
df = pd.read_csv(path).iloc[:,1:]

#creating a function to clean the string of the column names
def clean(s):
    s = s.replace(' ','_')
    s = s.replace('\n','')
    return s

#using a List comprehension to apply the function to clean the column names and ignore the columns with the IP address
lst = [clean(x) for x in df.columns if 'IP' not in x]

#collecting the items in the list and storing them in variables to use in the SQL command
Server_ID =lst[0]
Sponsor=lst[1]
Server_Name=lst[2]
Timestamp=lst[3]
Distance=lst[4]
Ping=lst[5]
Download=lst[6]
Upload=lst[7]
Share=lst[8]

#creating an engine to connect to the database
engine = create_engine("sqlite:///dataset_speedtest/main.db")
connection = engine.connect()

#creating a table using SQL
stmt = f"""CREATE TABLE speedtest(
                {Sponsor}  VARCHAR(50),
                {Server_Name}  VARCHAR(50),
                {Timestamp} DATETIME,
                {Distance} DECIMAL,
                {Ping} TEXT,
                {Download} DECIMAL,
                {Upload} DECIMAL
                );"""

#executing the SQL command above
results = connection.execute(stmt)             
