from .econ_jp import *
from dataclasses import dataclass

@dataclass
class KakeiChosaShishutsu:

    name: str = '家計調査支出 時系列データ（二人以上の世帯） 2000年1月から'
    url: str = "https://www.stat.go.jp/data/kakei/longtime/csv/h-mon-a.csv"

    def get_data(self):
        return kakei_chosa()
