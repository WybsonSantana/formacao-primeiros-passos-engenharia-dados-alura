import json
import csv


class Dados:

    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.ler_dados()
        self.nomes_colunas = self.obter_nomes_colunas()
        self.quantidade_linhas = self.obter_tamanho_da_base()

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
            dados = self.ler_json()
        elif self.tipo_dados == 'csv':
            dados = self.ler_csv()
        elif self.tipo_dados == 'list':
            dados = self.path
            self.path = 'lista em memória'
        return dados

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

    def obter_tamanho_da_base(self):
        return len(self.dados)

    def juntar_base_de_dados(dados_a, dados_b):
        combined_list = []
        combined_list.extend(dados_a.dados)
        combined_list.extend(dados_b.dados)
        return Dados(combined_list, 'list')

    def transformar_dados_tabela(self):
        dados_combinados_tabela = [self.nomes_colunas]
        for row in self.dados:
            linha = []
            for coluna in self.nomes_colunas:
                linha.append(row.get(coluna, 'Indisponível'))
            dados_combinados_tabela.append(linha)
        return dados_combinados_tabela

    def salvar_dados(self, path):
        dados_combinados_tabela = self.transformar_dados_tabela()
        with open(path, 'w', encoding='utf-8', newline='') as file:
            spam_writer = csv.writer(file)
            spam_writer.writerows(dados_combinados_tabela)
