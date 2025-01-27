from instagrapi.exceptions import PrivateError
from .utils import console, Panel, Status, Table

def analyze_profile(cl, username):
    with Status(f"[bold blue]Analisando o perfil de @{username}... espreitando os segredos do Instagram...👀\n[/bold blue]\n", spinner="dots") as status:
        try:
            target_user_info = cl.user_info_by_username(username)
            
            if target_user_info.is_private:
                console.print(Panel.fit(
                    f"🔒 [bold yellow]Oops! A conta @{username} é privada.[/bold yellow]\n"
                    "Parece que alguém não quer que bisbilhotemos por aqui... 😅\n",
                    title="Aviso"
                ))
                return
            
            followers = cl.user_followers(target_user_info.pk)
            followers_usernames = {follower.username for follower in followers.values()}
            
            following = cl.user_following(target_user_info.pk)
            following_usernames = {user.username for user in following.values()}
            
            not_following_back = following_usernames - followers_usernames
            not_following_back_count = len(not_following_back)
            
            if not_following_back_count == 0:
                console.print(Panel.fit(
                    f"🎉 [bold green]Uaaaau! Todas as pessoas que @{username} segue também seguem de volta![/bold green]\n"
                    "Parece que todo mundo está na vibe 'seguir de volta'! Será que rolaram biscoitos ou só simpatia? 🍪😄",
                    title="📌 Resultado"
                ))
            else:
                console.print(Panel.fit(
                    f"🔍 [bold]Pessoas que não seguem @{username} de volta:[/bold] {not_following_back_count}\n"
                    "Será que eles estão ocupados demais ou só não gostam de seguidores? 🤔",
                    title="📌 Resultado"
                ))
            
                table_not_following_back = Table(title=f"🚫 Pessoas que não seguem @{username} de volta", show_header=True, header_style="bold magenta", width=80)
                table_not_following_back.add_column("Nº", justify="right", style="cyan", no_wrap=True, min_width=5)
                table_not_following_back.add_column("Usuário", style="yellow", min_width=20)
                
                for i, username in enumerate(not_following_back, start=1):
                    table_not_following_back.add_row(str(i), username)
                
                console.print(table_not_following_back)
            
        except PrivateError as e:
            console.print(Panel.fit(
                f"🔒 [bold yellow]A conta @{username} é privada.[/bold yellow]\n"
                "Parece que alguém não quer que bisbilhotemos por aqui... 😅",
                title="Aviso"
            ))
        except Exception as e:
            console.print(Panel.fit(
                f"❌ [bold red]Erro ao obter informações da conta @{username}:[/bold red] {e}\n"
                "Talvez o Instagram esteja de mal humor hoje... 🤷‍♂️",
                title="Erro"
            ))