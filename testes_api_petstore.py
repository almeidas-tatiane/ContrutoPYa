import pytest
import requests

url = 'https://petstore.swagger.io/v2/user'

def testar_incluir_usuario():
    # Configura
    status_code_esperado = 200   # comunicação
    codigo_esperado = 200        # funcional
    tipo_esperado = 'unknown'    # fixo como desconhecido
    messagem_esperada = '18228'  # id do usuario



    headers = {'Content-Type': 'application/json'}

    #Executa
    resposta= requests.post(f'{url}',
                            data=open('json/usuario1.json', 'rb'), headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code) # Status Code
    print(resposta.json()) # Response Body

    #Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == messagem_esperada

def testar_consultar_usuario():
    # Configura
    username = 'almeidas.tatiane'  # input / entrada para a consulta
    id_esperado= 18228
    username_esperado = 'almeidas.tatiane'
    email_esperado = 'almeidas.tatiane@iterasys.com.br'
    telefone_esperado = '19999999999'
    user_status = 0
    status_code_esperado = 200

    headers = {'Content-Type': 'application/json'}

    #Executa
    resposta = requests.get(f'{url}/{username}', headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(resposta.json())  # Response Body

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['username'] == username_esperado
    assert corpo_da_resposta['id'] == id_esperado
    assert corpo_da_resposta['email'] == email_esperado
    assert corpo_da_resposta['phone'] == telefone_esperado
    assert corpo_da_resposta['userStatus'] == user_status

def testar_atualizar_usuario():
    #Configura
    username = 'almeidas.tatiane'  #input
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    messagem_esperada = '18229'


    headers = {'Content-Type': 'application/json'}

    #Executa
    resposta = requests.put(f'{url}/{username}',
                            data=open('json/usuario2.json', 'rb'), headers=headers)


    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(resposta.json())


    #Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == messagem_esperada



def testar_deletar_usuario():
    #Configura
    username = 'almeidas.tatiane'  #input
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    messagem_esperada = 'almeidas.tatiane'

    headers = {'Content-Type': 'application/json'}

    #Executa
    resposta = requests.delete(f'{url}/{username}', headers=headers)


    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(resposta.json())



    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == messagem_esperada

def testar_consultar_usuario_e_extrair_senha(username):
    # Configura
    id_esperado = 18228
    username_esperado = 'almeidas.tatiane'
    email_esperado = 'almeidas.tatiane@iterasys.com.br'
    telefone_esperado = '19999999999'
    user_status = 0
    status_code_esperado = 200

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.get(f'{url}/{username}', headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(resposta.json())  # Response Body

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['username'] == username_esperado
    assert corpo_da_resposta['id'] == id_esperado
    assert corpo_da_resposta['email'] == email_esperado
    assert corpo_da_resposta['phone'] == telefone_esperado
    assert corpo_da_resposta['userStatus'] == user_status

    return corpo_da_resposta['password']

def testar_login(username, password):
    # Configura
    status_code_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = 'logged in user session:'

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.get(f'{url}/login?username={username}&password={password}', headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(resposta.json())  # Response Body

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == status_code_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert mensagem_esperada in corpo_da_resposta['message']
    token = corpo_da_resposta['message'].rpartition(':')[-1]

    print(f'Token: {token}')
    return token

def testar_orquestracao_consultar_senha_e_realizar_login():
    # vai orquestrar as chamadas de duas funções para atingir o seu objetivo

    #Configura
    username = 'almeidas.tatiane'

    #Executa
    password = testar_consultar_usuario_e_extrair_senha(username)
    token = testar_login(username, password)
    print(f'Token no maestro: {token}')

