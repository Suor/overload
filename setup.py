from setuptools import setup

setup(
    name='p2-overload',
    version='0.1',
    author='Alexander Schepanovski',
    author_email='suor.web@gmail.com',

    description='Overload python 2 functions with decorator.',
    long_description=open('README.rst').read(),
    url='http://github.com/Suor/overload',
    license='BSD',

    py_modules=['overload'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
