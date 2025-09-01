import random
from dotenv import load_dotenv
from Jogadores import login_jogador, mostrar_ranking, cadastrar_jogador
from Conexao import conectar

load_dotenv()

def jogar(carros):
    carro_escolhido = random.choice(carros)
    print("\n🎮 Novo jogo iniciado!")
    print("Tente adivinhar qual é o carro escolhido. Você terá 4 dicas 😉")
    tentativas = 4

    for i in range(tentativas):
        if i == 0:
            print(f"Dica {i+1}: Marca -> {carro_escolhido['marca']}")
        elif i == 1:
            print(f"Dica {i+1}: Ano de fabricação -> {carro_escolhido['ano']}")
        elif i == 2:
            print(f"Dica {i+1}: Potência -> {carro_escolhido['potencia']} CV")
        elif i == 3:
            print(f"Dica {i+1}: Tipo de carroceria -> {carro_escolhido['carroceria']}")

        resposta = input("Qual carro você acha que é? ").strip()
        if resposta.lower() == carro_escolhido["modelo"].lower():
            print(f"🎉 Parabéns! Você acertou: era o {carro_escolhido['modelo']} 🚗")
            return True
        else:
            print("❌ Errou!")
    else:
        print(f"😢 Suas tentativas acabaram. O carro era {carro_escolhido['modelo']}.")
        return False

def main():
    conexao = conectar()
    if not conexao:
        return

    while True:
        jogador = login_jogador(conexao)
        if jogador:
            break
        print("\nUsuário não encontrado. Deseja cadastrar um novo jogador?")
        opcao = input("Digite 'sim' para cadastrar ou qualquer outra tecla para tentar novamente: ").strip().lower()
        if opcao == 'sim':
            cadastrar_jogador(conexao)

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
        acertou = jogar(carros)
        if acertou:
            cursor.execute("UPDATE jogadores SET pontuacao = pontuacao + 10 WHERE id = %s", (jogador['id'],))
            conexao.commit()
            print("🏅 Você ganhou 10 pontos!")
        jogar_novamente = input("\nGostaria de jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! Até a próxima 🚗")
            mostrar_ranking(conexao)
            break

    cursor.close()
    conexao.close()

if __name__ == "__main__":
    main()
