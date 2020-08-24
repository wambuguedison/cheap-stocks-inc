from click.testing import CliRunner
from main import check_currency

def test_check_currency():
  runner = CliRunner()
  result = runner.invoke(check-currency, ['XAFsad'])
  assert result.exit_code == 1
  assert result.output == 'The ISO code is a three-letter alphabetic code'
        'and an equivalent three-digit numeric code'