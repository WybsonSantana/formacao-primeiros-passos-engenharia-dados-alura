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
    return list(dados[-1].keys())


def renomear_colunas_dados_csv(dados_csv, key_mapping):
    new_dados_csv = []
    for old_dict in dados_csv:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_dados_csv.append(dict_temp)
    return new_dados_csv


def obter_tamanho_da_base(dados):
    return len(dados)


def juntar_base_de_dados(dados_a, dados_b):
    combined_list = []
    combined_list.extend(dados_a)
    combined_list.extend(dados_b)
    return combined_list


def transformar_dados_tabela(dados, nomes_colunas):
    dados_combinados_tabela = [nomes_colunas]
    for row in dados:
        linha = []
        for coluna in nomes_colunas:
            linha.append(row.get(coluna, 'Indisponível'))
        dados_combinados_tabela.append(linha)
    return dados_combinados_tabela


def salvar_dados(dados, path):
    with open(path, 'w', encoding='utf-8', newline='') as file:
        spam_writer = csv.writer(file)
        spam_writer.writerows(dados)


def main():
    # Definição do caminho dos arquivos a serem lidos
    path_json = '..\\data\\raw\\dados_empresaA.json'
    path_csv = '..\\data\\raw\\dados_empresaB.csv'

    # Definição do caminho dos arquivos a serem salvos
    path_dados_combinados = '..\\data\\processed\\dados_combinados.csv'

    # leitura do arquivo de dados no formato json e obtenção dos nomes das colunas
    print('Manipulando o arquivo json...')
    dados_json = ler_dados(path_json, 'json')
    nomes_colunas_json = obter_nomes_colunas(dados_json)
    tamanho_dados_json = obter_tamanho_da_base(dados_json)
    print(f'Tamanho da base de dados: {tamanho_dados_json} itens')
    print(f'Primeiro item da base de dados: {dados_json[0]}')
    print(f'Nomes das colunas: {nomes_colunas_json}\n')

    # leitura do arquivo de dados no formato csv e obtenção dos nomes das colunas
    print('Manipulando o arquivo csv...')
    dados_csv = ler_dados(path_csv, 'csv')
    nomes_colunas_csv = obter_nomes_colunas(dados_csv)
    tamanho_dados_csv = obter_tamanho_da_base(dados_csv)
    print(f'Tamanho da base de dados: {tamanho_dados_csv} itens')
    print(f'Primeiro item da base de dados: {dados_csv[0]}')
    print(f'Nomes das colunas: {nomes_colunas_csv}')

    # Definição do mapeamento dos nomes de colunas para os dados csv
    key_mapping = {'Nome do Item': 'Nome do Produto',
                   'Classificação do Produto': 'Categoria do Produto',
                   'Valor em Reais (R$)': 'Preço do Produto (R$)',
                   'Quantidade em Estoque': 'Quantidade em Estoque',
                   'Nome da Loja': 'Filial',
                   'Data da Venda': 'Data da Venda'}

    # Renomeando os nomes das colunas dos dados csv
    print('Renomeando os nomes das colunas...')
    dados_csv = renomear_colunas_dados_csv(dados_csv, key_mapping)
    nomes_colunas_csv = obter_nomes_colunas(dados_csv)
    print(f'Nomes renomeados das colunas: {nomes_colunas_csv}\n')

    # Manipulando o arquivo com as bases combinadas
    print('Manipulando o arquivo após junção dos dados...')
    dados_fusao = juntar_base_de_dados(dados_json, dados_csv)
    nomes_colunas_fusao = obter_nomes_colunas(dados_fusao)
    tamanho_dados_fusao = obter_tamanho_da_base(dados_fusao)
    print(f'Tamanho da base de dados: {tamanho_dados_fusao} itens')
    print(f'Primeiro item da base de dados: {dados_fusao[0]}')
    print(f'Nomes das colunas: {nomes_colunas_fusao}\n')

    # Transformando e salvando os dados combinados
    print('Transformando e salvando os dados combinados...')
    dados_fusao_tabela = transformar_dados_tabela(dados_fusao, nomes_colunas_fusao)
    salvar_dados(dados_fusao_tabela, path_dados_combinados)
    print('Dados salvos com sucesso!')


main()
