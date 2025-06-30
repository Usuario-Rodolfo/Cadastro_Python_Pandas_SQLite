import pandas as pd

paises = ['Irã', 'Rússia', 'EUA', 'Brasil']
populacoes = [85.03, 144.4, 331.0, 213.0]

df = pd.DataFrame({
    'País': paises,
    'População (milhões)': populacoes
})

print("DataFrame completo:")
print(df)

print("\nColuna 'País':")
print(df['País'])

print("\nTipo do objeto df:", type(df))

# Criar DataFrame para nova linha
nova_linha = pd.DataFrame([{'País': 'Japão', 'População (milhões)': 125.8}])

# Usar concat para adicionar linha
df = pd.concat([df, nova_linha], ignore_index=True)

print("\nDataFrame após adicionar o Japão:")
print(df)

# Remover a linha com país 'Rússia'
df = df[df['País'] != 'Rússia']

print("\nDataFrame após remover a Rússia:")
print(df)