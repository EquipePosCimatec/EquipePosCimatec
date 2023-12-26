import streamlit as st

#cabeçalho

col1,_, col2, __ = st.columns([3,2,3,2]) 

# Posicionando as imagens em cada coluna
with col1:
          st.image('https://www.mpba.mp.br/sites/all/themes/prodeb/logo.png', width=300)
with col2:
          st.image('https://arquivo.rhsconsult.com.br/logo/1695063140_senai%20cimatec.png', width=300)
st.markdown("---")
# Título
st.title('Aplicação de Data Science e Analytics')

# Introdução
st.markdown("""Este trabalho tem como objetivo explorar a aplicação de Data Science e Analytics, com base no aprendizado da Pós Graduação do MPBA no Cimatec. Através do uso de técnicas de Machine Learning, implementadas na linguagem Python, busca-se desenvolver modelos preditivos que ajudem na eficiencia do trabalho no MPBA.
""")

# Modelos de Machine Learning
st.subheader('Exemplos de Modelos de Machine Learning')

# Regressão Linear
st.markdown("""
**Regressão Linear:**
Utilizada para prever metas de rendimento e estimativas de trabalho. É um modelo simples, mas eficaz para prever valores contínuos baseados em variáveis independentes.
""")

# Árvores de Decisão e Florestas Aleatórias
st.markdown("""
**Árvores de Decisão e Florestas Aleatórias:**
Ideais para classificar o tamanho adequado de equipes administrativas baseadas em diversos fatores, como carga de trabalho, eficiência de equipe, entre outros.
""")

# Redes Neurais Artificiais
st.markdown("""
**Redes Neurais Artificiais:**
Podem ser aplicadas para prever as necessidades futuras de Promotorias de Justiça, considerando padrões complexos e não lineares nos dados.
""")

