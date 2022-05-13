import sys
sys.path.append('../econ_jp')
from datetime import datetime
from econ_jp import econ_jp


def test_length():
    df = econ_jp.kakei_chosa()
    len_df = len(df)
    assert len_df == 185


def test_multiindex():
    df = econ_jp.kakei_chosa()
    len_index = len(df.index[0])
    assert len_index == 5


def test_singleindex():
    df = econ_jp.kakei_chosa(multi_index=False)
    len_index = len([df.index[0]])
    assert len_index == 1


def test_topindex():
    df = econ_jp.kakei_chosa(multi_index=False)
    top_index = df.index[0]
    assert top_index == '世帯数分布(抽出率調整)'


def check_date():
    df = econ_jp.kakei_chosa()
    top_date = df.columns[0]
    assert top_date == datetime(2000, 1, 31)
