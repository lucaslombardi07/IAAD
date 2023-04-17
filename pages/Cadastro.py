import streamlit as st
import mysql.connector as mysql
import pandas as pd
import json 

user = json.load(open("IAAD/user.txt", "r"))

mydb = mysql.connect(
    host = user['host'],
    user = user['user'],
    password = user['password'],
    database = user['database']
)