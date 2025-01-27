import logging
from dotenv import load_dotenv
from src import login_to_instagram, analyze_profile, console, Panel

load_dotenv()

logging.basicConfig(level=logging.CRITICAL, filename='logs/app.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    cl = login_to_instagram()
    if not cl:
        return

    while True:
        console.print(Panel.fit(
            "[bold magenta] Ei, Sherlock![/bold magenta] Qual perfil você quer investigar hoje?"
            "\nDigite o nome de usuário abaixo (e não se preocupe, não vamos contar pra ninguém!)",
            title="🔍 Modo Detetive Ativado"
        ))

        target_username = console.input("👉 [bold cyan]Nome do perfil: [/bold cyan]").strip()

        analyze_profile(cl, target_username)

        continuar = console.input("🔍 [bold cyan]Quer analisar outro perfil? (sim/não): [/bold cyan]").strip().lower()
        if continuar not in ["sim", "s", "yes", "y"]:
            console.print(Panel.fit("👋 [bold green]Até a próxima, detetive![/bold green]", title="Finalizando"))
            break

if __name__ == "__main__":
    main()