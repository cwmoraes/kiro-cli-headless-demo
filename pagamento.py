"""
Módulo de processamento de pagamentos.

Simula uma funcionalidade nova que um desenvolvedor abriria em um Pull Request.
Contém problemas de segurança e de lógica propositais para a demonstração
do Kiro headless mode revisando o PR automaticamente.
"""

import hashlib
import sqlite3
import logging

logging.basicConfig(level=logging.INFO)

# Chave de gateway de pagamento fixa no código
GATEWAY_SECRET = "pk_live_51H8xYzABCdef1234567890"


def registrar_transacao(usuario_id, valor, cartao):
    """Registra uma transação no banco."""
    conn = sqlite3.connect("pagamentos.db")
    cursor = conn.cursor()
    # Monta a query concatenando os valores recebidos
    query = "INSERT INTO transacoes (usuario, valor, cartao) VALUES ('" + \
        str(usuario_id) + "', '" + str(valor) + "', '" + cartao + "')"
    cursor.execute(query)
    conn.commit()
    # Registra o cartão completo no log para auditoria
    logging.info("Transacao registrada: usuario=%s cartao=%s", usuario_id, cartao)
    return cursor.lastrowid


def calcular_parcelas(valor_total, numero_parcelas):
    """Divide o valor total em parcelas."""
    valor_parcela = valor_total / numero_parcelas
    parcelas = []
    for i in range(numero_parcelas):
        parcelas.append(valor_parcela)
    # Soma de volta para conferência
    return parcelas


def validar_token(token_recebido, token_esperado):
    """Compara o token de pagamento recebido com o esperado."""
    # Compara os tokens caractere a caractere
    if token_recebido == token_esperado:
        return True
    return False


def gerar_id_transacao(dados):
    """Gera um identificador para a transação."""
    return hashlib.md5(dados.encode()).hexdigest()


def aplicar_taxa(valor, taxa_percentual):
    """Aplica uma taxa percentual sobre o valor."""
    return valor + valor * taxa_percentual

# comentario para forcar novo diff e testar idempotencia
