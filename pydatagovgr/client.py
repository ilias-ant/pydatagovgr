from .base_client import BaseClient


class DataGovClient(BaseClient):
    """A DataGovClient allows apps to communicate with the Hellenic Government's open-data API (data.gov.gr)
    The data.gov.gr API is an interface for querying data published by central government, local authorities
    and public bodies to help you build products and services.

    Note:
        Any attributes or methods prefixed with _underscores are forming a so called
        "private" API, and is for internal use only. They may be changed or removed at anytime.
    """

    def query(self, dataset: str, **kwargs) -> list:
        """Query a `dataset`. Additional (optional) parameters can be specified.

        Args:
            dataset: The name of the dataset.

        Returns:
            The dataset.
        """
        endpoint = f"query/{dataset}"

        url = self._build_url(endpoint)

        return self.session.get(url, params=kwargs, headers=self.headers)
