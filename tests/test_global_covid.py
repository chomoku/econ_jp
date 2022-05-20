from econ_jp import econ_jp
import pandas as pd


class TestClass:
    def test_dataframe(self):
        df = econ_jp.global_covid_daily_data()
        assert type(df) == pd.DataFrame
