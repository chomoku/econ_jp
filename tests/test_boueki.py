import pandas as pd

from econ_jp import econ_jp


class TestClass:
    def test_dataframe(self):
        df = econ_jp.boueki_total_monthly()
        assert type(df) == pd.DataFrame
