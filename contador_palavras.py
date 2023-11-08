
import requests  # Usado para fazer solicitações HTTP
from bs4 import BeautifulSoup  # Usado para analisar HTML
from collections import Counter  # Usado para contar elementos em uma lista
import string  # Usado para operações com strings
from googletrans import Translator  # Usado para tradução de palavras
import json  # Usado para manipular dados JSON
import re  # Usado para expressões regulares


# Inicializa o dicionário de contagem global
contagem_palavras_global = Counter()

def traduzir_ingles_para_portugues(palavra_em_ingles):
    """
    Traduz uma palavra do inglês para o português usando a biblioteca googletrans.

    Args:
        palavra_em_ingles (str): A palavra em inglês que será traduzida.

    Returns:
        str: A tradução da palavra em português.

    Raises:
        Exception: Em caso de erro na tradução, uma exceção é capturada e uma mensagem de erro é exibida.

    Exemplo de uso:
     traduzir_ingles_para_portugues("apple")
    'maçã'
    """
    try:
        # Inicializa um objeto Translator para tradução
        translator = Translator()

        # Realiza a tradução da palavra do inglês (src='en') para o português (dest='pt')
        traducao = translator.translate(palavra_em_ingles, src='en', dest='pt')

        # Retorna o texto da tradução
        return traducao.text
    except Exception as e:
        # Em caso de erro, captura a exceção e exibe uma mensagem de erro
        print(f"Erro na tradução: {e}")
        return None

# Função para obter o conteúdo de uma URL
def obter_conteudo_da_url(url):
    """
    Obtém o conteúdo de uma URL por meio de uma solicitação HTTP.

    Args:
        url (str): A URL da qual o conteúdo será obtido.

    Returns:
        str: O conteúdo da URL como texto, caso a solicitação seja bem-sucedida.
        None: Caso ocorra um erro durante a solicitação.

    Exemplo de uso:
     conteudo = obter_conteudo_da_url("http://example.com")
     if conteudo:
         print(conteudo)
     else:
         print("Erro ao obter conteúdo da URL")
    """
    try:
        # Realiza uma solicitação HTTP GET para a URL especificada
        response = requests.get(url)

        # Verifica se o código de status da resposta é 200 (OK)
        if response.status_code == 200:
            # Retorna o conteúdo da resposta como texto
            return response.text
        else:
            # Se o código de status não for 200, exibe uma mensagem de erro
            print("Erro ao acessar a URL. Código de status:", response.status_code)
            return None
    except Exception as e:
        # Em caso de erro na solicitação, captura a exceção e exibe uma mensagem de erro
        print("Erro ao acessar a URL:", e)
        return None

# Função para contar palavras em um texto
def contar_palavras(texto):
    """
    Conta a ocorrência de palavras em um texto.

    Args:
        texto (str): O texto a ser analisado.

    Returns:
        collections.Counter: Um objeto Counter que contém as palavras e suas contagens.

    Exemplo de uso:
     texto = "Este é um exemplo de texto. Um exemplo simples."
     contagem = contar_palavras(texto)
     print(contagem)
    """
    # Divide o texto em palavras usando espaço em branco como separador
    palavras = texto.split()

    # Remove pontuações e converte todas as palavras para minúsculas
    palavras = [p.strip(string.punctuation).lower() for p in palavras]

    # Usa a classe Counter do módulo collections para contar as palavras
    return Counter(palavras)

def ordenar_dicionario_por_ocorrencia(dicionario):
    """
    Ordena um dicionário com base na quantidade de ocorrências dos valores.

    Args:
        dicionario (dict): O dicionário a ser ordenado.

    Returns:
        dict: Um novo dicionário contendo os mesmos pares chave-valor, mas ordenados por ocorrência (do maior para o menor).

    Exemplo de uso:
     dicionario = {'apple': 3, 'banana': 1, 'cherry': 5}
     dicionario_ordenado = ordenar_dicionario_por_ocorrencia(dicionario)
     print(dicionario_ordenado)
    """
    # Usa a função `sorted` para ordenar o dicionário com base no valor (quantidade de ocorrências)
    # A chave de ordenação é uma função lambda que retorna o valor associado à chave
    # `reverse=True` indica que a ordenação será do maior para o menor
    dicionario_ordenado = dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=True))

    return dicionario_ordenado

def salvar_dicionario_em_arquivo(dicionario, nome_arquivo):
    """
    Salva um dicionário em um arquivo JSON.

    Args:
        dicionario (dict): O dicionário a ser salvo.
        nome_arquivo (str): O nome do arquivo onde o dicionário será salvo.

    Returns:
        None

    Exemplo de uso:
     dicionario = {'apple': 3, 'banana': 1, 'cherry': 5}
     nome_arquivo = 'dicionario.json'
     salvar_dicionario_em_arquivo(dicionario, nome_arquivo)
    Dicionário salvo com sucesso no arquivo dicionario.json
    """
    try:
        # Abre o arquivo especificado em modo de escrita ('w')
        with open(nome_arquivo, 'w') as arquivo:
            # Usa a função `json.dump` para escrever o dicionário no arquivo no formato JSON
            json.dump(dicionario, arquivo)
        print(f"Dicionário salvo com sucesso no arquivo {nome_arquivo}")
    except Exception as e:
        # Em caso de erro, captura a exceção e exibe uma mensagem de erro
        print(f"Erro ao salvar o dicionário: {e}")

