from econ_jp import econ_jp
import pandas as pd


class TestClass:
    def test_dataframe(self):
        df = econ_jp.boueki_total_monthly()
        assert type(df) == pd.DataFrame
