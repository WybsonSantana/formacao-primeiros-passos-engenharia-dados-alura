import json
import csv


class Dados:

    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.ler_dados()
        self.nomes_colunas = self.obter_nomes_colunas()

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

    def obter_nomes_colunas(self):
        return list(self.dados[-1].keys())

    def renomear_colunas_dados(self, key_mapping):
        new_dados = []
        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados.append(dict_temp)
        self.dados = new_dados
        self.nomes_colunas = self.obter_nomes_colunas()
