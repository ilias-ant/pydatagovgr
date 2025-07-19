# pydatagovgr

[![PyPI](https://img.shields.io/pypi/v/pydatagovgr?color=blue&label=PyPI&logo=PyPI&logoColor=white)](https://pypi.org/project/pydatagovgr/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pydatagovgr?logo=python&logoColor=white)](https://www.python.org/) [![codecov](https://codecov.io/gh/ilias-ant/pydatagovgr/branch/main/graph/badge.svg?token=2H0VB8I8IH)](https://codecov.io/gh/ilias-ant/pydatagovgr) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/ilias-ant/pydatagovgr/ci.yml?branch=main)](https://github.com/ilias-ant/pydatagovgr/actions/workflows/ci.yml) [![Documentation Status](https://readthedocs.org/projects/pydatagovgr/badge/?version=latest)](https://pydatagovgr.readthedocs.io/en/latest/?badge=latest)
 [![PyPI - Wheel](https://img.shields.io/pypi/wheel/pydatagovgr?color=orange)](https://www.python.org/dev/peps/pep-0427/)


A Pythonic client for the official [data.gov.gr](https://data.gov.gr) API. Aims to be an easy, intuitive and 
out-of-the-box way to:

- find data published by central government, local authorities and public bodies of Greece
- build related products and services.

while being robust, following best-practices and eliminating developer-induced bugs.

The aspiration for this library is to enable users of different backgrounds (academia, industry, students etc.) with 
an interest to programmatically explore and utilize the open data of data.gov.gr, to do so without having to 
write-debug-maintain trivial code or worry about that.

## Install

The recommended installation is via `pip`:

```bash
pip install pydatagovgr
```

## Quick Usage

```python
from pydatagovgr import DataGovClient


gov = DataGovClient(token='xoxb-1234-1243')

# fetch public administration evaluation data
evaluation_data = gov.query('public-administration-evaluation')

# you can also download them as CSV
evaluation_csv = gov.query('download/public-administration-evaluation', type='csv')

# or JSON
evaluation_csv = gov.query('download/public-administration-evaluation', type='json')

# fetch the COVID-19 vaccination data
covid_data = gov.query('mdg_emvolio', date_from='2024-01-01', date_to='2021-12-31')

# fetch data on Greece's internet traffic
traffic_data = gov.query('internet_traffic', date_from='2025-06-15', date_to='2025-07-18')

# fetch a list of the forest fires
fire_data = gov.query('mcp_forest_fires', date_from='2017-01-01', date_to='2018-12-31')
```

## Features

The `pydatagovgr` client supports out-of-the-box all the things you know (and love), such as:

- **persistent session**: making several requests to data.gov.gr reuses the same underlying connection.
- **timeout policy**: informs data.gov.gr that it will await at most x seconds for a response for a given request. 
  Defaults to 60 sec.
- **retry policy**: to account for potential server failures of lossy network connections, client automatically retries
  with an exponential-backoff, to avoid harming the data.gov.gr. Defaults to a maximum of 3 retries.

## Not-So-Quick Usage

The data.gov.gr API exposes, through its `api/v1/query` GET endpoint, various **datasets** from different topics.

The `pydatagovgr` client thus provides a corresponding `query` method, through which every available dataset can be obtained. 

- You can also pass additional arguments to filter the results accordingly.
- Some endpoint have required params while others do not.
- If you want to directly download the results as JSON or CSV, add the keyword `download/` before the dataset name e.g. `download/mdg_emvolio` and pass the param `type='json'` or `type='csv'` respectively. 

```python
from pydatagovgr import DataGovClient


gov = DataGovClient()

# fetch the COVID-19 vaccination data for the 2021
sailing_data = gov.query('sailing_traffic', date_from='2025-01-01', date_to='2025-07-18')
```
You can also use Python objects as arguments:

```python
import datetime


data = gov.query(
    'sailing_traffic', 
    date_from=datetime.date(2025, 1, 1),
    date_to=datetime.date(2025, 7, 18)
)
```

Apart from the authentication token, you can also configure the timeout and retry policies of your client. For example: 

```python
# this client will stop waiting for a response after 7 seconds 
gov = DataGovClient(timeout=7)

# this client will retry at most 3 times, with an exponential-backoff
# (i.e. each retry waits exponentially longer before occurs: 1, 2, 4, 8, ...sec)
gov = DataGovClient(max_retries=3)

# this client will respect both a timeout policy and a retry policy
gov = DataGovClient(timeout=7, max_retries=3)
```

## Related Projects

- [go-data-gov-gr-sdk](https://github.com/ppapapetrou76/go-data-gov-gr-sdk): An SDK - written in Go - to access the data.gov.gr API.
- [datagovgR](https://github.com/elenigvasilaki/datagovgR): An R Wrapper Package for the data.gov.gr API.

## How to contribute

If you wish to contribute, [this](CONTRIBUTING.md) is a great place to start!

## License

Distributed under the [MIT License](LICENSE).

## Acknowledgements

All rights are reserved by the official [https://data.gov.gr](https://data.gov.gr) site, its developers, its maintainers and the 
Hellenic Government.
