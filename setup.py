try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

# here = path.abspath(path.dirname(__file__))

# with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
#   long_description = f.read()

setup(
    name = 'address-terminal',
    version = '0.1',
    description = 'My Project Test',
    #long_description = 'I need to input a README',
    url = 'DoesNotExistYet',
    author = 'David Capella',
    author_email = 'D_Capella@yahoo.com',
    #license = ''
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2.7.10',
    ],
    keywords = 'programming testing basic',
    packages = ['testing_project'],
    # packages = find_packages(exclude=['tests', 'docs']),
    # py_modules = [""]
    # install_requires = ['peppercorn'],
    # extras_require = {
    #   'dev': ['check-manifest'],
    #   'tet': ['coverage'],
    # },
    # package_data = {
    #     'sample': ['package_data.dat'],
    # },
    # data_files=[('my_data', ['data/data_file'])],
    entry_points = {
        'bin': [
            'sample = sample:first_bin',
        ],
    },
)



# config = {
#     'description': 'My Project Test',
#     'author': 'David Capella',
#     'url': 'URL to get it at.',
#     'download_url': 'Where to download it.',
#     'author_email': 'D_Capella@yahoo.com',
#     'version': '0.1',
#     'install_requires': ['nose'],
#     'packages': ['testing_project', 'testing_project.first'],
#     'scripts': ['first_bin'],
#     'name': 'testing_project'
# }
