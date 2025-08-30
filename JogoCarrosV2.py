import mysql.connector
import random
from dotenv import load_dotenv
import os

load_dotenv()

def conectar():
    try:
        conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
        )
        return conexao
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None

def jogar(carros):
    carro_escolhido = random.choice(carros)
    print("\n🎮 Novo jogo iniciado!")
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

        resposta = input("Qual carro você acha que é? ").strip()
        if resposta.lower() == carro_escolhido["modelo"].lower():
            print(f"🎉 Parabéns! Você acertou: era o {carro_escolhido['modelo']} 🚗")
            break
        else:
            print("❌ Errou!")
    else:
        print(f"😢 Suas tentativas acabaram. O carro era {carro_escolhido['modelo']}.")

def main():
    conexao = conectar()
    if not conexao:
        return

    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM carros")
    carros = cursor.fetchall()
    if not carros:
        print("Nenhum carro cadastrado no banco de dados.")
        cursor.close()
        conexao.close()
        return

    print("🎮 Bem-vindo ao jogo de adivinhação de carros!")
    while True:
        jogar(carros)
        jogar_novamente = input("\nGostaria de jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! Até a próxima 🚗")
            break

    cursor.close()
    conexao.close()

if __name__ == "__main__":
    main()