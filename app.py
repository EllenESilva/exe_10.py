import streamlit as st

st.title("Titulo da pagina")
st.header("Cabeçalho")
st.subheader("ub cabeçalho")
st.text("texto simples")

st.markdown("titulo markdown")

valor = st.slider("Selecione um valor", 0,100,50)
st.write("Valor selecionado", valor)

if st.button("Clique aqui"):
    st.write("Botão clicado!")

nome = st.text_input('Digite seu nome')
st.write('nome:', nome)

opcao = st.selectbox('Escolha uma opção: ', ['opcao 1','opcao 2','opcao3'])
st.write('Opção escolhida: ', opcao)

opcoes = st.multiselect('Escolha multiplas opções: ' ,['opcao 1', 'opcao 2', 'opcao 3'])
st.write('Opções escolhidas: ',opcoes)

arquivo = st.file_uploader('Escolha um arquivo')
if arquivo is not None:
    st.write('Arquivo carregado: ',arquivo.name)

    if st.checkbox('mostrar texto'):
        st.write('texto mostrado!')

genero = st.radio('escolha seu gênero: ', ['masculino', 'feminino', 'outro'])
st.write('gênero; ', genero)

import matplotlib.pyplot as pit

fig, ax = pit.subplots()
ax.plot([1,2,3,4],[10,20,30,40])
st.pyplot(fig)

#dividindo em duas colunas
col1 , col2 = st.columns(2)
col1.write('coluna 01')
col2.write('coluna 02')
#barras laterais
st.sidebar.title('barra lateral')
st.sidebar.slider('Slide na barra lateral',0,100,50)
#Expansors
    

st.image('instagram-logo.png', width=225)
