def cadastrar_jogador(conexao):
    cursor = conexao.cursor()

    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    usuario = input("Nome de usuário: ")
    email = input("Email: ")

    try:
        cursor.execute(
            "INSERT INTO jogadores (nome, sobrenome, usuario, email) VALUES (%s, %s, %s, %s)",
            (nome, sobrenome, usuario, email)
        )
        conexao.commit()
        print("✅ Jogador cadastrado com sucesso!")
    except Exception as e:
        print("❌ Erro ao cadastrar:", e)

def login_jogador(conexao):
    cursor = conexao.cursor(dictionary=True)
    usuario = input("Digite seu usuário: ")

    cursor.execute("SELECT * FROM jogadores WHERE usuario = %s", (usuario,))
    jogador = cursor.fetchone()

    if jogador:
        print(f"🎮 Bem-vindo de volta, {jogador['nome']} {jogador['sobrenome']}!")
        return jogador
    else:
        print("❌ Usuário não encontrado.")
        return None

def mostrar_ranking(conexao):
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT usuario, pontuacao FROM jogadores ORDER BY pontuacao DESC LIMIT 10")
    ranking = cursor.fetchall()

    print("\n🏆 Ranking dos Jogadores:")
    for i, player in enumerate(ranking, start=1):
        print(f"{i}. {player['usuario']} - {player['pontuacao']} pontos")
