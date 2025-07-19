# Quick Usage

```python
from pydatagovgr import DataGovClient


gov = DataGovClient()

# fetch public administration evaluation data
evaluation_data = gov.query('public-administration-evaluation')

# you can also download them as CSV
evaluation_csv = gov.query('download/public-administration-evaluation', type='csv')

# or JSON
evaluation_json = gov.query('download/public-administration-evaluation', type='json')

# fetch the COVID-19 vaccination data
covid_data = gov.query('mdg_emvolio', date_from='2024-01-01', date_to='2021-12-31')

# fetch data on Greece's internet traffic
traffic_data = gov.query('internet_traffic', date_from='2025-06-15', date_to='2025-07-18')

# fetch a list of the forest fires
fire_data = gov.query('mcp_forest_fires', date_from='2017-01-01', date_to='2018-12-31')
```