from setuptools import setup

setup(
    name='Game Stats REST API',
    version='0.1.0',
    author='Jugal Bilimoria',
    description="A RESTful API which allows users to track and store game player data.",
    url='https://github.com/JugalBili/Game-Stats-API',
    license='license.txt',
    long_description=open('README.md').read(),
    install_requires=[
        "dnspython==2.1.0"
        "flask==1.1.2"
        "pymongo==3.11.3"
        "python-dotenv==0.15.0"
    ],
    python_requires='>=3.6',
)