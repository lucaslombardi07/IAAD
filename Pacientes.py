import streamlit as st
import mysql.connector as mysql
import pandas as pd
import json 

#criar interface CRUD usando streamlit e mysql

st.header("Sistema Clínicas")
st.subheader("Pacientes")

user = json.load(open("IAAD/user.txt", "r"))

mydb = mysql.connect(
    host = user['host'],
    user = user['user'],
    password = user['password'],
    database = user['database']
)

cursor = mydb.cursor()

selection = st.selectbox("Selecione a operação para ser feita nos pacientes", ["Mostrar todos", "Inserir", "Atualizar", "Deletar"])

if selection == "Inserir":
    st.header("Inserir novo paciente")
    cpfpaciente = st.text_input("CPF do paciente")
    nome = st.text_input("Nome do paciente")
    genero = st.selectbox("Gênero do paciente", ["M", "F"])
    datanascimento = st.date_input("Data de nascimento do paciente")
    telefone = st.text_input("Telefone do paciente")
    email = st.text_input("Email do paciente")
    if st.button("Inserir"):
        cursor.execute(f"INSERT INTO Paciente (cpfpaciente, nomepac, datanascimento, telefone, email) VALUES ('{cpfpaciente}', '{nome}', '{datanascimento}', '{telefone}', '{email}');")
        mydb.commit()
        st.success("Paciente inserido com sucesso!")

elif selection == "Atualizar":
    st.header("Atualizar paciente")
    cursor.execute("SELECT cpfpaciente FROM Paciente;")
    cpfpaciente = [col[0] for col in cursor.fetchall()]
    cpfpaciente = st.selectbox("Selecione o paciente", cpfpaciente)
    if cpfpaciente:
        nome = st.text_input("Nome do paciente (deixe em branco se não deseja modificar)")
        datanascimento = st.date_input("Data de nascimento do paciente (deixe em branco se não deseja modificar)")
        genero = st.selectbox("Gênero do paciente (deixe em branco se não deseja modificar)", ["", "M", "F"])
        telefone = st.text_input("Telefone do paciente (deixe em branco se não deseja modificar)")
        email = st.text_input("Email do paciente (deixe em branco se não deseja modificar)")

        cursor.execute(f"SELECT * FROM Paciente WHERE cpfpaciente = '{cpfpaciente}';")
        columns = [col[0] for col in cursor.description]
        df = pd.DataFrame(cursor.fetchall(), columns=columns)
        if nome == "":
            nome = df['NomePac'][0]
        if datanascimento == "":
            datanascimento = df['DataNascimento'][0]
        if genero == "":
            genero = df['Genero'][0]
        if telefone == "":
            telefone = df['Telefone'][0]
        if email == "":
            email = df['Email'][0]

        if st.button("Atualizar"):
            cursor.execute(f"UPDATE Paciente SET nomepac = '{nome}', datanascimento = '{datanascimento}', genero = '{genero}', telefone = '{telefone}', email = '{email}' WHERE cpfpaciente = '{cpfpaciente}';")
            mydb.commit()
            st.success("Paciente atualizado com sucesso!")
elif selection == "Deletar":
    st.header("Deletar paciente")
    cursor.execute("SELECT cpfpaciente FROM Paciente;")
    cpfpaciente = [col[0] for col in cursor.fetchall()]
    cpfpaciente = st.selectbox("Selecione o paciente", cpfpaciente)
    if cpfpaciente:
        if st.button("Deletar"):
            # deletar também da tabela de consultas
            cursor.execute(f"DELETE FROM AgendaConsulta WHERE cpfpaciente = '{cpfpaciente}';")
            cursor.execute(f"DELETE FROM Paciente WHERE cpfpaciente = '{cpfpaciente}';")
            mydb.commit()
            st.success("Paciente deletado com sucesso!")
else:
    st.header("Mostrar todos os pacientes")
    cursor.execute("SELECT * FROM Paciente;")
    columns = [col[0] for col in cursor.description]
    df = pd.DataFrame(cursor.fetchall(), columns=columns)
    st.write(df)