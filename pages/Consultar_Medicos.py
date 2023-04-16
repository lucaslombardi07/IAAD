import streamlit as st
import mysql.connector as mysql
import pandas as pd

mydb = mysql.connect(
    host = "localhost",
    user = "root",
    password = "30336604",
    database = "clinica_IAAD"
)

cursor = mydb.cursor()
st.write(mydb)

def p_codigo():
    cursor.execute("SELECT CodMed FROM Medico ;")
    codigos = [col[0] for col in cursor.fetchall()]
    selected_med = st.selectbox("Código", codigos)

    
    cursor.execute(f"SELECT m.NomeMed as Médico, m.CodMed as Código, c.NomeCli as Clinica, m.Genero, m.Email, e.NomeEspec as Especialidade FROM Medico as m, Especialidade as e, Clinica as c, ClinicaMedico as cm WHERE m.CodEspec = e.CodEspec and cm.CodCli = c.CodCli and cm.CodMed = m.CodMed and m.CodMed = \'{selected_med}\';")
    columns = [col[0] for col in cursor.description]
    df = pd.DataFrame(cursor.fetchall(), columns=columns)
    
    return df

def p_nome():
    cursor.execute("SELECT NomeMed FROM Medico ;")
    nomes = [col[0] for col in cursor.fetchall()]
    selected_med = st.selectbox("Nome", nomes)
    
    cursor.execute(f"SELECT m.NomeMed as Médico, m.CodMed as Código, c.NomeCli as Clinica, m.Genero, m.Email, e.NomeEspec as Especialidade FROM Medico as m, Especialidade as e, Clinica as c, ClinicaMedico as cm WHERE m.CodEspec = e.CodEspec and cm.CodCli = c.CodCli and cm.CodMed = m.CodMed and m.NomeMed = \'{selected_med}\';")
    columns = [col[0] for col in cursor.description]
    df = pd.DataFrame(cursor.fetchall(), columns=columns)
    
    return df
    
def p_clinica():
    cursor.execute("SELECT NomeCli FROM Clinica ;")
    clinicas = [col[0] for col in cursor.fetchall()]
    selected_med = st.selectbox("Clinica", clinicas)
    
    cursor.execute(f"SELECT m.NomeMed as Médico, m.CodMed as Código, c.NomeCli as Clinica, m.Genero, m.Email, e.NomeEspec as Especialidade FROM Medico as m, Especialidade as e, Clinica as c, ClinicaMedico as cm WHERE m.CodEspec = e.CodEspec and cm.CodCli = c.CodCli and cm.CodMed = m.CodMed and c.NomeCli = \'{selected_med}\';")
    columns = [col[0] for col in cursor.description]
    df = pd.DataFrame(cursor.fetchall(), columns=columns)
    
    return df

def p_especialidade():
    cursor.execute("SELECT NomeEspec FROM Especialidade ;")
    especialidades = [col[0] for col in cursor.fetchall()]
    selected_med = st.selectbox("Especialidade", especialidades)
    
    cursor.execute(f"SELECT m.NomeMed as Médico, m.CodMed as Código, c.NomeCli as Clinica, m.Genero, m.Email, e.NomeEspec as Especialidade FROM Medico as m, Especialidade as e, Clinica as c, ClinicaMedico as cm WHERE m.CodEspec = e.CodEspec and cm.CodCli = c.CodCli and cm.CodMed = m.CodMed and e.NomeEspec = \'{selected_med}\';")
    columns = [col[0] for col in cursor.description]
    df = pd.DataFrame(cursor.fetchall(), columns=columns)
    
    return df

dic = {'Código': p_codigo, 'Nome': p_nome, 'Clinica': p_clinica, 'Especialidade': p_especialidade}
s = st.radio("Buscar Medico por:", dic)

f = dic[s]

st.write(f())