import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="API REST GildedRose",
    version="0.0.1",
    author="dfleta",
    author_email="gelpiorama@gmail.com",
    description="API REST Flask example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dfleta/api-rest-gildedrose.git",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'aniso8601==8.0.0',
        'astroid==2.3.3',
        'Click==7.0',
        'dnspython==1.16.0',
        'Flask==1.1.1',
        'Flask-Cors==3.0.9',
        'flask-mongoengine==0.9.5',
        'Flask-PyMongo==2.3.0',
        'Flask-RESTful==0.3.7',
        'Flask-WTF==0.14.2',
        'isort==4.3.21',
        'itsdangerous==1.1.0',
        'Jinja2==2.11.3',
        'lazy-object-proxy==1.4.3',
        'MarkupSafe==1.1.1',
        'mccabe==0.6.1',
        'mongoengine==0.19.1',
        'pkg-resources==0.0.0',
        'pycodestyle==2.5.0',
        'pylint==2.4.4',
        'pymongo==3.10.1',
        'pytz==2019.3',
        'six==1.14.0',
        'typed-ast==1.4.0',
        'Werkzeug==1.0.0',
        'wrapt==1.11.2',
        'WTForms==2.2.1',
    ],
)
