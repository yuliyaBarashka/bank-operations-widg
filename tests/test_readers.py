from unittest.mock import patch
import pandas as pd
from src.readers import read_transactions_from_csv, read_transactions_from_excel


@patch("pandas.read_csv")
def test_read_transactions_from_csv(mock_read_csv):
    mock_df = pd.DataFrame([
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200}
    ])
    mock_read_csv.return_value = mock_df

    result = read_transactions_from_csv("fake_path.csv")

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["id"] == 1


@patch("pandas.read_excel")
def test_read_transactions_from_excel(mock_read_excel):
    mock_df = pd.DataFrame([
        {"id": 1, "amount": 100}
    ])
    mock_read_excel.return_value = mock_df

    result = read_transactions_from_excel("fake_path.xlsx")

    assert isinstance(result, list)
    assert result[0]["amount"] == 100
