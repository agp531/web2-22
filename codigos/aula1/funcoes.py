# Funcoes
import datetime

def somar(a, b):
    return a + b

# soma dois ints
res = somar(2, 3)
print("resultado 1:", res)

# soma int e float
res = somar(5, 5.5)
print("resultado 2:", res)

# soma floats
res = somar(4.5, 5.5)
print("resultado3:", res)

# obtem a data e hora atual
data_hoje = datetime.datetime.now()

print(data_hoje)

