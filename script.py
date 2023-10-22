import itertools
import random
import string

# Solicita ao usuário os dados necessários
nome = input("Informe o nome: ")
data_nascimento = input("Informe a data de nascimento (DDMMYYYY): ")
ano_atual = input("Informe o ano atual: ")
familiares = input("Informe nomes de familiares (separados por vírgula): ")
usar_caracteres_especiais = input("Incluir caracteres especiais? (S/N): ").strip().lower() == "s"
tamanho_senha = int(input("Quantidade de caracteres por senha na wordlist: "))
nome_arquivo = input("Nome do arquivo de saída (ex: wordlist.txt): ")

# Define os caracteres especiais
caracteres_especiais = "!@#$%^&*()_+-=[]{}|;:,.<>?/\\"

# Gera a wordlist
wordlist = []

def criar_senha(variacoes, tamanho):
    senha = []
    todas_variacoes = ''.join(variacoes)
    for _ in range(tamanho):
        caracter = random.choice(todas_variacoes)
        senha.append(caracter)
    return ''.join(senha)

# Combina todas as variações de caracteres
todas_variacoes = nome + nome.lower() + nome.upper() + nome.capitalize() + \
    nome.replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0') + \
    data_nascimento + data_nascimento[4:] + data_nascimento[:4] + data_nascimento[::-1] + \
    ano_atual + ano_atual[2:] + ano_atual[1:] + str(int(ano_atual) - 1) + str(int(ano_atual) + 1) + \
    ''.join(familiares)

if usar_caracteres_especiais:
    todas_variacoes += caracteres_especiais

# Cria senhas misturadas
for _ in range(5000):  # Quantidade de senhas a serem geradas (ajuste conforme necessário)
    senha = criar_senha(todas_variacoes, tamanho_senha)
    wordlist.append(senha)

# Salva a wordlist em um arquivo de texto
with open(nome_arquivo, "w") as arquivo:
    for senha in wordlist:
        arquivo.write(senha + "\n")

print(f"Wordlist criada e salva em {nome_arquivo}.")
