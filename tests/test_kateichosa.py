import sys

# sys.path.append("../econ_jp")
from datetime import datetime
from econ_jp import econ_jp


class TestClass:
    def test_kakei_chosa_length(self):
        df = econ_jp.kakei_chosa()
        len_df = len(df.columns)
        print(len_df)
        assert len_df == 185

    def test_kakei_chosa_multiindex(self):
        df = econ_jp.kakei_chosa()
        len_index = len(df.columns[0])
        assert len_index == 5

    def test_kakei_chosa_singleindex(self):
        df = econ_jp.kakei_chosa(multi_index=False)
        len_index = len([df.columns[0]])
        assert len_index == 1

    def test_kakei_chosa_topindex(self):
        df = econ_jp.kakei_chosa(multi_index=False)
        top_index = df.columns[0]
        assert top_index == "世帯数分布(抽出率調整)"

    def check_kakei_chosa_date(self):
        df = econ_jp.kakei_chosa()
        top_date = df.index[0]
        print(top_date)
        assert top_date == datetime(2000, 1, 31)
