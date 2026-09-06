def texto_estilizado():
    ESTILOS = {
        "vermelho": "\033[91m",
        "verde": "\033[92m",
        "amarelo": "\033[93m",
        "azul": "\033[94m",
        "magenta": "\033[95m",
        "ciano": "\033[96m",
        "negrito": "\033[1m",
        "sublinhado": "\033[4m",
        "resetar": "\033[0m"
    }

    arte = f"""{ESTILOS['ciano']}{ESTILOS['negrito']}
  _____       _   _
 |  __ \     | | | |
 | |__) |   _| |_| |__   ___  _ __
 |  ___/ | | | __| '_ \ / _ \| '_ \
 | |   | |_| | |_| | | | (_) | | | |
 |_|    \__, |\__|_| |_|\___/|_| |_|
         __/ |
        |___/
{ESTILOS['resetar']}"""

    print(arte)
    print(f"{ESTILOS['verde']}>> Bem-vindo ao mundo do código colorido! <<{ESTILOS['resetar']}\n")

    print(f"{ESTILOS['negrito']}Veja o que dá para fazer nativamente no terminal:{ESTILOS['resetar']}")
    print(f"{ESTILOS['vermelho']}* Este texto é vermelho.{ESTILOS['resetar']}")
    print(f"{ESTILOS['amarelo']}* Este texto é amarelo.{ESTILOS['resetar']}")
    print(f"{ESTILOS['magenta']}{ESTILOS['sublinhado']}* Este texto é magenta e sublinhado!{ESTILOS['resetar']}")
    print(f"{ESTILOS['azul']}{ESTILOS['negrito']}* E este é azul e em negrito.{ESTILOS['resetar']}\n")

    print(f"{ESTILOS['ciano']}Dica: A mágica acontece graças aos códigos de escape ANSI! 🚀{ESTILOS['resetar']}")

def exibir_menu():
    menu = """
=====================================
Olá escolha a opção que deseja fazer!
=====================================
[A] Novo Jogo
[B] Carregar Jogo
[C] Sair
"""
    print(menu)

    opcao = input('Digite a opção desejada: ').strip().upper()

    match opcao:
            case 'A':
                texto_estilizado()
            case 'B':
                print("Carregando jogo...")
            case 'C':
                print("Saindo do jogo...")
            case _:
                print("Opção inválida! Tente A, B ou C.")

if __name__ == "__main__":
    exibir_menu()