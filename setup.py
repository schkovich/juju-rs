from setuptools import setup, find_packages

setup(name='juju-rs',
      version="0.0.1",
      classifiers=[
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Operating System :: OS Independent'],
      author='Goran Miskovic',
      author_email='schkovich@gmail.com',
      description="RackSpace integration with juju",
      long_description=open("README.md").read(),
      url='https://github.com/schkovich/juju-rs.git',
      license='BSD',
      packages=find_packages(),
      install_requires=["PyYAML", "requests"],
      tests_require=["nose", "mock"],
      entry_points={
          "console_scripts": [
              'juju-rs = juju_rs.cli:main']},
      )
