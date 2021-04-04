import streamlit as st
import numpy as np
import pandas as pd
import joblib

def carregadataset(estado):
    if estado == "São Paulo":
        return pd.read_csv('data/datasetfinalsp.csv')
    elif estado == "Minas Gerais":
        return pd.read_csv('data/datasetfinalmg.csv')
    elif estado == "Bahia":
        return pd.read_csv('data/datasetfinalba.csv')
    elif estado == "Rio Grande do Sul":
        return pd.read_csv('data/datasetfinalrs.csv')
    elif estado == "Goiás":
        return pd.read_csv('data/datasetfinalgo.csv')
    elif estado == "Pará":
        return pd.read_csv('data/datasetfinalpa.csv')

#Importação do dataset:
#dataset = pd.read_csv('data/datasetfinal.csv')


def recomenda(produto,dataset):
    cesta = produto
    df = dataset[dataset['antecedents'].str.contains(cesta)] 
    return df[['antecedents','consequents']]

def app():

    from PIL import Image
    foto = Image.open('Groceries.jpeg')
    #st.image(foto, caption='Logo do Streamlit', use_column_width=False)
    
    col1, col2, col3 = st.beta_columns(3)
    foto = Image.open('Groceries.jpeg')#inserindo na coluna 2 
    col2.image(foto, use_column_width=True)
    
    #Título do Sidebar
    st.title("Recomendação de Cesta com Algoritmo Apriori")
    
    #Subtítulo do Sidebar para Escolha do Estado:
    st.subheader("Selecione o Estado")
    
    #Seleção do Estado
    Estado = st.radio('',["Minas Gerais", "São Paulo", "Bahia", "Rio Grande do Sul", "Goiás", "Pará"])
    
    #Carrega dataset
    df_estado = carregadataset(Estado)
    
    #Subtítulo do Sidebar
    st.subheader("Escolha de Produtos")
    
    #Dicionário de Produtos
    product_options = ['-','AGUA', 'MACARRAO', 'ARROZ', 'ACUCAR', 'CAFE COM LEITE', 'MARGARINA COM OU SEM SAL', 'PAO FRANCES',
                      'BIFE', 'CAFE', 'CARNE BOVINA', 'FRANGO EM PEDACOS']
    
    #Caixa de seleção para cada prduto
    Product1 = st.selectbox("Produto 1:", product_options)
    Product2 = st.selectbox("Produto 2:", product_options)
    Product3 = st.selectbox("Produto 3:", product_options)

    #Subtítlo para Resultado do Apriori
    st.subheader('Resultado de Recomendação:')
    
    df_final = pd.concat([recomenda(Product1,df_estado),recomenda(Product2,df_estado),recomenda(Product3,df_estado)])
    st.table(df_final.consequents.unique())
    #st.dataframe(df_final)
    
if __name__ == "__main__":
    app()
