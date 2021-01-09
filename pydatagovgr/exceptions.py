class DataGovError(Exception):
    """Base class for data.gov.gr exceptions."""


class DataGovResponseError(DataGovError):
    """Error raised when data.gov.gr does not send the expected response."""
