import requests

import pandas as pd
import streamlit as st


def fazer_request(url, params=None):
    resposta = requests.get(url, params=params, timeout = 10)
    try: 
        resposta.raise_for_status()
    except requests.HTTPError as e:
        print(f'Error no request: {e}')
        resultado = None
    else:
        resultado = resposta.json()
    return resultado

def pegar_nome_por_decada(nome):
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
    dados_decadas = fazer_request(url=url)
    if not dados_decadas:
        return {}
    dict_decadas = {}
    for dados in dados_decadas[0]['res']:
        decada = dados['periodo']
        quantidade = dados['frequencia']
        dict_decadas[decada] = quantidade
        
    return dict_decadas


def main():
    st.title('Web App Nomes')
    st.write('Dados do IBGE (fonte: https://servicodados.ibge.gov.br/api/docs/nomes?versao=2)')

    nome = st.text_input('Consulte um nome')
    if not nome:
        st.stop()
    if " " in nome:
        st.info("A API do IBGE pode não retornar dados para nomes compostos.")
    nome = nome.strip().lower()

    dict_decadas = pegar_nome_por_decada(nome)
    if not dict_decadas:
        st.warning(f'Nenhum dados encontrado para o nome {nome}')
        st.stop()

    df = pd.DataFrame.from_dict(dict_decadas, orient = "index", columns=["Frequência"])
    df.index.name = "Década"
    df = df.sort_index()  

    col1, col2 = st.columns([0.3,0.7])
    with col1:
        st.write('Frequência por década')
        st.dataframe(df)
    
    with col2:
        st.write('Evolução no tempo')
        st.line_chart(df)

if __name__ == '__main__':
    main()