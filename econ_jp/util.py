from datetime import datetime


def _wareki_to_seireki_dot(x: str) -> datetime:
    """
    ドット区切りの和暦のデータを西暦に変換する関数
    x: str
    SYY.MM.DD
    HYY.MM.DD
    RYY.MM.DD
    """
    try:
        date = x.split(".")
        if date[0].startswith("S"):
            year_int = 1925 + int(date[0][1:])
        elif date[0].startswith("H"):
            year_int = 1988 + int(date[0][1:])
        elif date[0].startswith("R"):
            year_int = 2018 + int(date[0][1:])

        return datetime(year_int, int(date[1]), int(date[2])).date()
    except:
        pass


def _wareki_split(x, add_num):
    x = x[2:]
    split_one = x.split('年')
    year_int = int(split_one[0]) + add_num
    split_two = split_one[1].split('月')
    month_int = int(split_two[0])
    day_int = int(split_two[1].replace('日', ''))
    return datetime(year_int, month_int, day_int)

def _wareki_to_seireki(x) -> datetime:
    try:
        if x[:2] == '令和':
            return _wareki_split(x, 2018)
        elif x[:2] == '平成':
            return _wareki_split(x, 1988)
        elif x[:2] == '昭和':
            return _wareki_split(x, 1925)
    except:
        pass
