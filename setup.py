from setuptools import setup

setup(name='covid19-stats',
      version='0.0.1',
      description='Python wrapper functions for retrieving real-time and past information from JHU CSSE database',
      url='https://github.com/chinokenochkan/covid19_stats',
      author='Chi Nok Enoch Kan',
      author_email='kanxx030@gmail.com',
      license='MIT',
      packages=['covid19-stats'],
      install_requires=[
          'pydicom','numpy','matplotlib','scipy','Pillow'
      ],
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
      ],
      zip_safe=False)