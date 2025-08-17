# Criando bytes a partir de uma string
texto = "Olá, mundo!"
dados_bytes = texto.encode('utf-8')  # Converte a string em bytes usando UTF-8
print(dados_bytes)  # Saída: b'Ol\xc3\xa1, mundo!'

# Criando bytes diretamente com b''
dados_bytes2 = b'Hello World'
print(dados_bytes2)  # Saída: b'Hello World'

# Criando bytes a partir de uma lista de inteiros (0-255)
lista = [65, 66, 67, 68]  # Valores ASCII
dados_bytes3 = bytes(lista)
print(dados_bytes3)  # Saída: b'ABCD'

# Escrevendo bytes num arquivo
with open('arquivo_bytes.bin', 'wb') as f:
    f.write(dados_bytes)
    f.write(dados_bytes2)
    f.write(dados_bytes3)
