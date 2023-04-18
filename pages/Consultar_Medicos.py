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
    selected_med = st.selectbox("Especialidade", set(especialidades))
    
    cursor.execute(f"SELECT m.NomeMed as Médico, m.CodMed as Código, c.NomeCli as Clinica, m.Genero, m.Email, e.NomeEspec as Especialidade FROM Medico as m, Especialidade as e, Clinica as c, ClinicaMedico as cm WHERE m.CodEspec = e.CodEspec and cm.CodCli = c.CodCli and cm.CodMed = m.CodMed and e.NomeEspec = \'{selected_med}\';")
    columns = [col[0] for col in cursor.description]
    df = pd.DataFrame(cursor.fetchall(), columns=columns)
    
    return df

selected = st.selectbox("Selecionar",["Todos","Filtrar","Inserir","Atualizar","Deletar"])

if selected == "Filtrar":

    dic = {'Código': p_codigo, 'Nome': p_nome, 'Clinica': p_clinica, 'Especialidade': p_especialidade}
    s = st.radio("Buscar Medico por:", dic)
    f = dic[s]
    st.write(f())

    
elif selected == "Inserir":

    st.header("Inserir médico")

    codMed = st.text_input("código do médico")
    nomeMed = st.text_input("nome do médico")
    genero = st.text_input("genero do medico")
    telefone = st.text_input("telefone do médico")
    email = st.text_input("email do médico")
    codEspec = st.text_input("código da especialidade")

    if st.button("Inseir"):

        cursor.execute(f"""INSERT INTO medico (genero, especialidade, clinica_id) 
                           VALUES ('{codMed}', '{nomeMed}','{genero}', '{telefone}, '{email}', '{codEspec}');""")
        mydb.commit()
        st.success("Médico inserido com sucesso!")

elif selected == "Deletar":

    st.header("Deletar médico")
    codMed = st.text_input("Código do médico a ser deletado")

    if st.button("Deletar"):

        cursor.execute(f"""DELETE FROM clinica_medico
                            WHERE codMed = '{codMed}""")

        cursor.execute(f"""DELETE FROM medico
                           WHERE codMed = '{codMed}';""")
        mydb.commit()
        st.success("Médico deletado com sucesso!")

elif selected == "Atualizar":

    st.header("Atualizar clínica")

    cursor.execute("SELECT codMed FROM Medico;")
    codcli = [col[0] for col in cursor.fetchall()]
    codclid = st.selectbox("Selecione o médico", codcli)

    if codclid:
        nomeMed = st.text_input("Nome da médico (deixe em branco se não deseja modificar)")
        telefone = st.text_input("Telefone do médico (deixe em branco se não deseja modificar)")
        email = st.text_input("email do médico (deixe em branco se não deseja modificar)")
        genero = st.text_input("genero do médico (deixe em branco se não deseja modificar)")
        codEspec = st.text_input("Especialidade do médico (deixe em branco se não deseja mudar)")

        cursor.execute(f"SELECT * FROM Clinica WHERE codcli = '{codclid}';")
        columns = [col[0] for col in cursor.description]
        df = pd.DataFrame(cursor.fetchall(), columns=columns)
        if nomeMed == "":
            nome = df['NomeCli'][0]
        if genero == "":
            genero = df['Genero'][0]
        if telefone == "":
            telefone = df['Telefone'][0]
        if email == "":
            email = df['Email'][0]

    if st.button("Atualizar"):

        cursor.execute(f"""UPDATE medico
                           SET nomeMed = '{nomeMed}', genero = '{genero}', telefone = '{telefone}',email = '{email}', codEspec = '{codEspec}'
                           WHERE codMed = '{codclid}';""")
        mydb.commit()
        st.success("Médico atualizado com sucesso!")

else: 
    cursor.execute("SELECT * from Medico;")

    columns = [col[0] for col in cursor.description]
    df = pd.DataFrame(cursor.fetchall(), columns=columns)

    st.header("Informações dos médicos")
    st.write("Aqui constam os dados de todos os médicos de todas as clínicas.")
    st.write(df)
    