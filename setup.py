"""
    Python Standard Package Setup Configuration file.
"""

from os import path
from setuptools import setup

with open(
        path.join(path.abspath(path.dirname(__file__)), 'README.md'),
        encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='emosent-py',
    packages=['emosent'],
    version='0.1.6',
    license='MIT',
    description='Python module to get Sentiment Rankings for Unicode Emojis.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Fintel Labs Inc.',
    author_email='omkar@fintel.ai',
    url='https://fintel.ai',
    download_url=(
        'https://github.com/FintelLabs/emosent-py/archive/master.zip'
    ),
    keywords=[
        'emoji', 'sentiment', 'analysis', 'ranking', 'emoticon', 'polarity'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    include_package_data=True
)
