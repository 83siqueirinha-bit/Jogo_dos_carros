import mysql.connector
import random
from dotenv import load_dotenv
import os

load_dotenv()

conexao = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
)

cursor = conexao.cursor(dictionary=True)
cursor.execute("SELECT * FROM carros")
carros = cursor.fetchall()
carro_escolhido = random.choice(carros)

print("🎮 Bem-vindo ao jogo de adivinhação de carros!")
print("Tente adivinhar qual é o carro escolhido. Você terá 4 dicas 😉")

tentativas = 4

for i in range(tentativas):
    if i == 0:
        print(f"Dica {i+1}: Ano de fabricação -> {carro_escolhido['ano']}")
    elif i == 1:
        print(f"Dica {i+1}: Marca -> {carro_escolhido['marca']}")
    elif i == 2:
        print(f"Dica {i+1}: Potência -> {carro_escolhido['potencia']}")
    elif i == 3:
        print(f"Dica {i+1}: Tipo de carroceria -> {carro_escolhido['carroceria']}")

    resposta = input("Qual carro você acha que é? ")

    if resposta.lower() == carro_escolhido["modelo"].lower():
        print(f"🎉 Parabéns! Você acertou: era o {carro_escolhido['modelo']} 🚗")
        break
    else:
        print("❌ Errou!")
else:
    print(f"😢 Suas tentativas acabaram. O carro era {carro_escolhido['modelo']}.")

cursor.close()
conexao.close()