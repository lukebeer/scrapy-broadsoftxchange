from setuptools import setup, find_packages

setup(
    name='broadsoftxchange',
    version='1.4',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = broadsoftxchange.settings']},
)
