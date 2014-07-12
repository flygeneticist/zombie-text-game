try:
  from setuptools import setup
except ImportError:
  from disutils.core import setup

config = {
  'name': 'Zombie Text Game',
  'description': 'Survive the zombies and escape from the hosiptal to save your family.',
  'author': 'Kevin Keller',
  'url': 'https:github.com/flygeneticist/zombie-text-game/',
  'download_url': 'https://github.com/flygeneticist/zombie-text-game/archive/master.zip',
  'author_email': 'flygeneticist@gmail.com',
  'version': '0.1',
  'install_requires': [''],
  'packages': ['']
  }

setup(**config)
