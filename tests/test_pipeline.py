import os

import pandas as pd


def test_of_extract_data():
    from app.pipeline.extract import extract_data

    data = extract_data(os.path.abspath('data/input/'))
    assert isinstance(data, list)
    assert len(data) > 0
    assert data is not None
