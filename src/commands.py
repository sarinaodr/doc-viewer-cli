from typer import prompt, Typer, FileTextWrite, Option
from constants import SEC_FILE_NAME
from rich import print
from fastapi.commands import fastapi

typer = Typer()


@typer.command()
def init():
    github_personal_token: str = prompt("Enter your github personal token")
    with open(SEC_FILE_NAME, "w") as file:
        file.write(github_personal_token)
    print(
        "[bold green]Success![/bold green] Github personal token has been set successfully! :boom:"
    )


def register_commands(app: Typer):
    app.command()(init)
    app.command()(fastapi)
