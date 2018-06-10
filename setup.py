# coding: utf-8
from setuptools import setup, find_packages

NAME = "faxplus-api"
VERSION = "0.3"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="FAX.PLUS REST API",
    author="faxplus",
    author_email="info@fax.plus",
    url="https://github.com/alohi/faxplus-python",
    keywords=["faxplus", "fax.plus", "alohi"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Fax",
    ],
    long_description="""\
    This is the fax.plus API v1 developed for third party developers and organizations. In order to have a better coding experience with this API, let's quickly go through some points:
    - This API assumes **/accounts** as an entry point with the base url of **https://restapi.fax.plus/v1**.
    - This API treats all date and times sent to it in requests as **UTC**. Also, all dates and times returned in responses are in **UTC**
    - Once you have an access_token, you can easily send a request to the resource server with the base url of **https://restapi.fax.plus/v1** to access your permitted resources. As an example to get the user's profile info you would send a request to **https://restapi.fax.plus/v1/accounts/self** when **Authorization** header is set to "Bearer YOUR_ACCESS_TOKEN" and custom header of **x-fax-clientid** is set to YOUR_CLIENT_ID
    """
)
