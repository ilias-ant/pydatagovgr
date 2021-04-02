from typing import Optional

from urllib.parse import urljoin
from urllib3.util.retry import Retry

from .adapters import TimeoutHTTPAdapter
from .session import DataGovSession


class BaseClient(object):
    """This client handles constructing and sending HTTP requests to data.gov.gr.

    Attributes:
        token (str): A string specifying an xoxp or xoxb token.
        base_url (str): A string representing the data.gov.gr base URL.
            Default is 'https://data.gov.gr/api/v1/'.
        timeout (int): The maximum number of seconds the client will will await
            a response to its request from data.gov.gr. The data.gov.gr server can use
            this to ensure that a timely response is generated - *however* this decision
            lies entirely with the data.gov.gr and the client cannot enforce it somehow.
            Defaults to 60 seconds.
        max_retries (int): The maximum number of retries in case of unsuccessful request.
            Defaults to 3.
    """

    BASE_URL = "https://data.gov.gr/api/v1/"

    def __init__(
        self,
        token: Optional[str] = None,
        base_url: str = BASE_URL,
        timeout: int = 60,
        max_retries: int = 3,
    ) -> None:
        self.base_url = base_url
        self.max_retries = max_retries
        self.timeout = timeout
        self.token = None if token is None else token.strip()
        self.headers = self._get_headers()
        self.session = self._init_session()

    def _get_headers(self) -> dict:
        """Constructs the headers need for a request.

        Returns:
            The headers dictionary.
                e.g. {
                    'Authorization': 'Token xoxb-1234-1243',
                }
        """

        return {"Authorization": f"Token {self.token}"}

    def _build_url(self, endpoint: str) -> str:
        """Joins the base data.gov.gr and an `endpoint` to form an absolute URL.

        Args:
            endpoint: The API endpoint.
                e.g. 'query/mdg_emvolio'

        Returns:
            The built URL.
                e.g. 'https://data.gov.gr/api/v1/query/mdg_emvolio'
        """

        return urljoin(self.BASE_URL, endpoint)

    def _init_session(self) -> DataGovSession:
        """Initializes a DataGovSession and adapts several policies.

        Returns:
            The DataGovSession object.
        """
        retry_strategy = Retry(
            total=self.max_retries,
            backoff_factor=2,  # 1, 2, 4, 8, 16, 32, 64, 128, 256, ... seconds
            status_forcelist=[413, 429, 500, 502, 503, 504],
        )
        # initialize custom adapter for retry & timeout policies
        adapter = TimeoutHTTPAdapter(max_retries=retry_strategy, timeout=self.timeout)

        session = DataGovSession()
        session.mount("https://", adapter)
        session.mount("http://", adapter)

        return session
