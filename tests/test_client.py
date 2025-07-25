import datetime

import pytest
import responses

from pydatagovgr import exceptions


@pytest.fixture
def client():
    from pydatagovgr import client

    return client.DataGovClient()


class TestDataGovClient:
    @staticmethod
    def assert_proper_api_call():
        """Custom assertion method."""

        # assert that a single request was made
        assert len(responses.calls) == 1
        # with the proper headers
        assert responses.calls[0].request.headers["Connection"] == "keep-alive"

    @responses.activate
    def test_query_dataset_invalid_type(self, client):
        expected_body = '{"type":["Το xml δεν είναι έγκυρη επιλογή."]}'

        responses.add(
            responses.GET,
            url="https://data.gov.gr/api/v1/query/mdg_emvolio",
            body=expected_body,
            status=400,
        )

        with pytest.raises(exceptions.DataGovResponseError) as exc:
            client.query("mdg_emvolio", type="xml")

        self.assert_proper_api_call()
        assert "400" in str(exc.value)
        assert expected_body in str(exc.value)

    @responses.activate
    def test_query_dataset_successful(self, client):
        expected_content = [{"foo": "bar"}]

        responses.add(
            responses.GET,
            url="https://data.gov.gr/api/v1/query/mdg_emvolio",
            json=expected_content,
            status=200,
        )

        res = client.query("mdg_emvolio")

        self.assert_proper_api_call()
        assert res == expected_content

    @responses.activate
    def test_query_dataset_successful_with_params(self, client):
        expected_content = [{"foo": "bar"}]

        responses.add(
            responses.GET,
            url="https://data.gov.gr/api/v1/query/mdg_emvolio",
            json=expected_content,
            status=200,
        )

        res = client.query("mdg_emvolio", date_from="2021-01-01", date_to="2021-12-31")

        self.assert_proper_api_call()
        assert res == expected_content
        assert responses.calls[0].request.params == {
            "date_from": "2021-01-01",
            "date_to": "2021-12-31",
        }

    @responses.activate
    def test_query_dataset_successful_with_pythonic_params(self, client):
        expected_content = [{"foo": "bar"}]

        responses.add(
            responses.GET,
            url="https://data.gov.gr/api/v1/query/mdg_emvolio",
            json=expected_content,
            status=200,
        )

        res = client.query(
            "mdg_emvolio",
            date_from=datetime.date(2021, 1, 1),
            date_to=datetime.date(2021, 12, 31),
        )

        self.assert_proper_api_call()
        assert res == expected_content
        assert responses.calls[0].request.params == {
            "date_from": "2021-01-01",
            "date_to": "2021-12-31",
        }

    @responses.activate
    def test_query_dataset_invalid_json_content(self, client):
        responses.add(
            responses.GET,
            url="https://data.gov.gr/api/v1/query/mdg_emvolio",
            body="this-aint-json",  # response.json() will fail
            status=200,
        )

        with pytest.raises(exceptions.DataGovResponseError) as exc:
            client.query("mdg_emvolio")

        self.assert_proper_api_call()
        assert "invalid JSON response" in str(exc.value)

    @responses.activate
    def test_query_dataset_csv_type(self, client):
        expected_body = "."

        responses.add(
            responses.GET,
            url="https://data.gov.gr/api/v1/query/download/public-administration-evaluation?type=csv",
            body=expected_body,
            status=200,
        )

        res = client.query("download/public-administration-evaluation", type="csv")

        assert res.content == bytes(expected_body, 'utf-8')
