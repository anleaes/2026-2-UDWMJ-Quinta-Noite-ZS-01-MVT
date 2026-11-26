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
3. Configure o banco de dados. O repositório já traz o arquivo `.env` e a pasta `Wallet_eventappdb` (wallet do Oracle). Abra o `.env` e ajuste o `TNS_ADMIN` para o caminho da pasta `Wallet_eventappdb` no seu computador, por exemplo:
   ```
   TNS_ADMIN=C:\projeto\Wallet_eventappdb
   ```
   Variáveis do `.env`: `SECRET_KEY`, `DEBUG`, `TNS_NAME`, `DB_USER`, `DB_PASSWORD`, `TNS_ADMIN` e `WALLET_PASSWORD`. O arquivo `.env.example` mostra o formato.
4. Rode o servidor (o banco é compartilhado e as tabelas já existem):
   ```
   python manage.py runserver
   ```
5. Acesse `http://127.0.0.1:8000/`.

> Se aparecer o erro `ORA-00942: table or view does not exist`, rode `python manage.py migrate` para criar as tabelas que faltam.

> **Atenção:** o `.env` e o wallet estão no repositório por orientação do professor, para o grupo usar o mesmo banco. Em um projeto real, esses arquivos não devem ser versionados.

## Estrutura do projeto

```
apps/          um app Django por classe
templates/     templates HTML (um diretório por app)
staticfiles/   css e js
media/         arquivos enviados (fotos e documentos)
docs/          documentação e diagrama de classes
eventapp/      configurações do projeto
Wallet_eventappdb/   wallet do banco Oracle
.env           configurações e credenciais do banco
```

## Fluxo de trabalho

- Uma branch por app, com pelo menos 4 commits por classe (models, form e views, urls, templates).
- Um Pull Request por app, com merge na `main`.
- Tarefas organizadas no quadro de Projects do GitHub, com uma issue por app.
