# coding: utf-8
import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-info_screen',
    version='0.3',
    description='Django simple info screen application',
    author='Olli-Pekka Puolitaival',
    author_email='oopee1@gmail.com',
    url='https://github.com/OPpuolitaival/django-info_screen',
    download_url='https://github.com/applecat/django-simple-poll/tarball/0.1.1',
    license='MIT',
    long_description=README,
    packages=['info_screen'],
    install_requires=[
    ],
    classifiers=[
        'Framework :: Django',
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Engineering :: Visualization',
    ],
    include_package_data=True,
)