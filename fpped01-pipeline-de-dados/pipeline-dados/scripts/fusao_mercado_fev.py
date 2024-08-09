from processamento_dados import Dados


def main():
    # Definição do caminho dos arquivos a serem lidos
    path_json = '../data/raw/dados_empresaA.json'
    path_csv = '../data/raw/dados_empresaB.csv'

    # Definição do caminho dos arquivos a serem salvos
    path_dados_combinados = '../data/processed/dados_combinados.csv'

    # Etapa de extração dos dados
    # leitura do arquivo de dados no formato json, obtenção dos nomes das colunas e tamanho da base
    print('Manipulando o arquivo json...')
    dados_empresa_a = Dados(path_json, 'json')
    print(f'Tamanho da base de dados: {dados_empresa_a.quantidade_linhas} itens')
    print(f'Nomes das colunas: {dados_empresa_a.nomes_colunas}')
    print(f'Primeiro item da base: {dados_empresa_a.dados[0]}\n')

    # leitura do arquivo de dados no formato csv, obtenção dos nomes das colunas e tamanho da base
    print('Manipulando o arquivo csv...')
    dados_empresa_b = Dados(path_csv, 'csv')
    print(f'Tamanho da base de dados: {dados_empresa_b.quantidade_linhas} itens')
    print(f'Nomes das colunas: {dados_empresa_b.nomes_colunas}')
    print(f'Primeiro item da base: {dados_empresa_b.dados[0]}\n')

    # Definição do mapeamento dos nomes de colunas para os dados csv
    key_mapping = {'Nome do Item': 'Nome do Produto',
                   'Classificação do Produto': 'Categoria do Produto',
                   'Valor em Reais (R$)': 'Preço do Produto (R$)',
                   'Quantidade em Estoque': 'Quantidade em Estoque',
                   'Nome da Loja': 'Filial',
                   'Data da Venda': 'Data da Venda'}

    # Renomeando os nomes das colunas dos dados csv
    print('Renomeando os nomes das colunas...')
    dados_empresa_b.renomear_colunas_dados(key_mapping)
    print(f'Nomes renomeados das colunas: {dados_empresa_b.nomes_colunas}')
    print(f'Primeiro item da base: {dados_empresa_b.dados[0]}\n')

    # Manipulando o arquivo com as bases combinadas
    print('Manipulando o arquivo após junção dos dados...')
    dados_fusao = Dados.juntar_base_de_dados(dados_empresa_a, dados_empresa_b)
    print(f'Tamanho da base de dados: {dados_fusao.quantidade_linhas} itens')
    print(f'Nomes das colunas: {dados_fusao.nomes_colunas}')
    print(f'Primeiro item da base: {dados_fusao.dados[0]}\n')

    # Transformando e salvando os dados combinados
    print('Transformando e salvando os dados combinados...')
    dados_fusao.salvar_dados(path_dados_combinados)
    print('Dados salvos com sucesso!')


main()
