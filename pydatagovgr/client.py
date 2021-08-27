from typing import Any

from .base_client import BaseClient


class DataGovClient(BaseClient):
    """A `DataGovClient` allows apps to communicate with the Hellenic Government's open-data API (data.gov.gr)
    The data.gov.gr API is an interface for querying data published by central government, local authorities
    and public bodies to help you build products and services.

    **Note**: Any attributes or methods prefixed with _underscores are forming a so called "private" API, and is
    for internal use only. They may be changed or removed at anytime.

    Example:

        >>> from pydatagovgr import DataGovClient
        >>> gov = DataGovClient(token='xoxb-1234-1243')

    """

    def query(self, dataset: str, **kwargs: Any) -> list:
        """Query a `dataset`. Additional (optional) parameters can be specified.

        Example:
            >>> # fetch the COVID-19 vaccination data
            >>> covid_data = gov.query('mdg_emvolio')
            >>> # fetch data on Greece's internet traffic
            >>> traffic_data = gov.query('internet_traffic')
            >>> # fetch a list of the forest fires
            >>> fire_data = gov.query('mcp_forest_fires')

        Args:
            dataset: The name of the dataset.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            The dataset.

        Raises:
            DataGovResponseError: Error raised when data.gov.gr does not send the expected response.
        """
        url = self._build_url(f"query/{dataset}")

        return self.session.get(url, params=kwargs, headers=self.headers)
