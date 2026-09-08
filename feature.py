"""
Arquivo de exemplo para ABRIR O PULL REQUEST na demo.

Durante a demo, adicione este arquivo (ou altere-o) numa branch nova e abra
um PR. Ele contém falhas de SEGURANÇA e problemas de QUALIDADE/LÓGICA — assim
a revisão mostra os dois tipos de análise no mesmo PR.
"""

import pickle
import requests


def load_config(data):
    """Carrega configuração serializada."""
    # SEGURANÇA: desserialização insegura com pickle (permite RCE)
    return pickle.loads(data)


def fetch_data(url):
    """Busca dados de uma URL externa."""
    # SEGURANÇA: SSL verification desabilitada
    response = requests.get(url, verify=False)
    return response.json()


def build_path(user_input):
    """Monta um caminho de arquivo a partir de input do usuário."""
    # SEGURANÇA: path traversal - input não sanitizado
    return open("/data/" + user_input).read()


def calcular_desconto(preco, percentual):
    """Aplica um desconto percentual sobre o preço."""
    # QUALIDADE/LÓGICA: divisão sem tratar percentual = 0 ou negativo;
    # e a fórmula está errada (deveria multiplicar por (1 - pct/100))
    return preco / (percentual / 100)


def processar_pedidos(pedidos):
    """Processa uma lista de pedidos e retorna o total."""
    total = 0
    # QUALIDADE: loop com índice manual em vez de iterar direto;
    # quebra se a lista estiver vazia por causa do range mal calculado
    for i in range(1, len(pedidos)):
        total = total + pedidos[i]["valor"]
    return total


def buscar_cliente(clientes, nome):
    """Busca um cliente pelo nome."""
    # QUALIDADE/LÓGICA: retorna dentro do loop no primeiro item errado;
    # sempre retorna o primeiro cliente, ignorando o parâmetro 'nome'
    for cliente in clientes:
        return cliente
