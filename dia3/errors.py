"""
1. Identificando um erro de sintaxe
print("Olá, mundo!"

Aqui falta fechar o parênteses. Ele lançou um SyntaxError, erro de sintaxe.

Código correto:
"""
print("Olá, mundo")

"""
2. Lidando com um NameError
print(nome)

Aqui o erro é diferente: está sendo pedido para imprimir algo no console, mas esse algo ainda
não foi definido. O programa lançou um NameError

Código correto:
"""
nome = "Pedro"
print(nome)

"""
3. Erro de tipagem (TypeError)
def somar(a, b):
    return a + b

resultado = somar(10, "5")
print(resultado)

Aqui deu um TypeError, pois o Python não consegue somar uma string com um número. 
Código corrigido:
"""
def somar(a, b):
    return float(a) + float(b) # Convertendo para número

"""
4. Corrigindo um erro de índice (IndexError)
numeros = [10, 20, 30]
indice = int(input("Digite um índice para acessar a lista: ")) 

print(numeros[indice])

Há três erros:
Caso o usuário digite um index que não existe (3, por exemplo), o programa lançará um IndexError.
Um segundo erro é que, caso a entrada seja vazia, ele dará um ValueError.
Por fim, se o usuário digitar algo que não é um inteiro, dará erro
Isso pode ser corrigido com um try except
Código corrigido:
"""
try:
    numeros = [10, 20, 30]
    indice = int(input("Digite um índice para acessar a lista: ")) 
    print(numeros[indice])
except Exception as e:
    print('Erro: ', e)

"""
5. Testando múltiplos erros ao mesmo tempo
def dividir(a, b):
    return a / b

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

resultado = dividir(int(num1), int(num2))
print(f"Resultado: {resultado}")

Aqui há três erros: o primeiro é que não há tratamento de erro para a divisão por zero, podendo ocorrer
uma ZeroDivisionError
O segundo é que não há tratamento de tipagem de entrada (se o usuário escrever uma string, dará erro)
O terceiro é, novamente, caso a entrada seja vazia
Também pode ser tratado com um try except

Código corrigido:
"""

def dividir(a, b):
    return a / b

try:
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")

    resultado = dividir(int(num1), int(num2))
    print(f"Resultado: {resultado}")
except Exception as e:
    print('Erro:', e)

"""
6. Erro ao trabalhar com dicionários:
dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}

chave = input("Digite a chave que deseja acessar: ")

print(f"O valor da chave '{chave}' é: {dados[chave]}")

Aqui o erro ocorre quando o usuário digitar uma chave que não existe no dicionário. Pode ser
tratado com um try except, como os outros códigos, ou com o método get(), que pega um valor que está
em uma chave se a chave exister. Se não existir, retorna None

Código corrigido:
"""
dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}

chave = input("Digite a chave que deseja acessar: ")
if dados.get(chave) is not None:
    print(f"O valor da chave '{chave}' é: {dados[chave]}")
else:        
    print("Erro: a chave informada não existe")

"""
7. Exercício 7: Criando um Erro personalizado:
def validar_idade(idade)
    if idade < 0 or idade > 120:
        raise ValueError("A idade deve estar entre 0 e 120 anos!")  # Erro personalizado
    return f"Idade válida: {idade}"

idade = int(input("Digite sua idade: "))
print(validar_idade(idade))

Novamente, aqui faltou a validação se a entrada for um número.
Além disso, há um erro de sintaxe: faltou o dois pontos após a definição da função

Código corrigido:
"""

def validar_idade(idade):
    if idade < 0 or idade > 120:
        raise ValueError("A idade deve estar entre 0 e 120 anos!")  # Erro personalizado
    return f"Idade válida: {idade}"

while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0 or idade > 120:
            print("Erro: idade deve estar entre 0 e 120 anos")
        else:
            print(validar_idade(idade))
            break
    except Exception as e: # Pode tratar tanto entrada que não seja int quanto entrada vazia
        print("Erro: idade não é um número")

"""
8. Debugando um código com múltiplos erros:
def calcular_media(notas):
    soma = sum(notas)
    quantidade = len(notas)
    return soma / quantidade

notas = [8, 9, "10", 7]
media = calcular_media(notas)
print(f"Média: {media:.2f}")

Há vários erros:
Primeiro, é preciso tratar para que exista pelo menos um elemento no array (len > 0) para que não ocorra
divisão por zero.
Segundo, há uma string dentro do array de notas, e python não consegue somar string com números. É
preciso converter para número antes disso
Terceiro, é preciso tratar a exceção caso um dos elementos do array seja uma string

Código corrigido:
"""
def calcular_media(notas):
    if not notas:
        raise ValueError("Erro: a lista de notas está vazia.")
    
    soma = 0
    quantidade = 0

    # Preciso tentar converter manualmente todos os elementos do array para testar se algum deles é inválido
    for nota in notas:
        try:
            numero = float(nota) 
            soma += numero
            quantidade += 1
        except ValueError:
            print(f"Aviso: o valor '{nota}' não é um número válido e será ignorado")

    if quantidade == 0:
        raise ValueError("Erro: nenhuma nota válida")

    return soma / quantidade

notas = [8, 9, "10", 7, "teste"]
media = calcular_media(notas)
print(f"Média: {media:.2f}")