# Demo — Kiro CLI Headless Mode

Repositório de demonstração do **Kiro Headless Mode** revisando Pull Requests
automaticamente. A cada PR, o Kiro posta **dois comentários**: um de **segurança**
e um de **qualidade de código**.

> ⚠️ Os arquivos `app.py` e `feature.py` contêm problemas **propositais** para fins
> de demonstração. Não é código de produção.

## Como funciona

1. Você abre um Pull Request neste repositório.
2. O GitHub Actions dispara o workflow `.github/workflows/kiro-review.yml`.
3. O workflow instala o Kiro CLI, gera o diff do PR e roda o Kiro em modo headless
   duas vezes — uma análise de segurança e uma de qualidade.
4. O Kiro posta dois comentários no PR com os problemas encontrados.

Ninguém aperta nenhum botão — roda sozinho no pipeline. As duas análises são
apenas prompts diferentes para o mesmo agente.

## Pré-requisitos

- Assinatura Kiro Pro (ou superior) para gerar API key.
- Uma API key gerada em [app.kiro.dev](https://app.kiro.dev) na seção **API Keys**.
- A key salva como secret do repositório: `Settings > Secrets and variables > Actions`,
  com o nome `KIRO_API_KEY`.

## Estrutura

```
demo-repo/
├── app.py                          # código com 5 falhas de segurança propositais
├── feature.py                      # arquivo para abrir o PR (segurança + qualidade)
├── README.md                       # este arquivo
├── .github/
│   └── workflows/
│       └── kiro-review.yml         # workflow: 2 análises (segurança + qualidade)
└── mock/
    ├── kiro-review-mock.yml         # workflow mockado (2 comentários, offline)
    └── review-output-exemplo.md     # saída de exemplo para slide/fallback
```

## Rodando a demo

1. Suba este repositório no GitHub.
2. Configure o secret `KIRO_API_KEY`.
3. Crie uma branch e adicione o `feature.py` (ou altere o `app.py`).
4. Abra um Pull Request.
5. Acompanhe o workflow na aba **Actions** e veja os dois comentários aparecerem no PR.

> Sem API key ou offline? Use o workflow em `mock/kiro-review-mock.yml`, que posta
> os dois comentários pré-escritos sem chamar o Kiro de verdade.

## Problemas plantados

### `app.py` — segurança

| # | Problema | Severidade |
|---|----------|-----------|
| 1 | Credencial hardcoded (`API_KEY`, `DB_PASSWORD`) | Crítico |
| 2 | SQL injection em `get_user` | Alto |
| 3 | Command injection em `run_backup` | Crítico |
| 4 | Hash MD5 para senha | Médio |
| 5 | SQL injection em `login` | Crítico |

### `feature.py` — segurança + qualidade (é o que abre o PR)

| # | Problema | Tipo |
|---|----------|------|
| 1 | Desserialização insegura com `pickle` (RCE) | Segurança |
| 2 | SSL verification desabilitada | Segurança |
| 3 | Path traversal em `build_path` | Segurança |
| 4 | Fórmula de desconto incorreta em `calcular_desconto` | Qualidade/Lógica |
| 5 | Loop que pula o primeiro item em `processar_pedidos` | Qualidade/Lógica |
| 6 | `buscar_cliente` ignora o parâmetro de busca | Qualidade/Lógica |
