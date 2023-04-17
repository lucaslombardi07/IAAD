import streamlit as st
import mysql.connector as mysql
import pandas as pd
import json 

#criar interface CRUD usando streamlit e mysql

st.header("CRUD usando streamlit e mysql")


user = json.load(open("IAAD/user.txt", "r"))

mydb = mysql.connect(
    host = user['host'],
    user = user['user'],
    password = user['password'],
    database = user['database']
)

st.write(mydb)

cursor = mydb.cursor()

cursor.execute("SELECT * FROM Paciente;")

columns = [col[0] for col in cursor.description]

df = pd.DataFrame(cursor.fetchall(), columns=columns)

st.write(df)