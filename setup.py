import setuptools

with open('README.md') as file:

    readme = file.read()

name = 'aiocord'

version = '1.1.10'

author = 'Exahilosys'

url = f'https://github.com/{author}/{name}'

download_url = f'{url}/archive/v{version}.tar.gz'

setuptools.setup(
    name = name,
    version = version,
    author = author,
    author_email = 'exahilosys@gmail.com',
    url = url,
    download_url = download_url,
    packages = setuptools.find_packages(),
    license = 'MIT',
    description = 'API wrapper for Discord.',
    long_description = readme,
    long_description_content_type = 'text/markdown',
    include_package_data = True,
    install_requires = [
        'aiohttp',
        'yarl',
        'pynacl'
    ],
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
