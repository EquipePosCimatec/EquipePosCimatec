import streamlit as st

#cabeçalho

col1,_, col2, __ = st.columns([3,2,3,2]) 

# Posicionando as imagens em cada coluna
with col1:
          st.image('https://www.mpba.mp.br/sites/all/themes/prodeb/logo.png', width=300)
with col2:
          st.image('https://arquivo.rhsconsult.com.br/logo/1695063140_senai%20cimatec.png', width=300)
st.markdown("---")
st.markdown('### TRABALHO DE MACHINE LEARNING HANDS-ON ###')
st.markdown('---')
st.markdown('#### Turma do Ministério Público do Estado da Bahia ####')
st.markdown('#### **Disciplina:** Machine Learning Hands On ####')
st.markdown('#### **Professor:** Ricardo Ferreira da Rocha ####')
st.markdown('#### **Alunos:** ####')
st.markdown('>>- ##### ***Carlos Bastos Stucki*** #####')
st.markdown('>>- ##### ***Gerson Adriano Yamashita*** #####')
st.markdown('>>- ##### ***Rodrigo da Silva Nunes*** #####')



