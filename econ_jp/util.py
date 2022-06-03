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
