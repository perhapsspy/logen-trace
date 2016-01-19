# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = ['suds', 'pytz']


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='logen-trace',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    author='PerhapsSPY',
    author_email='perhapsspy@gmail.com',
    url='https://github.com/perhapsspy/logen-trace',
    description="Delivery confirmation for Logen(https://www.ilogen.com)",
    long_description=readme(),
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
