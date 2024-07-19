import streamlit as lgn

def login (usuario, senha):
    loginCerto = "Ellen"
    senhaCerta = "12112007"
    return usuario == loginCerto and senha == senhaCerta
lgn.title('Pagina de login')

with lgn.form(key= 'login_form'):
    usuario = lgn.text_input('Nome de usuario:')
    senha = lgn.text_input('Digite sua senha:')
    botao = lgn.form_submit_button(label='Entrar')


if botao:
    if login(usuario, senha):
        lgn.sucess('login bem sucedido')
        lgn.write('Bem vido')
    else:
        lgn.error('Nome do usuario e senha incorretos.')

    


