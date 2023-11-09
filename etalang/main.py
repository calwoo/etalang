import typer


app = typer.Typer(no_args_is_help=True)

@app.command()
def main(path: str, lex: bool = False):
    typer.echo("doing stuff")
