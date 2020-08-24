from setuptools import setup

setup(
  name='check-currency',
  version='0.1',
  py_modules=['check-currency'],
  install_requires=[
      'Click',
  ],
  entry_points='''
      [console_scripts]
      check-currency=main:check_currency
  ''',
)