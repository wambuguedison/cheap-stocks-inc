import click

@click.command()
@click.argument('currency', required=True)
def check_currency(currency):
  """Usage

  check_currency 'currency'

  - where currency is the ISO 4217 code

  This command checks whether the currency is supported or not

  """
  if len(currency) != 3:
    raise click.UsageError(
        'The ISO code is a three-letter alphabetic code '
        'and an equivalent three-digit numeric code'
    )

if __name__ == "__main__":
  check_currency()
