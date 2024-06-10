from setuptools import setup, find_packages

setup(name='ip_adapter',
      version='0.1',
      description='implementation of the IPAdapter models for HF Diffusers',
      author='cubiq',
      url='https://github.com/cubiq/Diffusers_IPAdapter',
      packages=find_packages(where='.'),
      package_dir={"": "."}
)
