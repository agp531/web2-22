# Lê informacao do usuario:
nome = input("Digite seu nome: ")

print("Seja bem vindo", nome)

# declara variavel idade, lê entrada digitada pelo usuário e converte para int
idade = int(input("Qual a sua idade: "))

if idade >= 18:
    print(f'acesso liberado > idade: {idade}')
else:
    print('acesso negado')

