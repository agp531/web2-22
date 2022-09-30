# Declara uma lista de números:
notas = [5, 8, 9, 10]

# for "amigável" (não necessário contador e índice) 
# "syntax sugar" do python
for n in notas:
    print(n)

# python é fracamente tipado. Permite uma lista com tipos diferentes:
items = ['A', 8, 'C', 10]
for n in items:
    print(n)

