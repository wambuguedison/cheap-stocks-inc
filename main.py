import click

@click.command()
@click.argument('currency', required=True)
def cli_app(currency):
  """This is a testing help"""
  click.echo("testing " + currency)

if __name__ == "__main__":
  cli_app()
