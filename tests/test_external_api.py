from unittest.mock import Mock, patch

from src.external_api import convert_to_rubles


def test_convert_to_rubles_rub():
    transaction = {
        "operationAmount": {
            "amount": "1000",
            "currency": {"code": "RUB"}
        }
    }

    assert convert_to_rubles(transaction) == 1000.0


@patch("src.external_api.os.getenv")
@patch("src.external_api.requests.get")
def test_convert_to_rubles_usd(mock_get, mock_getenv):
    mock_getenv.return_value = "FAKE_API_KEY"

    fake_response = Mock()
    fake_response.json.return_value = {"result": 9200.0}
    fake_response.raise_for_status.return_value = None

    mock_get.return_value = fake_response

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }

    assert convert_to_rubles(transaction) == 9200.0

    mock_get.assert_called_once()
