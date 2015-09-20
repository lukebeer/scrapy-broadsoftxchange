# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='scrapy-broadsoftxchange',
    version="1.17",
    description="Download documents and published software from Broadsoft Xchange",
    long_description="",
    keywords='scrapy broadsoft broadworks xchange',
    url='https://github.com/lukebeer/scrapy-broadsoftxchange',
    author='Luke Berezynskyj (Aka Beer)',
    author_email='mail@luke.beer',
    license='MIT',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'distribute',
        'scrapy',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
