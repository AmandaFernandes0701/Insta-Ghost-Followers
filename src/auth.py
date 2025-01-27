import os
import logging
from instagrapi import Client
from instagrapi.exceptions import ChallengeRequired, LoginRequired
from dotenv import load_dotenv
from .utils import console, Panel, Status


load_dotenv()

def login_to_instagram():
    logging.disable(logging.CRITICAL)

    with Status("[bold blue]Aguarde, não saia daí! Estamos executando o login... 🕵️‍♂️🔍\n\n[/bold blue]", spinner="dots") as status:

        cl = Client()
        cl.logger.setLevel(logging.CRITICAL)

        your_username = os.getenv('INSTAGRAM_USERNAME')
        your_password = os.getenv('INSTAGRAM_PASSWORD')

        try:
            cl.login(your_username, your_password)
            console.print(Panel.fit("✅ [bold green]Login realizado com sucesso![/bold green]", title="Instagram"))
            return cl
        except ChallengeRequired as e:
            console.print(Panel.fit("🔒 [bold red]Desafio de segurança detectado.[/bold red]\nPor favor, verifique sua conta no aplicativo do Instagram.", title="Erro"))
            return None
        except LoginRequired as e:
            console.print(Panel.fit(f"❌ [bold red]Erro ao fazer login:[/bold red] {e}", title="Erro"))
            return None
        except Exception as e:
            error_message = str(e)
            wrapped_message = "\n".join([error_message[i:i+80] for i in range(0, len(error_message), 80)])
            console.print(Panel.fit(f"❌ [bold red]Erro inesperado ao fazer login:[/bold red]{wrapped_message}", title="Erro"))
            return None