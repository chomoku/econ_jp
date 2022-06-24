import traceback
import warnings
from datetime import timedelta
from io import BytesIO

import numpy as np
import pandas as pd
import requests

warnings.simplefilter("ignore")
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
    df = pd.read_excel(
        data_url, sheet_name="平残（Average amounts outstanding）", engine="openpyxl"
    )
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
    df = df.set_index(table_titles[lang]["index"])
    df.index = pd.to_datetime(df.index)
    return df


def jp_covid_daily_data() -> pd.DataFrame:
    """
    NHKのコロナウィルス感染者数などのデータを読み込む関数。
    新型コロナ関連の情報提供:NHK
    https://www3.nhk.or.jp/news/special/coronavirus/data/rules.html
    Returns:
        pd.DataFrame
        ロングフォームな各都道府県のデータを返す

    """
    csv_url = "https://www3.nhk.or.jp/n-data/opendata/coronavirus/nhk_news_covid19_prefectures_daily_data.csv"
    try:
        r = requests.get(csv_url)
        df = pd.read_csv(BytesIO(r.content))
        df["日付"] = pd.to_datetime(df["日付"])
        df = df.melt(id_vars=["日付", "都道府県コード", "都道府県名"])
        return df
    except:
        print("データを取得できませんでした。")


def global_covid_daily_data(cumsum: bool = False) -> pd.DataFrame:
    """
    世界のコロナウィルス感染者数のデータ。
    データソース: Johns Hopkins University https://github.com/CSSEGISandData/COVID-19
    Params:
        cumsum: bool
            日々の感染者数を返すか、累計値を返すか。初期値はFalseで
            日々の感染者数を返す。

    Returns:
        pd.DataFrame
        インデックスに日付、カラムに国名を持つデータを返す
    """
    data_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    df = pd.read_csv(data_url)
    df = df.set_index("Country/Region")
    df = df.loc[:, "1/22/20":]
    df.columns = pd.to_datetime(df.columns)
    df = df.T
    if not cumsum:
        df = df.diff()
        df = df.dropna(how="all")
        return df
    else:
        return df


def supermarkets_num(tenpo_type: str = "合計") -> pd.DataFrame:
    """
    日本のスーパーマーケット数のデータを取得する（単月時系列）
    データソース: 一般社団法人全国スーパーマーケット協会
    統計・データで見るスーパーマーケット:
    スーパーマーケット店舗数より: http://www.j-sosm.jp/tenpo/index.html

    Params:
        tenpo_type: str
        スーパーマーケットの種類: '合計', '総合', '大型', '中型', '小型'
    Returns:
        pd.DataFrame
    """
    data_url = "http://www.j-sosm.jp/dl/tenpo2205.xlsx"
    try:
        df = pd.read_excel(
            data_url,
            header=2,
            index_col="集計日",
            sheet_name=tenpo_type,
            engine="openpyxl",
        )
        df.index = df.index.map(lambda x: x - timedelta(1))
        df.index = pd.to_datetime(df.index)
        df = df.drop(["Unnamed: 0", "Unnamed: 1"], axis=1)
        return df
    except:
        print("データが取得できません")


def supermarkets_sales(data_type: str = "全体", kizon_ten: bool = False) -> pd.DataFrame:
    """
    日本のスーパーマーケットの販売動向データを取得する（単月時系列）
    データソース: 一般社団法人全国スーパーマーケット協会
    統計・データで見るスーパーマーケット:
    スーパーマーケット店舗数より: http://www.j-sosm.jp/news/index.html
    Params:
        data_type: str
            データの種別: '全体', 'エリア別', '店舗数別'
        kizon_ten: bool
            全店データか既存点データか選択する: 初期値 False: 全店
    Returns:
        pd.DataFrame
    """
    zen_kizon = ["前年同月比（全店）", "前年同月比（既存店）"]

    try:
        data_url = "http://www.j-sosm.jp/dl/hanbai_month.xlsx"
        df = pd.read_excel(
            data_url, header=[2, 3], sheet_name=data_type, engine="openpyxl"
        )
        idx = pd.IndexSlice
        data = df.loc[:, idx[zen_kizon[kizon_ten], :]]
        first_date = str(df.loc[:, idx["実績年月", :]].loc[0].values[0])
        date_index = pd.date_range(
            f"{first_date[:4]}-{first_date[4:]}-1", freq="M", periods=len(data)
        )
        data_columns = data.columns.get_level_values(1)
        data.index = date_index
        data.columns = data_columns
        return data
    except:
        print("データが取得できません")


def supermarkets_di(di_type: str = "売上高DI"):
    """
    日本のスーパーマーケットの各種DIを取得する（単月時系列）
    データソース: 一般社団法人全国スーパーマーケット協会
    統計・データで見るスーパーマーケット:
    スーパーマーケット店舗数より: http://www.j-sosm.jp/news/index.html
    Params:
        di_type: str
            DIの種類の指定: '売上高DI', '収益DI', '生鮮品仕入原価DI', '食品仕入原価DI', '販売価格DI', ' 客単価DI', ' 来客数DI'
    Returns:
        pd.DataFrame
    """
    try:
        data_url = "http://www.j-sosm.jp/dl/keieidoukou.xlsx"
        df = pd.read_excel(data_url, header=3, sheet_name=di_type, engine="openpyxl")
        first_date = str(df["実績年月"][0])
        index_date = pd.date_range(
            f"{first_date[:4]}/{first_date[4:]}/1", freq="M", periods=len(df)
        )
        df.index = index_date
        df = df.drop("実績年月", axis=1)
        return df
    except:
        print("データが取得できません")
