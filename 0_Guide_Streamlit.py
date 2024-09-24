import streamlit as st

st.set_page_config(
    page_title="Projeto em Streamlit",
    page_icon="👋",
)

st.write("# Welcome to my project with Streamlit, my first contact! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
"""
## Trilha de Aprendizado: Do Zero ao Primeiro Projeto com Streamlit

Esta trilha de aprendizado vai guiá-la desde os primeiros passos com o Streamlit até a construção de um projeto real. A jornada é dividida em fases para que você possa avançar de forma organizada e prática.

## Fase 1: Fundamentos de Python

### Objetivo
Ter um conhecimento básico de Python é essencial para começar com Streamlit. Se você ainda não tem, foque em aprender os conceitos principais:

- Variáveis e tipos de dados
- Condicionais e loops
- Funções
- Manipulação de listas e dicionários
- Leitura e escrita de arquivos
- Conhecimento básico de bibliotecas (ex: pandas, numpy, matplotlib)

### Recursos Sugeridos
- [Curso de Python para Iniciantes (em vídeo)](https://www.youtube.com/watch?v=S9uPNppGsGo)
- [Documentação oficial do Python](https://docs.python.org/3/tutorial/index.html)

---

## Fase 2: Introdução ao Streamlit

### Objetivo
Entender o que é o Streamlit, como ele funciona e instalar no seu ambiente de desenvolvimento.

### Passos
1. **Instalação**:
   - Instale o Streamlit usando o pip:
     ```bash
     pip install streamlit
     ```
   - Execute o comando abaixo para verificar se a instalação foi bem-sucedida:
     ```bash
     streamlit hello
     ```
     Isso abrirá um exemplo interativo no seu navegador.

2. **Leitura Básica**:
   - Leia sobre os conceitos iniciais na [documentação oficial](https://docs.streamlit.io/library/get-started).
   - Entenda a proposta do Streamlit: ele permite criar aplicações web com Python de maneira fácil e rápida, sem precisar de conhecimento em front-end.

3. **Crie Seu Primeiro Script**:
   - Crie um arquivo Python chamado `app.py` com o código abaixo:
     ```python
     import streamlit as st
     st.title('Meu Primeiro App com Streamlit')
     st.write("Olá, mundo!")
     ```
   - Execute o arquivo:
     ```bash
     streamlit run app.py
     ```
     Isso vai abrir seu primeiro aplicativo no navegador.

---

## Fase 3: Explorando Componentes do Streamlit

### Objetivo
Familiarizar-se com os principais componentes do Streamlit para começar a construir interfaces interativas.

### Passos
1. **Exibir Texto e Dados**:
   - Use funções como `st.write`, `st.text`, `st.markdown` para mostrar texto, tabelas e gráficos.

2. **Inputs do Usuário**:
   - Pratique criando interações com o usuário através de botões, sliders e checkboxes:
     ```python
     if st.button('Clique aqui'):
         st.write('Você clicou no botão!')
     ```
   - Outros inputs importantes: `st.text_input`, `st.number_input`, `st.file_uploader`.

3. **Visualizando Dados**:
   - Integre gráficos no seu app usando bibliotecas como Matplotlib, Seaborn, ou Plotly:
     ```python
     import matplotlib.pyplot as plt
     import numpy as np

     x = np.linspace(0, 10, 100)
     y = np.sin(x)

     fig, ax = plt.subplots()
     ax.plot(x, y)
     st.pyplot(fig)
     ```

4. **Organizando Layouts**:
   - Divida sua interface em colunas ou use containers:
     ```python
     col1, col2 = st.columns(2)
     with col1:
         st.write("Conteúdo na coluna 1")
     with col2:
         st.write("Conteúdo na coluna 2")
     ```

---

## Fase 4: Projeto Prático

### Objetivo
Criar seu primeiro projeto prático com Streamlit, colocando em prática o que aprendeu nas fases anteriores.

### Exemplo de Projeto: Dashboard de Visualização de Dados

#### Etapas do Projeto

1. **Escolha o Dataset**:
   - Use um conjunto de dados como o Titanic ou outro dataset público do [Kaggle](https://www.kaggle.com/datasets).
   - Exemplo: Um dataset CSV com informações sobre vendas ou dados demográficos.

2. **Crie a Interface**:
   - Implemente os componentes que você já explorou: título, descrição, inputs do usuário para filtrar dados.

3. **Carregue e Exiba os Dados**:
   - Implemente o código para carregar o arquivo CSV e exibir os dados em uma tabela.
   ```python
   import pandas as pd
   import streamlit as st

   uploaded_file = st.file_uploader("Escolha um arquivo CSV")
   if uploaded_file is not None:
       data = pd.read_csv(uploaded_file)
       st.write(data)

"""
)
