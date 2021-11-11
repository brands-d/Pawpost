from setuptools import setup
from src.__init__ import __version__

setup(
    name='pawpost',
    version=__version__,
    description='A template for an open-source Python project. ',
    url='https://github.com/brands-d?tab=repositories',
    author='Dominik Brandstetter',
    author_email='dominik.brandstetter@edu.uni-graz.at',
    package_dir={'': 'src'},
    packages=['sub_module'],
    python_requires='>=3.8',
    install_requires=['numpy>=1.20'],
    extras_require={
        'docs': ['sphinx==4.1.2', 'sphinx-rtd-theme==0.5.2'],
        'test': ['pytest==6.2.5', 'flake8==3.9.2'],
        'dev': ['sphinx==4.1.2', 'check-manifest==0.46',
                'twine==3.4.2', 'sphinx-rtd-theme==0.5.2']},
    classifiers=['Topic :: Documentation :: Sphinx',
                 'Natural Language :: English',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.8',
                 'Topic :: Communications :: Email',
                 'Topic :: Scientific/Engineering :: Physics',
                 'Topic :: Software Development :: Version Control :: Git',
                 'Topic :: Text Processing :: Markup :: reStructuredText',
                 'License :: OSI Approved :: MIT License'
                 ]
)
