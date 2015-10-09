#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        raise SystemExit(errno)


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')


install_requires = set(x.strip() for x in open('requirements.txt'))
install_requires_replacements = {
    'https://github.com/ethereum/pyrlp/tarball/develop#egg=rlp': 'rlp>=0.3.9',
    'https://github.com/ethereum/pydevp2p/tarball/develop#egg=devp2p': 'devp2p>=0.5.2',
    'https://github.com/ethereum/pyethereum/tarball/develop#egg=ethereum': 'ethereum>=1.0.5',
    'https://github.com/ethereum/ethash/tarball/master#egg=pyethash': 'pyethash'}

install_requires = [install_requires_replacements.get(r, r) for r in install_requires]

test_requirements = ['ethereum-serpent>=1.8.1']

version = '1.0.6'  # preserve format, this is read from __init__.py

setup(
    name='pyethapp',
    version=version,
    description="Python Ethereum Client",
    long_description=readme + '\n\n' + history,
    author="HeikoHeiko",
    author_email='heiko@ethdev.com',
    url='https://github.com/ethereum/pyethapp',
    packages=[
        'pyethapp',
    ],
    package_data={
        'pyethapp': ['data/*.json']
    },
    license="BSD",
    zip_safe=False,
    keywords='pyethapp',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
    cmdclass={'test': PyTest},
    install_requires=install_requires,
    tests_require=test_requirements,
    entry_points='''
    [console_scripts]
    pyethapp=pyethapp.app:app
    '''
)
