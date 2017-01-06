import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-log-viewer',
    version='0.1',
    author="InkaLabs",
    packages='log-viewer',
    include_package_data=True,
    license='BSD License',  # example license
    description='A simple Django app to read log files in the admin.',
    long_description=README,
    url='https://bitbucket.org/inkalabsinc/django-log-viewer/',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: X.Y',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
)
