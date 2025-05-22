from setuptools import setup, find_packages

setup(
    name='cryodatabot',  
    version='0.1.0', 
    description='A Python package for data generation and processing in cryo-EM.',  
    author='qibo,minrui', 
    author_email='your.email@example.com', 
    url='https://github.com/t00shadow/CryoDataBot',  
    packages=find_packages(), 
    include_package_data=True,
    install_requires=[
        'numpy',
        'scipy',
        'pandas',
        'matplotlib',
        'PyQt5'
    ],
    entry_points={
        'console_scripts': [
        #    'cryodatabot=__main__:main'
           'cryodatabot=cryodatabot.main_gui:main'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6', 
)
