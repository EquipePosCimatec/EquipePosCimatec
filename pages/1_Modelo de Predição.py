import streamlit as st 
import pandas as pd
import numpy as np
from pycaret.regression import load_model, predict_model
from pycaret.datasets import get_data
from PIL import Image

base = get_data('us_presidential_election_results')
modelo = load_model('recursos/modelo-previsao-ganhador-gbc')

st.header('🤵 Deploy do Modelo de Previsão de Vencedor da Eleição Presidencial dos EUA')
st.markdown('---')
#Widgets para fazer os inputs do modelo

#cycle                  False
#state                  False
#dem_poll_avg           False
#dem_poll_avg_margin    False
#incumbent_party        False
#incumbent_running      False
#party_winner           False

col1, col2, col3, col4 = st.columns(4)

with col4:
	cycle  = st.selectbox(label = 'Ano da Eleição Presidencial', 
		options = base['cycle'].unique())
with col3:
	state  = st.selectbox(label = 'Estado dos Estados Unidos', 
		options = base['state'].unique())

with col1:
	def trad(x):
		return 'Republicano' if x == 'republican' else 'Democrata'
	incumbent_party	= st.radio('Partido', ['republican', 'democrat'], format_func = trad)
with col2:
	# incumbent_running : Indica se o presidente em exercício está concorrendo novamente naquela eleição (1 indica que está concorrendo, 0 indica o contrário).
	def trad2(x):
		return "SIM" if x == 1 else 'NÃO'
	incumbent_running	= st.radio('O presidente está concorrendo a Reeleição?', [1, 0], format_func = trad2)


col5,_, col6 = st.columns([5,1,5])

with col5:
	dem_poll_avg = st.slider(label = ' Média das pesquisas de opinião para o candidato', 
	min_value=17.450183, 
	max_value=87.344071, 
	value= 42.408222, 
	step=0.000001, 
	help='Informe a Média das pesquisas de opinião')
	st.write(f"Valor selecionado: {dem_poll_avg:.6f}")

with col6:
	dem_poll_avg_margin = st.slider(label = ' Margem média entre os candidados republicano e democrata', 
	min_value=-46.972194, 
	max_value=79.091771, 
	value= -1.967499, 
	step=0.000001, 
	help='margem média nas pesquisas de opinião para o candidato democrata em relação ao candidato republicano no estado específico')
	st.write(f"Valor selecionado: {dem_poll_avg_margin:.6f}")
	

#Criar um DataFrame com os inputs exatamente igual ao dataframe em que foi treinado o modelo

aux = {'cycle': [cycle],
		'state': [state],
		'dem_poll_avg': [dem_poll_avg ],
		'dem_poll_avg_margin': [dem_poll_avg_margin],
		'incumbent_party': [incumbent_party],
		'incumbent_running': [incumbent_running]}

prever = pd.DataFrame(aux)

#st.write(prever)

#Usar o modelo salvo para fazer previsao nesse Dataframe

botao = st.button('Prever Partido Vencedor',
		type = 'primary',
		use_container_width = True)

imgrep='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8XrXrH_z-XUEcJ_mnjUyEjfor7sCKZWohMKXl9Vs6WGwhskcnIpO-0zH5BA&s'
imgdem='https://img.freepik.com/vetores-premium/um-burro-nas-cores-do-simbolo-da-bandeira-americana-do-partido-democrata-dos-eua-isolado-icone-vector-ilustracao-design_431724-7343.jpg?w=740'


if botao:
	previsao = predict_model(modelo, data = prever)
	venc = previsao.loc[0,'prediction_label']
	partido_vencedor = ('Republicano' if venc == 1 else 'Democrata')
	img_vencedor = (imgrep if venc == 1 else imgdem)
	st.write(f'### O partido vencedor é o: {partido_vencedor}')
	st.image(img_vencedor ,width=300)
st.markdown("---")
	


