import os
import uuid

from pip.req import parse_requirements
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

install_reqs = parse_requirements(os.path.join(here, 'requirements.txt'), session=uuid.uuid1())
reqs = [str(ir.req) for ir in install_reqs]

with open(os.path.join(here, 'README.md')) as fp:
    long_description = fp.read()

setup(
    name='cert-schema',
    version='1.2.16',
    description='tools for working with blockchain certificates',
    author='MIT Media Lab Blockchain Certificates',
    tests_require=['tox'],
    url='https://github.com/blockchain-certificates/cert-schema',
    license='MIT',
    author_email='certs@mit.edu',
    long_description=long_description,
    packages=find_packages(),
    package_data={"cert_schema": ["schema/certificate/1.1/*.json", "schema/certificate/1.2/*.json"]},
    install_requires=reqs
)
