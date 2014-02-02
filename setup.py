# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='django-textadmin',
    version='0.1.5',
    description='Simple template-based content swapping for CMS-less sites',
    long_description=readme,
    author='Ben Lopatin',
    author_email='ben.lopatin@wellfireinteractive.com',
    url='https://github.com/Visgean/django-textadmin',
    license='BSD License',
    packages=find_packages(exclude=('example', 'docs')),
    platforms=['OS Independent'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires=[
        'Django>=1.5',
    ],
    include_package_data=True,
)
