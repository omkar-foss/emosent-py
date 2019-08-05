"""
    Python Standard Package Setup Configuration file.
"""

from distutils.core import setup

setup(
    name='emosent-py',
    packages=['emosent'],
    version='0.1.0',
    license='MIT',
    description='Python module to get Sentiment Rankings for Unicode Emojis.',
    author='Fintel Labs Inc.',
    author_email='omkar@fintel.ai',
    url='https://fintel.ai',
    download_url=(
        'https://github.com/FintelLabs/emosent-py/archive/v_01.tar.gz'
    ),
    keywords=[
        'emoji', 'sentiment', 'analysis', 'ranking', 'emoticon', 'polarity'
    ],
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers, Fintech Enthusiasts',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
