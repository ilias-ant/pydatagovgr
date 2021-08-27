# Quick Usage

You must have an account on [data.gov.gr](https://data.gov.gr) to use the API service. In order to register and request
an API token, submit a request in the designated official form [here](https://data.gov.gr/token/). The procedure is very 
simple and takes less than 5 minutes.

```python
from pydatagovgr import DataGovClient


gov = DataGovClient(token='xoxb-1234-1243')

# fetch the COVID-19 vaccination data
covid_data = gov.query('mdg_emvolio')

# fetch data on Greece's internet traffic
traffic_data = gov.query('internet_traffic')

# fetch a list of the forest fires
fire_data = gov.query('mcp_forest_fires')
```