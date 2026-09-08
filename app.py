"""
Aplicação de exemplo para demo do Kiro Headless Mode.

ATENÇÃO: Este arquivo contém vulnerabilidades PROPOSITAIS para fins de
demonstração. NÃO use este código em produção. As falhas aqui existem
para que o agente de revisão do Kiro as identifique ao vivo na demo.
"""

import sqlite3
import os
import hashlib


# PROBLEMA 1: credencial hardcoded no código-fonte
API_KEY = "sk_live_1234567890abcdef"
DB_PASSWORD = "admin123"


def get_user(user_id):
    """Busca um usuário pelo ID."""
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # PROBLEMA 2: SQL injection - concatenação direta de input na query
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return cursor.fetchone()


def run_backup(filename):
    """Executa backup do banco."""
    # PROBLEMA 3: command injection - input direto no os.system
    os.system("cp app.db " + filename)


def hash_password(password):
    """Gera hash da senha do usuário."""
    # PROBLEMA 4: uso de MD5 para senha (algoritmo fraco/quebrado)
    return hashlib.md5(password.encode()).hexdigest()


def login(username, password):
    """Autentica um usuário."""
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # PROBLEMA 5: SQL injection na autenticação (crítico)
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)
    user = cursor.fetchone()
    if user:
        return True
    return False
