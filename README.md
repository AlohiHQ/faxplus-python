# FAX.PLUS Python SDK

<p>
  <h4>Made for third-party developers and organizations to send and receive faxes from their own software or application.</h4>
  <p>
    <a href="#"><img src="https://img.shields.io/pypi/v/faxplus-api?style=flat-square" alt="NPM version"></img></a>
    <img src="https://img.shields.io/badge/license-MIT-green.svg?style=flat-square" alt="License">
  </p>
</p>

<p>
  <a href="https://apidoc.fax.plus" target="_blank">API Documentation</a>  •
  <a href="https://www.fax.plus" target="_blank">Home</a>  •
  <a href="https://www.fax.plus/help/" target="_blank">Help Center</a>  •
  <a href="https://www.fax.plus/contact-us/" target="_blank">Contact Us</a>
</p>

- Only available to [Enterprise](https://www.fax.plus/pricing/) clients

## Requirements.

Python 3.5+

## Installation
### pip install

To install the package from PyPi

```sh
# From PyPi
pip install faxplus-api

# Directly from Github
pip install git+https://github.com/alohi/faxplus-python.git
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
git clone https://github.com/alohi/faxplus-python.git
cd faxplus-python
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

## Getting Started

Example usage:

```python
from faxplus import ApiClient, FaxesApi

client = ApiClient(configuration)
api = FaxesApi()
faxes = api.list_faxes("self", category=FaxCategory.INBOX)
```

## Documentation
Visit the full API reference at [apidoc.fax.plus](https://apidoc.fax.plus).

## Author
© 2022 Alohi (Geneva, Switzerland) - [Alohi.com](https://alohi.com)
