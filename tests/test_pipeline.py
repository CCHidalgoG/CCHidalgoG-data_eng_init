import pandas as pd



def test_of_extract_data():
    from app.pipeline.extract import extract_data
    data = extract_data("data/input/")
    assert isinstance(data, pd.DataFrame)
    assert data.shape[0] > 0
    assert data.shape[1] > 0
    assert data is not None
    assert not data.empty
    assert data is not None
    assert not data.empty