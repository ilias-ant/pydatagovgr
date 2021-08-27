# Not-So-Quick Usage

The data.gov.gr API exposes, through its `api/v1/query` GET endpoint, various **datasets** from different topics.

The `pydatagovgr` client thus provides a corresponding `query` method, through which every available dataset can be obtained.
You can also pass additional arguments to filter the results accordingly. 

```python
from pydatagovgr import DataGovClient


gov = DataGovClient(token='xoxb-1234-1243')

# fetch the COVID-19 vaccination data for the 2021
data = gov.query('mdg_emvolio', date_from='2021-01-01', date_to='2021-12-31')
```
You can also use Python objects as arguments:

```python
import datetime


data = gov.query(
    'mdg_emvolio', 
    date_from=datetime.date(2021, 1, 1), 
    date_to=datetime.date(2021, 12, 31)
)
```

Apart from the authentication token, you can also configure the timeout and retry policies of your client. For example: 

```python
# this client will stop waiting for a response after 7 seconds 
gov = DataGovClient(token='xoxb-1234-1243', timeout=7)

# this client will retry at most 3 times, with an exponential-backoff
# (i.e. each retry waits exponentially longer before occurs: 1, 2, 4, 8, ...sec)
gov = DataGovClient(token='xoxb-1234-1243', max_retries=3)

# this client will respect both a timeout policy and a retry policy
gov = DataGovClient(token='xoxb-1234-1243', timeout=7, max_retries=3)
```