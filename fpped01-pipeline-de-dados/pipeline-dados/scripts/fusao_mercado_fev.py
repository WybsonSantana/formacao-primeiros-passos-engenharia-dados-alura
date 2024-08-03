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


def main():
    path_json = '..\\data\\raw\\dados_empresaA.json'
    path_csv = '..\\data\\raw\\dados_empresaB.csv'

    dados_json = ler_dados(path_json, 'json')
    print(dados_json[0])
    print(type(dados_json))

    dados_csv = ler_dados(path_csv, 'csv')
    print(dados_csv[0])
    print(type(dados_csv))


main()
