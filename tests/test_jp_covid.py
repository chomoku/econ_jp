import pandas as pd

from econ_jp import econ_jp


class TestClass:
    def test_dataframe(self):
        df = econ_jp.jp_covid_daily_data()
        assert type(df) == pd.DataFrame
