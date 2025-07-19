# Not-So-Quick Usage

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