from setuptools import setup, find_packages


setup(
    name='scrapekit',
    version='0.0.1',
    description="Light-weight tools for web scraping",
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='web scraping crawling http cache threading',
    author='Friedrich Lindenberg',
    author_email='friedrich@pudo.org',
    url='http://github.com/pudo/scrapekit',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'test']),
    namespace_packages=[],
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        "requests>=2.3.0"
    ],
    tests_require=[],
    entry_points={
        'console_scripts': []
    }
)
