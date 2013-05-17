from distutils.core import setup

setup(
    name='GSoc Honeynet Test',
    version='0.1.0',
    author='Akshit Agarwal',
    author_email='akshit.jiit@gmail.com',
    scripts=['server.py','client.py'],
    url='http://pypi.python.org/pypi/TowelStuff/',
    description='Client Server Simple Program.',
    long_description=open('README.md').read(),
)
