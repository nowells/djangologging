from setuptools import setup, find_packages
 
setup(
    name='django-logging',
    version='0.1.0',
    description="A Django wrapper to Python's logging module",
    author='Fraser Nevett',
    author_email='frasern@gmail.com',
    url='http://code.google.com/p/django-logging/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
