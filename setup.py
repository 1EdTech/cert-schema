import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open('requirements.txt') as f:
    install_reqs = f.readlines()
    reqs = [str(ir) for ir in install_reqs]

with open(os.path.join(here, 'README.md')) as fp:
    long_description = fp.read()

setup(
    name='cert-schema',
    version='2.1.5',
    description='Blockchain certificates JSON-LD context and JSON schemas',
    author='info@blockcerts.org',
    url='https://github.com/blockchain-certificates/cert-schema',
    license='MIT',
    author_email='info@blockcerts.org',
    long_description=long_description,
    packages=find_packages(),
    package_data={"cert_schema": ["1.1/*.json", "1.2/*.json", "2.0-alpha/*.json", "2.0/*.json"]},
    install_requires=reqs
)
