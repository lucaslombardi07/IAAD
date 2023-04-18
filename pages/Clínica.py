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

cursor = mydb.cursor()

# Mostrando todas as clínicas do banco de dados
selection = st.selectbox("Selecione a operação para ser feita nas clínicas", ["Mostrar todas", "Inserir", "Inserir Médico", "Atualizar", "Deletar"])

if selection == "Inserir":
    st.header("Inserir nova clínica")
    codclid = st.text_input("Código da clínica")
    nome = st.text_input("Nome da clínica")
    endereco = st.text_input("Endereço da clínica")
    telefone = st.text_input("Telefone da clínica")
    email = st.text_input("Email da clínica")
    if st.button("Inserir"):
        cursor.execute(f"INSERT INTO Clinica (codcli, nomecli, endereco, telefone, email) VALUES ('{codclid}', '{nome}', '{endereco}', '{telefone}', '{email}');")
        mydb.commit()
        st.success("Clínica inserida com sucesso!")
elif selection == "Atualizar":
    st.header("Atualizar clínica")
    cursor.execute("SELECT codcli FROM Clinica;")
    codcli = [col[0] for col in cursor.fetchall()]
    codclid = st.selectbox("Selecione a clínica", codcli)
    if codclid:
        nome = st.text_input("Nome da clínica (deixe em branco se não deseja modificar)")
        endereco = st.text_input("Endereço da clínica (deixe em branco se não deseja modificar)")
        telefone = st.text_input("Telefone da clínica (deixe em branco se não deseja modificar)")
        email = st.text_input("Email da clínica (deixe em branco se não deseja modificar)")

        cursor.execute(f"SELECT * FROM Clinica WHERE codcli = '{codclid}';")
        columns = [col[0] for col in cursor.description]
        df = pd.DataFrame(cursor.fetchall(), columns=columns)
        if nome == "":
            nome = df['NomeCli'][0]
        if endereco == "":
            endereco = df['Endereco'][0]
        if telefone == "":
            telefone = df['Telefone'][0]
        if email == "":
            email = df['Email'][0]

        if st.button("Atualizar"):
            cursor.execute(f"UPDATE Clinica SET nomecli = '{nome}', endereco = '{endereco}', telefone = '{telefone}', email = '{email}' WHERE codcli = '{codclid}';")
            mydb.commit()
            st.success("Clínica atualizada com sucesso!")
elif selection == "Deletar":
    st.header("Deletar clínica")
    cursor.execute("SELECT codcli FROM Clinica;")
    codcli = [col[0] for col in cursor.fetchall()]
    codclid = st.selectbox("Selecione a clínica", codcli)
    if codclid:
        if st.button("Deletar"):
            cursor.execute(f"DELETE FROM ClinicaMedico WHERE codcli = '{codclid}';")
            cursor.execute(f"DELETE FROM Clinica WHERE codcli = '{codclid}';")
            mydb.commit()
            st.success("Clínica deletada com sucesso!")
elif selection == "Inserir Médico":
    st.header("Inserir médico em clínica")
    cursor.execute("SELECT codcli FROM Clinica;")
    codcli = [col[0] for col in cursor.fetchall()]
    codclid = st.selectbox("Selecione a clínica", codcli)
    if codclid:
        cursor.execute("SELECT codmed FROM Medico;")
        codmed = [col[0] for col in cursor.fetchall()]
        codmedd = st.selectbox("Selecione o médico", codmed)
        if codmedd:
            if st.button("Inserir"):
                cursor.execute(f"INSERT INTO ClinicaMedico (codcli, codmed) VALUES ('{codclid}', '{codmedd}');")
                mydb.commit()
                st.success("Médico inserido na clínica com sucesso!")
else:
    st.header("Todas as clínicas")
    cursor.execute("SELECT * FROM Clinica;")
    columns = [col[0] for col in cursor.description]
    df = pd.DataFrame(cursor.fetchall(), columns=columns)
    st.write(df)