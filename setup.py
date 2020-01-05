from distutils.core import setup
setup(
  name = 'zpytrading',
  packages = ['zpytrading'],
  version = '0.1',
  license='MIT',
  description = 'Zinnion Streaming / Trading SDK',
  author = 'Mauro Delazeri',
  author_email = 'mauro@zinnion.com',
  url = 'https://github.com/Zinnion/zpytrading',
  download_url = 'https://github.com/Zinnion/zpytrading/archive/ztrading-0_0_1.tar.gz',
  keywords = ['zpytrading','zinnion','sdk','api'],
  install_requires=[
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 4 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)