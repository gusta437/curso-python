import streamlit as st
import datetime
import json
import os

ARQUIVO_DADOS = 'veiculos.json'


def carregar_veiculos():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_veiculos(veiculos):
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(veiculos, f, ensure_ascii=False, indent=4)

def cadastrar_veiculos():
    st.title('Cadastrar Veículo')
    marca = st.text_input('Marca')
    modelo = st.text_input('Modelo')
    ano = st.text_input('Ano')
    conserto = st.text_input('Conserto necessário')

    if st.button('Cadastrar'):
        veiculos = carregar_veiculos()
        veiculo = {'marca': marca, 'modelo': modelo, 'ano': ano, 'conserto': conserto}
        veiculos.append(veiculo)
        salvar_veiculos(veiculos)
        st.success('Veículo cadastrado com sucesso!')
        st.balloons()

def listar_veiculos():
    st.title('Lista de Veículos Cadastrados')
    veiculos = carregar_veiculos()
    if veiculos:
        for i, veiculo in enumerate(veiculos):
            st.write(f"{i+1}. Marca: {veiculo['marca']}, Modelo: {veiculo['modelo']}, Ano: {veiculo['ano']}, Conserto: {veiculo['conserto']}")
    else:
        st.info('Nenhum veículo cadastrado.')

def editar_veiculos():
    st.title('Editar Veículo')
    veiculos = carregar_veiculos()
    if veiculos:
        opcoes = [f"{v['marca']} {v['modelo']} ({v['ano']})" for v in veiculos]
        indice = st.selectbox('Selecione um veículo para editar', range(len(opcoes)), format_func=lambda x: opcoes[x])

        marca = st.text_input('Marca', value=veiculos[indice]['marca'])
        modelo = st.text_input('Modelo', value=veiculos[indice]['modelo'])
        ano = st.text_input('Ano', value=veiculos[indice]['ano'])
        conserto = st.text_input('Conserto', value=veiculos[indice]['conserto'])

        if st.button('Salvar alterações'):
            veiculos[indice] = {'marca': marca, 'modelo': modelo, 'ano': ano, 'conserto': conserto}
            salvar_veiculos(veiculos)
            st.success('Veículo atualizado com sucesso!')
    else:
        st.info('Nenhum veículo cadastrado.')

def excluir_veiculos():
    st.title('Excluir Veículo')
    veiculos = carregar_veiculos()
    if veiculos:
        opcoes = [f"{v['marca']} {v['modelo']} ({v['ano']})" for v in veiculos]
        indice = st.selectbox('Selecione um veículo para excluir', range(len(opcoes)), format_func=lambda x: opcoes[x])
        if st.button('Confirmar exclusão'):
            veiculos.pop(indice)
            salvar_veiculos(veiculos)
            st.success('Veículo excluído com sucesso!')
    else:
        st.info('Nenhum veículo cadastrado.')

# Menu lateral
st.sidebar.title('Menu')
opcao = st.sidebar.radio(
    'Escolha uma opção:',
    ('Cadastrar Veículo', 'Listar Veículos', 'Editar Veículo', 'Excluir Veículo')
)

if opcao == 'Cadastrar Veículo':
    cadastrar_veiculos()
elif opcao == 'Listar Veículos':
    listar_veiculos()
elif opcao == 'Editar Veículo':
    editar_veiculos()
elif opcao == 'Excluir Veículo':
    excluir_veiculos()

st.sidebar.markdown('---')
st.sidebar.markdown('Desenvolvido por Gustavo')
st.sidebar.markdown(f'Total de veículos cadastrados: {len(carregar_veiculos())}')
