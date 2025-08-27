def ler_primeiras_linhas(nome_arquivo, x):
    """
    Lê as primeiras X linhas de um arquivo e as imprime na tela.
    
    Parâmetros:
    nome_arquivo (str): caminho/nome do arquivo a ser lido
    x (int): número de linhas a serem lidas
    
    Retorna:
    None
    """
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for i, linha in enumerate(arquivo, 1):
                print(linha, end='')  # end='' para evitar linhas extras
                if i >= x:
                    break
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso:
if __name__ == "__main__":
    nome_do_arquivo = input("Digite o nome do arquivo: ")
    numero_de_linhas = int(input("Quantas linhas deseja ler? "))
    
    ler_primeiras_linhas(nome_do_arquivo, numero_de_linhas)