def criar_dicionario_apenas_com_palavras(do_dicionario):
    """
    Cria um novo dicionário contendo apenas palavras válidas (sem caracteres especiais) do dicionário de entrada.

    Args:
        do_dicionario (dict): O dicionário de entrada que pode conter palavras e outros valores.

    Returns:
        dict: Um novo dicionário contendo apenas as palavras válidas do dicionário de entrada.

    Exemplo de uso:
     dicionario = {'apple': 3, 'banana': 1, 'cherry': 5, '123abc': 2}
     novo_dicionario = criar_dicionario_apenas_com_palavras(dicionario)
     print(novo_dicionario)
    """
    # Expressão regular para verificar se uma chave é uma palavra composta apenas por letras (sem caracteres especiais)
    padrao_palavra = re.compile(r"^[a-zA-Z]+$")

    # Inicializa um novo dicionário
    novo_dicionario = {}

    # Itera sobre as chaves e valores do dicionário de entrada
    for chave, valor in do_dicionario.items():
        # Verifica se a chave corresponde ao padrão de palavra
        if padrao_palavra.match(chave):
            # Se a chave for uma palavra válida, adiciona ao novo dicionário
            novo_dicionario[chave] = valor

    return novo_dicionario

def traduzir_dicionario(dicionario):
    """
    Traduz as palavras de um dicionário do inglês para o português e cria um novo dicionário com as traduções.

    Args:
        dicionario (dict): O dicionário contendo as palavras a serem traduzidas e suas ocorrências.

    Returns:
        list: Uma lista de dicionários contendo as palavras traduzidas, suas ocorrências e as palavras originais.

    Exemplo de uso:
     dicionario = {'apple': 3, 'banana': 1, 'cherry': 5}
     dicionario_traduzido = traduzir_dicionario(dicionario)
     print(dicionario_traduzido)
     """
    # Inicializa uma lista para armazenar os dicionários das palavras traduzidas
    dicionario_traduzido = []

    a = 1
    # Itera sobre as palavras e suas ocorrências no dicionário de entrada
    for palavra, ocorrencia in dicionario.items():
        # Exibe informações de progresso
        print(f"{ocorrencia} x {palavra} é {a} de {len(dicionario)}")
        a += 1

        # Chama a função `traduzir_ingles_para_portugues` para obter a tradução da palavra
        traducao = traduzir_ingles_para_portugues(palavra)

        # Verifica se a tradução foi bem-sucedida
        if traducao:
            # Adiciona um novo dicionário com a palavra original, sua tradução e o número de ocorrências
            dicionario_traduzido.append({palavra: {"traducao": traducao, "ocorrencia": ocorrencia}})

    return dicionario_traduzido

def remover_palavras_ocorridas(dicionario, vezes):
    """
    Remove do dicionário palavras que ocorrem menos de um determinado número de vezes.

    Args:
        dicionario (dict): O dicionário contendo as palavras e suas ocorrências.
        vezes (int): O número mínimo de vezes que uma palavra deve ocorrer para ser mantida.

    Returns:
        dict: Um novo dicionário contendo apenas as palavras que ocorrem igual ou mais vezes do que o valor especificado.

    Exemplo de uso:
     dicionario = {'apple': 3, 'banana': 1, 'cherry': 5}
     vezes = 2
     dicionario_filtrado = remover_palavras_ocorridas(dicionario, vezes)
     print(dicionario_filtrado)
    {'apple': 3, 'cherry': 5}
    """
    # Cria um novo dicionário filtrado usando uma compreensão de dicionário
    # Apenas as palavras que ocorrem igual ou mais vezes do que o valor especificado são mantidas
    dicionario_filtrado = {palavra: ocorrencias for palavra, ocorrencias in dicionario.items() if ocorrencias >= vezes}

    return dicionario_filtrado

# URL que você deseja consultar
lista_url=["http://web2py.com/books/default/chapter/29/00/preface",
"http://web2py.com/books/default/chapter/29/01/introduction",
"http://web2py.com/books/default/chapter/29/02/the-python-language",
"http://web2py.com/books/default/chapter/29/03/overview",
"http://web2py.com/books/default/chapter/29/04/the-core",
"http://web2py.com/books/default/chapter/29/05/the-views",
"http://web2py.com/books/default/chapter/29/06/the-database-abstraction-layer",
"http://web2py.com/books/default/chapter/29/07/forms-and-validators",
"http://web2py.com/books/default/chapter/29/08/emails-and-sms",
"http://web2py.com/books/default/chapter/29/09/access-control",
"http://web2py.com/books/default/chapter/29/10/services",
"http://web2py.com/books/default/chapter/29/11/jquery-and-ajax",
"http://web2py.com/books/default/chapter/29/12/components-and-plugins",
"http://web2py.com/books/default/chapter/29/13/deployment-recipes",
"http://web2py.com/books/default/chapter/29/14/other-recipes",
"http://web2py.com/books/default/chapter/29/15/helping-web2py"]

# Processa todas as URLs e atualiza o dicionário global
for url in lista_url:
    conteudo = obter_conteudo_da_url(url)

    if conteudo:
        print(f"Pegou conteúdo de {url}")
        # Analisa o HTML da página
        soup = BeautifulSoup(conteudo, "html.parser")
        texto = soup.get_text()  # Extrai o texto da página

        # Conta as palavras e atualiza o dicionário de contagem global
        contagem_palavras_global += contar_palavras(texto)

# Exemplo de uso:
dicionario_ordenado = ordenar_dicionario_por_ocorrencia(contagem_palavras_global)

# Exemplo de uso:
nome_arquivo = "dicionario_ordenado.json"
dicionario_menos_palavras = remover_palavras_ocorridas(dicionario_ordenado, 50)
dicionario_sem_caract_especial = criar_dicionario_apenas_com_palavras(dicionario_menos_palavras)
dicionario_formatado = traduzir_dicionario(dicionario_sem_caract_especial)



salvar_dicionario_em_arquivo(dicionario_formatado, nome_arquivo)