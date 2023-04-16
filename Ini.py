import streamlit as st
import mysql.connector as mysql
import pandas as pd

#criar interface CRUD usando streamlit e mysql

st.header("CRUD usando streamlit e mysql")

mydb = mysql.connect(
    host = "localhost",
    user = "root",
    password = "30336604",
    database = "clinica_IAAD"
)

st.write(mydb)

cursor = mydb.cursor()

cursor.execute("SELECT * FROM Paciente;")

columns = [col[0] for col in cursor.description]

df = pd.DataFrame(cursor.fetchall(), columns=columns)

st.write(df)