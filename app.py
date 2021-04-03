import streamlit as st
import numpy as np
import pandas as pd
import joblib

#Importação do dataset:
dataset = pd.read_csv('data/datasetfinal.csv')


def recomenda(produto):
    cesta = produto
    df = dataset[dataset['antecedents'].str.contains(cesta)] 
    return df[['antecedents','consequents']]

def app():
    
    #Título do Sidebar
    st.title("Recomendação de cesta com Algoritmo Apriori")
    
    #Subtítulo do Sidebar:
    st.subheader("Escolha de Produtos")
    
    #Dicionário de Produtos
    product_options = ['AGUA', 'MACARRAO', 'ARROZ', 'ACUCAR', 'CAFE COM LEITE', 'MARGARINA COM OU SEM SAL', 'PAO FRANCES',
                      'BIFE', 'CAFE', 'CARNE BOVINA', 'FRANGO EM PEDACOS']
    
    Product1 = st.selectbox("Produto 1:", product_options)
    Product2 = st.selectbox("Produto 2:", product_options)
    Product3 = st.selectbox("Produto 3:", product_options)

    st.subheader('Resultado de Recomendação:')
    
    df_final = pd.concat([recomenda(Product1),recomenda(Product2),recomenda(Product3)])
    st.dataframe(df_final.consequents.unique())
    #st.dataframe(df_final)
    
if __name__ == "__main__":
    # command to run the app: streamlit run app.py
    app()