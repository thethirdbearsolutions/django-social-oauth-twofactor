#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=7.0',
    'social-auth-app-django',
    'django-two-factor-auth',
    'Django',
    'phonenumbers',
    'django-phonenumber-field',
    'twilio',    
]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Ethan Jucovy",
    author_email='hello@thirdbearsolutions.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Log in to a Django site with social oauth (e.g. Google/Facebook) and optionally enforced two-factor",
    entry_points={
        'console_scripts': [
            'django_social_oauth_two_factor=django_social_oauth_two_factor.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='django_social_oauth_two_factor',
    name='django_social_oauth_two_factor',
    packages=find_packages(include=['django_social_oauth_two_factor', 'django_social_oauth_two_factor.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ejucovy/django_social_oauth_two_factor',
    version='0.1.0',
    zip_safe=False,
)
