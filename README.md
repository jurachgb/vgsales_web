# VGSales Web 🎮

🇧🇷 Aplicação web para análise de dados de vendas de jogos eletrônicos, construída com Flask e SQLite.

🇺🇸 Web application for analyzing video game sales data, built with Flask and SQLite.

---

## Funcionalidades / Features

- 🌍 Top N jogos mais vendidos globalmente / Top N best-selling games globally
- 📅 Top N jogos mais vendidos por ano / Top N best-selling games by year
- 🎮 Top N jogos mais vendidos por gênero / Top N best-selling games by genre
- 🔍 Busca de jogos por nome / Search games by name
- ⚔️ Comparador de dois gêneros lado a lado / Compare two genres side by side

---

## Como rodar / How to run

🇧🇷
1. Clone o repositório
2. Instale o Flask: `pip install flask`
3. Baixe o `vgsales.csv` no [Kaggle](https://www.kaggle.com/datasets/gregorut/videogamesales) e coloque na pasta do projeto
4. Gere o banco de dados: `python conversor_csv_SQL.py`
5. Rode a aplicação: `python app.py`
6. Acesse no navegador: `http://localhost:5000`

🇺🇸
1. Clone the repository
2. Install Flask: `pip install flask`
3. Download `vgsales.csv` from [Kaggle](https://www.kaggle.com/datasets/gregorut/videogamesales) and place it in the project folder
4. Generate the database: `python conversor_csv_SQL.py`
5. Run the application: `python app.py`
6. Open in browser: `http://localhost:5000`

---

## Tecnologias / Technologies

Python 3 · Flask · SQLite3 · Bootstrap 5 · Jinja2
