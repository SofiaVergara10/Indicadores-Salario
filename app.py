import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

wg = pd.read_csv("datossalario.csv")
st.title("Indicadores del Salario")
tab1, tab2 = st.tabs(["Análisis Univariado", "Análisis Bivariado"])

with tab1: 
    fig, ax = plt.subplots(1, 4, figsize=(10, 4))
    #salario
    ax[0].hist(wg["wage"])
    #educacion
    ax[1].hist(wg["educ"])
    #experiencia
    ax[2].hist(wg["exper"])
    #Raza
    conteo = wg["nonwhite"].value_counts()
    ax[3].bar(conteo.index, conteo.values)
    fig.tight_layout()
    st.pyplot(fig) 

with tab2: 
    fig, ax = plt.subplots(1, 3, figsize=(10, 4))
    #educ vs salario
    sns.scatterplot(data=wg, x="educ", y="wage", ax=ax[0])
    #experiencia vs salario
    sns.scatterplot(data=wg, x="exper", y="wage", ax=ax[1])
    #Raza vs salario
    sns.boxplot(data=wg, x="nonwhite", y="wage", ax=ax[2])
    fig.tight_layout() #ajusta al recuadro
    st.pyplot(fig) 