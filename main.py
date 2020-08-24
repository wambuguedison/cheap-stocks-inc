import click
import csv

@click.command()
@click.argument('currency', required=True)
def check_currency(currency):
  """Usage

  check_currency 'currency'

  - where currency is the ISO 4217 code

  This command checks whether the currency is supported or not

  check_currency --help

  This command shows how to use this tool
  """
  # Convert ISO code to upper case
  currency = currency.upper()
  # Check where user inputs ISO code in the correct format
  if len(currency) != 3:
    raise click.UsageError(
        'The ISO code is a three-letter alphabetic code '
        'and an equivalent three-digit numeric code'
    )

  # Read the csv file
  with open('Cheap.Stocks.Internationalization.Currencies.csv') as csv_file:
    # Use a python dictionary for easy accessibility of data
    csv_reader = csv.DictReader(csv_file)
    supported = False
    for row in csv_reader:
      if currency == row['ISO 4217 Code']:
        click.echo('{} is supported'.format(row['Country']))
        supported = True

    # Tell the user ISO code is not supported
    if not supported:
      click.echo('The currency - {} is not supported'.format(currency))

if __name__ == "__main__":
  check_currency()
