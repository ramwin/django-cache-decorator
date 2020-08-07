from setuptools import setup

version = '0.5.0'

setup(
    name = 'django3-cache-decorator',
    packages = ['django_cache_decorator'],
    license = 'MIT',
    version = version,
    description = 'Easily add caching to functions within a django project.',
    long_description=open('README.md').read(),
    author = 'Richard Caceres',
    author_email = 'me@rchrd.net',
    url = 'https://github.com/ramwin/django-cache-decorator/',
    download_url = 'https://github.com/ramwin/django-cache-decorator/tarball/' + version,
    keywords = ['django','caching','decorator'],
    classifiers = [],
)
