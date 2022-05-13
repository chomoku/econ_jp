import sys

# sys.path.append("../econ_jp")
from datetime import datetime
from econ_jp import econ_jp

class TestClass:
    def test_kakei_chosa_length():
        df = econ_jp.kakei_chosa()
        len_df = len(df)
        assert len_df == 185


    def test_kakei_chosa_multiindex():
        df = econ_jp.kakei_chosa()
        len_index = len(df.index[0])
        assert len_index == 5


    def test_kakei_chosa_singleindex():
        df = econ_jp.kakei_chosa(multi_index=False)
        len_index = len([df.index[0]])
        assert len_index == 1


    def test_kakei_chosa_topindex():
        df = econ_jp.kakei_chosa(multi_index=False)
        top_index = df.index[0]
        assert top_index == "世帯数分布(抽出率調整)"


    def check_kakei_chosa_date():
        df = econ_jp.kakei_chosa()
        top_date = df.columns[0]
        assert top_date == datetime(2000, 1, 31)


    def check_boueki_world_monthly():
        df = econ_jp.boueki_total_monthly()
        last_column = df.columns[-1]
        assert last_column == "trade_balance"
