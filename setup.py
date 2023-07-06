"""
    Python Standard Package Setup Configuration file.
"""

from os import path
from setuptools import setup

with open(
        path.join(path.abspath(path.dirname(__file__)), 'README.md'),
        encoding='utf-8'
    ) as readme_file:
    LONG_DESCRIPTION = readme_file.read()

setup(
    name='emosent-py',
    packages=['emosent'],
    version='0.1.7',
    license='MIT',
    description='Python module to get Sentiment Rankings for Unicode Emojis.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Omkar P',
    url='https://github.com/omkar-foss/emosent-py',
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
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    include_package_data=True
)
