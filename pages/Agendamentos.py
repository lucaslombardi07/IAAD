import streamlit as st
import mysql.connector as mysql
import pandas as pd
import json 

user = json.load(open("user.txt", "r"))

mydb = mysql.connect(
    host = user['host'],
    user = user['user'],
    password = user['password'],
    database = user['database']
)

cursor = mydb.cursor()
st.write(mydb)

def Agendar():
    cl1, cl2 = st.columns(2)
    
    with cl1:
        codcli = st.text_input("Código do Clinica")
    with cl2:
        codmed = st.text_input("Código do Médico")
    
    cpfp = st.text_input("CPF do Paciente")
    
    data = st.date_input("Data")
    time = st.time_input("Hora")
    
    dataTime = str(data)+" "+str(time)
    st.write(dataTime)
    b = st.button("Agendar")
    if b:
        cursor.execute(f"INSERT INTO AgendaConsulta (CodCli, CodMEd, CpfPaciente, Data_Hora) VALUES ({codcli}, {codmed}, {cpfp}, \'{dataTime}\');")
def Agendamentos():
    cursor.execute("SELECT NomeCli FROM AgendaConsulta as ac, clinica as c WHERE ac.codcli = c.codcli;")
    clinica = st.selectbox("Clinica", set([col[0] for col in cursor.fetchall()]))

    cursor.execute(f"SELECT ac.Data_Hora, m.NomeMed, p.Nomepac, ac.cpfpaciente FROM AgendaConsulta as ac, paciente as p, medico as m, clinica as c WHERE c.nomecli = \'{clinica}\' and ac.codcli = c.codcli and ac.codmed = m.codmed and ac.cpfpaciente = p.cpfpaciente;")
    columns = [col[0] for col in cursor.description]
    df = pd.DataFrame(cursor.fetchall(), columns=columns)
    st.write(df)
    return df


f = eval(st.radio("Escolha uma opção", ("Agendamentos", "Agendar")))
f()