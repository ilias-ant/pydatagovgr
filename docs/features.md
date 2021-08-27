# Features

The `pydatagovgr` client supports out-of-the-box all the things you know (and love), such as:

- **authentication**: properly handles the authentication to data.gov.gr - all you have to do is provide a valid token. 
- **persistent session**: making several requests to data.gov.gr reuses the same underlying connection.
- **timeout policy**: informs data.gov.gr that it will await at most x seconds for a response for a given request. 
  Defaults to 60 sec.
- **retry policy**: to account for potential server failures of lossy network connections, client automatically retries
  with an exponential-backoff, to avoid harming the data.gov.gr. Defaults to a maximum of 3 retries.
