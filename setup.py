from setuptools import setup, find_packages


setup(name='python-battlerite',
      version='0.1',
      author='Drew Monroe',
      author_email='d.monroe@snet.net',
      description='A wrapper around the Battlerite REST API',
      url='https://github.com/DrewMonroe/python-battlerite',
      license='MIT',
      packages=find_packages(),
      install_requires=['requests==2.18.4'],
      keywords=['battlerite']
      )
