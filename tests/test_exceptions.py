from pydatagovgr.exceptions import DataGovError, DataGovResponseError


def test_data_gov_error():
    err = DataGovError()

    assert isinstance(err, Exception)


def test_data_gov_response_error():
    err = DataGovResponseError()

    assert isinstance(err, Exception)
