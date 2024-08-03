import json
import csv


def ler_json(path_json):
    with open(path_json, 'r', encoding='utf-8') as file:
        return json.load(file)


def ler_csv(path_csv):
    dados_csv = []
    with open(path_csv, 'r', encoding='utf-8') as file:
        spam_reader = csv.DictReader(file, delimiter=',')
        for row in spam_reader:
            dados_csv.append(row)
    return dados_csv


def ler_dados(path, tipo_arquivo):
    if tipo_arquivo == 'json':
        return ler_json(path)
    elif tipo_arquivo == 'csv':
        return ler_csv(path)


def obter_nomes_colunas(dados):
    return list(dados[0].keys())


def renomear_colunas_dados_csv(dados_csv, key_mapping):
    new_dados_csv = []
    for old_dict in dados_csv:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_dados_csv.append(dict_temp)
    return new_dados_csv


def main():
    # Definição do caminho dos arquivos a serem lidos
    path_json = '..\\data\\raw\\dados_empresaA.json'
    path_csv = '..\\data\\raw\\dados_empresaB.csv'

# leitura do arquivo de dados no formato json e obtenção dos nomes das colunas
    dados_json = ler_dados(path_json, 'json')
    print(dados_json[0])
    nomes_colunas_json = obter_nomes_colunas(dados_json)
    print(nomes_colunas_json)

    # leitura do arquivo de dados no formato csv e obtenção dos nomes das colunas
    dados_csv = ler_dados(path_csv, 'csv')
    print(dados_csv[0])
    nomes_colunas_csv = obter_nomes_colunas(dados_csv)
    print(nomes_colunas_csv)

    # Definição do mapeamento dos nomes de colunas para os dados csv
    key_mapping = {'Nome do Item': 'Nome do Produto',
                   'Classificação do Produto': 'Categoria do Produto',
                   'Valor em Reais (R$)': 'Preço do Produto (R$)',
                   'Quantidade em Estoque': 'Quantidade em Estoque',
                   'Nome da Loja': 'Filial',
                   'Data da Venda': 'Data da Venda'}

# Renomeando os nomes das colunas dos dados csv
    dados_csv = renomear_colunas_dados_csv(dados_csv, key_mapping)
    nomes_colunas_csv = obter_nomes_colunas(dados_csv)
    print(nomes_colunas_csv)


main()
