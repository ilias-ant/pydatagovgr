import logging

import requests

from .exceptions import DataGovResponseError


logging.basicConfig()  # you need to initialize logging, otherwise you will not see anything from requests
logging.getLogger().setLevel(logging.CRITICAL)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


class DataGovSession(requests.Session):
    """
    This is a very thin wrapper around the requests Session object which allows
    us to wrap the response handler in order to handle it in a data.gov.gr way.
    """

    @staticmethod
    def _handle_response(response: requests.models.Response):
        """
        Handles the response received from data.gov.gr.
        """
        if not response.ok:
            raise DataGovResponseError(
                f"data.gov.gr error [{response.status_code}]: {response.text}"
            )

        try:
            json_response_content = response.json()

        except ValueError:
            raise DataGovResponseError(
                f"data.gov.gr invalid JSON response: {response.text}"
            )

        return json_response_content

    def request(self, *args, **kwargs):
        """Wraps Session.request and handles the response."""
        response = super(DataGovSession, self).request(*args, **kwargs)

        return self._handle_response(response)
