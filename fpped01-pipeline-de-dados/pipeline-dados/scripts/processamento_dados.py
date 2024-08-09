import json
import csv


class Dados:

    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.ler_dados()

    def ler_json(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def ler_csv(self):
        dados_csv = []
        with open(self.path, 'r', encoding='utf-8') as file:
            spam_reader = csv.DictReader(file, delimiter=',')
            for row in spam_reader:
                dados_csv.append(row)
        return dados_csv

    def ler_dados(self):
        if self.tipo_dados == 'json':
            return self.ler_json()
        elif self.tipo_dados == 'csv':
            return self.ler_csv()
