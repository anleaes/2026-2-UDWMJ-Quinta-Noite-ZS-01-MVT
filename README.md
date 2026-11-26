# EventApp - Sistema de Venda de Ingressos

Repositório: 2026-2-UDWMJ-Quinta-Noite-ZS-01-MVT

Projeto A3 (Desenvolvimento Web com Django): sistema web para venda de ingressos de eventos, feito em Django (padrão MTV) com banco Oracle Cloud (OCI).

## Integrantes

- Oliver Cowley
- Diogo Gomes
- Patrick Waschburger

## Tecnologias

- Python e Django (padrão MTV)
- Banco de dados Oracle (OCI) com `oracledb`
- python-decouple (variáveis de ambiente)
- Pillow (upload de imagens)
- HTML e CSS (layout próprio, sem frameworks)

## Classes (apps)

| App | Descrição |
|---|---|
| Atracao | Artistas e atrações dos eventos |
| Organizador | Quem organiza os eventos |
| Local | Locais onde os eventos acontecem |
| Evento | Eventos (organizador, local e atrações) |
| Setor | Setores de cada local |
| Cupom | Cupons de desconto de cada evento |
| Lote | Lotes de ingressos (preço e quantidade) |
| Participante | Pessoas que compram ingressos |
| Pedido | Pedidos feitos pelos participantes |
| Pagamento | Pagamento de cada pedido |
| Ingresso | Ingressos emitidos em cada pedido |
| CheckIn | Registro de entrada no evento |

O diagrama de classes está em [`docs/diagrama.md`](docs/diagrama.md).

## Como executar

1. Clone o repositório e entre na pasta:
   ```
   git clone https://github.com/anleaes/2026-2-UDWMJ-Quinta-Noite-ZS-01-MVT.git
   cd 2026-2-UDWMJ-Quinta-Noite-ZS-01-MVT
   ```
2. Crie e ative o ambiente (Miniconda):
   ```
   conda create -n eventapp python
   conda activate eventapp
   pip install -r requirements.txt
   ```
3. Crie o arquivo `.env` a partir do exemplo e preencha com os seus dados:
   ```
   copy .env.example .env
   ```
   Variáveis: `SECRET_KEY`, `DEBUG`, `TNS_NAME`, `DB_USER`, `DB_PASSWORD`, `TNS_ADMIN` e `WALLET_PASSWORD`.
4. Coloque a pasta do wallet do Oracle no computador e aponte o `TNS_ADMIN` para ela.
5. Crie as tabelas e rode o servidor:
   ```
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```
6. Acesse `http://127.0.0.1:8000/`.

> O `.env` e o wallet **não** são enviados ao Git.

## Estrutura do projeto

```
apps/          um app Django por classe
templates/     templates HTML (um diretório por app)
staticfiles/   css e js
media/         arquivos enviados (fotos e documentos)
docs/          documentação e diagrama de classes
eventapp/      configurações do projeto
```

## Fluxo de trabalho

- Uma branch por app, com pelo menos 4 commits por classe (models, form e views, urls, templates).
- Um Pull Request por app, com merge na `main`.
- Tarefas organizadas no quadro de Projects do GitHub, com uma issue por app.
