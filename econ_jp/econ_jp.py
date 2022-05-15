import traceback

import pandas as pd
import numpy as np

"""
データのカタチ
- 時系列のデータの場合、日付をインデックスに持ってくる。
"""


def kakei_chosa(multi_index: bool = True) -> pd.DataFrame:
    """
    2人以上家計の家計調査の2000年からの支出金額(小分類まで)
    のデータを返す関数

    出典：家計調査（家計収支編）　時系列データ（二人以上の世帯）（https://www.stat.go.jp/data/kakei/longtime/index.html）
    データURL: "https://www.stat.go.jp/data/kakei/longtime/csv/h-mon-a.csv"

    Params:
        multi_index: bool

    データフレームのインデックスの指定。Trueならマルチインデックスでデータを返し、Falseなら品目分類をインデックスにしてデータを返す。

    Returns:
        pd.DataFrame

    """
    kakei_url = "https://www.stat.go.jp/data/kakei/longtime/csv/h-mon-a.csv"
    try:
        df = pd.read_csv(kakei_url, encoding="shift-jis")
    except:
        print(traceback.format_exc())
        traceback.print_exc()
        print("家計調査のCSVファイルが読み込めません")
    data = df.loc[3:, "1":]
    data = data.astype(float)
    index_col = df.loc[3:, "Unnamed: 1":"Unnamed: 5"]
    index_name = df.loc[2, "Unnamed: 1":"Unnamed: 5"].values
    index_col.columns = index_name
    cols = pd.date_range("2000-01-01", freq="M", periods=int(df.columns[-1]))
    data.columns = cols
    if multi_index:
        data.index = pd.MultiIndex.from_frame(index_col)
        data = data.T
        return data
    else:
        single_index = index_col["品目分類"].values
        data.index = single_index
        data = data.T
        return data


def boueki_total_monthly() -> pd.DataFrame:
    """
    日本の貿易収支の月別推移データ（1979年～: 世界月別; 総額; 単位　千円）

    財務省　貿易統計: https://www.customs.go.jp/toukei/suii/html/time.htm
    csv url: https://www.customs.go.jp/toukei/suii/html/data/d41ma.csv

    Returns:
        pd.DataFrame
        列名:
            exp_total: 輸出額
            imp_total: 輸入額
            trade_balance: 貿易収支
        trade_balanceは長目が独自に計算している。
    """
    data_url = "https://www.customs.go.jp/toukei/suii/html/data/d41ma.csv"
    df = pd.read_csv(
        data_url,
        encoding="shift-jis",
    )
    df = df.loc[3:, :]
    df.columns = ["date", "exp_total", "imp_total"]
    df = df.set_index("date")
    df = df.replace("0", np.nan)
    df = df.dropna()
    df.index = pd.to_datetime(df.index)
    df = df.astype(np.int64)
    df["trade_balance"] = df["exp_total"] - df["imp_total"]
    return df


def boj_monetary_base(lang: str = "jp") -> pd.DataFrame:
    """
    日本銀行が供給する通貨量を示すマネタリーベースのデータを取得する関数。
    URL: https://www.boj.or.jp/statistics/boj/other/mb/index.htm/
    data_url = "https://www.boj.or.jp/statistics/boj/other/mb/mblong.xlsx"

    Params:
        lang: str
            'jp' or 'en'
            カラム名: 日本語 or 英語を選択できる

    Returns:
        pd.DataFrame
        マネタリーベースのデータ

    """
    data_url = "https://www.boj.or.jp/statistics/boj/other/mb/mblong.xlsx"
    df = pd.read_excel(data_url, sheet_name="平残（Average amounts outstanding）")
    df = df.loc[6:, "Unnamed: 1":]
    table_titles = {
        "en": {
            "columns": [
                "date",
                "monetary base",
                "banknotes in circulation",
                "coins in circuration",
                "current account balances",
                "reserve balances",
                "monetary base(seasonally adjusted)",
            ],
            "index": "date",
        },
        "jp": {
            "columns": [
                "日付",
                "マネタリーベース",
                "日本銀行券発行高",
                "貨幣流通高",
                "日銀当座預金",
                "日銀当座預金（準備預金）",
                "マネタリーベース（季節調整済み）",
            ],
            "index": "日付",
        },
    }
    df.columns = table_titles[lang]["columns"]
    df.index = df.set_index(table_titles[lang]["index"])
    df.index = pd.to_datetime(df.index)
    return df
