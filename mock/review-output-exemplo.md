# Exemplo de saída da revisão (mock)

Este arquivo mostra os dois comentários que o Kiro posta no PR — um de segurança
e um de qualidade. Use para slide ou como fallback se a demo ao vivo falhar.

---

## 🔒 Revisão de segurança (Kiro)

Analisei o diff deste Pull Request. Problemas de segurança encontrados:

### 🔴 Crítico

**1. Desserialização insegura com `pickle` — `feature.py`, linha ~15**
`pickle.loads()` sobre dados externos permite execução remota de código (RCE).
*Correção:* use `json.loads()` para dados não confiáveis.

**2. Path traversal — `feature.py`, linha ~27**
`open("/data/" + user_input)` permite ler arquivos fora do diretório esperado
(ex: `../../etc/passwd`).
*Correção:* valide o caminho com `os.path.realpath` e confirme que está dentro do diretório permitido.

### 🟠 Alto

**3. Verificação SSL desabilitada — `feature.py`, linha ~21**
`requests.get(url, verify=False)` expõe a requisição a ataques man-in-the-middle.
*Correção:* remova `verify=False`.

---
_Gerado via Kiro CLI Headless Mode._

---

## 🧹 Revisão de qualidade de código (Kiro)

Problemas de lógica e qualidade encontrados (não relacionados a segurança):

**1. Fórmula de desconto incorreta — `calcular_desconto`, linha ~31**
A função divide `preco / (percentual / 100)`, o que não calcula um desconto.
O correto para aplicar X% de desconto seria `preco * (1 - percentual / 100)`.
Além disso, não trata `percentual = 0` (divisão por zero).
*Sugestão:* corrigir a fórmula e validar o percentual.

**2. Loop ignora o primeiro item — `processar_pedidos`, linha ~39**
`for i in range(1, len(pedidos))` começa em 1, pulando o pedido de índice 0.
O total sempre exclui o primeiro pedido.
*Sugestão:* iterar direto: `for pedido in pedidos: total += pedido["valor"]`.

**3. Função ignora o parâmetro de busca — `buscar_cliente`, linha ~48**
O `return cliente` dentro do loop retorna sempre o primeiro cliente, ignorando
o parâmetro `nome`. A busca nunca funciona.
*Sugestão:* comparar `cliente["nome"] == nome` antes de retornar.

---
_Gerado via Kiro CLI Headless Mode._
