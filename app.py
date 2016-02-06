#! flask/bin/python
# -*- coding: utf-8 -*-
"""
Script that creates a simple Flask app that serves a page containing
a report for jobs performed @ a 3730 sequencing platform
"""
from flask import Flask
import MySQLdb
from datetime import datetime
from jinja2 import FileSystemLoader, Environment

USER = '3730bot'
PASSWORD = '3730bot'
DATABASE = 'sequenciador_3730'
QUERY = """
SELECT
sequenciamentos.placa as `Placa`,
usuarios.nome as `Pesquisador`,
usuarios.cpf as `CPF`,
usuarios.instituicao as `Instituição`,
usuarios.telefone as `Fone`,
usuarios.email as `e-mail`,
usuarios.dados_para_nf as `Dados para a NF`,
sequenciamentos.data_sequenciamento as `Data da Corrida`,
sequenciamentos.numero_seqs as `Quantidade de Amostras`
FROM sequenciamentos
INNER JOIN usuarios on sequenciamentos.id_user = usuarios.id
WHERE sequenciamentos.data_sequenciamento LIKE "%/{m}/{y}"
"""

ENV = Environment(loader=FileSystemLoader('.'))
TEMPLATE = ENV.get_template('3730bot.html')

app = Flask(__name__)


@app.route('/')
def index():
    """
    Function that serves the home route. It loads the current month and year,
    queries the database and renders a Jinja2 template as output
    """

    month = datetime.now().month # Loading the current month
    year = datetime.now().year  # Loading the current year
    query = QUERY.format(m=month, y=year) # Formating the query string

    try:
        database = MySQLdb.connect(host='localhost', user=USER, passwd=PASSWORD,
                                   db=DATABASE, use_unicode=True)
    except:
        return "500"

    cursor = database.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return TEMPLATE.render(records=result)

if __name__ == '__main__':
    app.run(debug=True)
