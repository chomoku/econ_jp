import warnings

import pandas as pd

from . import util

warnings.simplefilter("ignore")

"""
ひとまず関数の形で作成しておく。
それぞれクラスが良ければ、そのタイミングで作り直す。
econ_kyoto: 京都府内のオープンデータを扱う
京都府オープンデータカタログ: https://odcs.bodik.jp/260002/
京都市オープンデータポータルサイト: https://data.city.kyoto.lg.jp/
"""


def kyotofu_jinko() -> pd.DataFrame:
    """
    Return:
    melt_df: pd.DataFrame
    value: 人
    1990年から2020年までの5年ごとの年齢別人口のデータ
    Webページ: https://data.bodik.jp/dataset/260002_tokeisyo0207/resource/953a2f65-5e06-496c-b72e-f07c990e91c7

    """
    csv_url = "https://data.bodik.jp/dataset/59c7a51d-415d-49ff-b957-e4b5b4536e95/resource/953a2f65-5e06-496c-b72e-f07c990e91c7/download/tokeisyo0207.csv"
    df = pd.read_csv(csv_url)
    df = df[["西暦（暦年）", "地域", "区分", "総数（人）", "男（人）", "女（人）"]]
    df = df.rename({"西暦（暦年）": "西暦", "総数（人）": "総数", "男（人）": "男", "女（人）": "女"}, axis=1)
    melt_df = df.melt(id_vars=["西暦", "地域", "区分"])
    melt_df["西暦"] = melt_df["西暦"].map(lambda x: int(x.replace("年", "")))
    melt_df = melt_df.rename({"区分": "年齢", "variable": "性別"}, axis=1)
    return melt_df


def kyoto_jinko_doutai():
    """
    京都府の市区町村人口動態
    1991年から2020年まで
    value: 人
    Web URL: https://data.bodik.jp/dataset/260002_tokeisyo0220
    """
    csv_url = "https://data.bodik.jp/dataset/e6462071-be7d-4b42-9b0f-3b6779bdfe3e/resource/6881ea67-df45-428f-9738-1e38ad9acd20/download/tokeisyo0220.csv"
    df = pd.read_csv(csv_url)
    sel_col = [
        "西暦（暦年）",
        "地域",
        "出生数（人）",
        "死亡数（人）",
        "うち乳児死亡数（人）",
        "うち新生児（人）",
        "死産数（人）",
        "自然死産数（人）",
        "人工死産数（人）",
        "周産期死亡数（人）",
        "婚姻数（組）",
        "離婚数（組）",
    ]
    df = df[sel_col]
    new_col = [col.split("（")[0] for col in df.columns]
    df.columns = new_col
    df_melt = df.melt(id_vars=["西暦", "地域"])
    df_melt["西暦"] = df_melt["西暦"].map(lambda x: int(x.replace("年", "")))
    df_melt = df_melt.rename({"variable": "項目"}, axis=1)
    return df_melt


def kyotoshi_riyosho_ichiran():
    """
    京都市の理容所施設データ
    令和4年3月末時点
    web url: https://data.city.kyoto.lg.jp/node/109500
    """

    excel_url = "https://data.city.kyoto.lg.jp/file/20918/download?token=6QWu7_4X"
    df = pd.read_excel(excel_url, header=1)
    df["検査確認日"] = df["検査確認日"].map(util._wareki_to_seireki_dot)
    df = df.sort_values("検査確認日")
    df = df.reset_index(drop=True)
    return df


def kyotoshi_biyosho_ichiran():
    """
    京都市の美容施設データ
    令和4年3月末時点
    web url: https://data.city.kyoto.lg.jp/node/109500
    """

    excel_url = "https://data.city.kyoto.lg.jp/file/20920/download?token=7n6VJGbf"
    df = pd.read_excel(excel_url, header=1)
    df["検査確認日"] = df["検査確認日"].map(util._wareki_to_seireki_dot)
    df = df.sort_values("検査確認日")
    df = df.reset_index(drop=True)
    return df


def kyotoshi_cleaning_ichiran():
    """
    京都市の美容施設データ
    令和4年3月末時点
    web url: https://data.city.kyoto.lg.jp/node/109500
    """

    excel_url = "https://data.city.kyoto.lg.jp/file/20921/download?token=33SXGdv-"
    df = pd.read_excel(excel_url, header=1)
    df["検査確認日"] = df["検査確認日"].map(util._wareki_to_seireki_dot)
    df = df.sort_values("検査確認日")
    df = df.reset_index(drop=True)
    return df


def kyotoshi_shokuhin_eigyo_ichiran():
    """
    京都市の食品営業許可一覧データ
    令和3年3月末のデータ
    ファイルが大きため、読み込みに時間がかかります。
    WEB URL: https://data.city.kyoto.lg.jp/node/109294
    """
    excel_url = "https://data.city.kyoto.lg.jp/file/20414/download?token=Nc04YovV"
    excel = pd.ExcelFile(excel_url)
    sheet_list = excel.sheet_names
    data_list = list()
    df = pd.read_excel(excel_url, sheet_name=sheet_list)
    data_list = [v for v in df.values()]
    data = pd.concat(data_list).reset_index(drop=True)
    for col in data.columns[-3:]:
        data[col] = data[col].map(util._wareki_to_seireki_dot)
    data = data.sort_values("許可年月日")
    return data


def kyotoshi_hotels(data_lang: str = "JP") -> pd.DataFrame:
    """
    Args:
        data_lang: str
        "JP" or "EN"

    旅館業法に基づく許可施設及び施設外玄関帳場一覧（令和4年5月末現在）
    web url: https://data.city.kyoto.lg.jp/node/111302
    """
    excel_url = "https://data.city.kyoto.lg.jp/file/21120/download?token=inNjLzKc"
    sheet_list = pd.ExcelFile(excel_url).sheet_names
    if data_lang == "JP":
        sheet_names = [name for num, name in enumerate(sheet_list) if num % 2 == 0]
    elif data_lang == "EN":
        sheet_names = [name for num, name in enumerate(sheet_list) if num % 2 == 1]
    data = pd.read_excel(excel_url, sheet_name=sheet_names)
    data = [v for v in data.values()]
    data = pd.concat(data).reset_index(drop=True)
    data["許可日"] = data["許可日"].map(util._wareki_to_seireki_dot)
    data = data.reset_index(drop=True)
    return data


def kyotoshi_hinanjo():
    """
    京都市の避難所のエクセルデータを読み込む関数
    H310401現在
    WEB URL: https://data.city.kyoto.lg.jp/node/94892#{}
    """
    excel_url = "https://data.city.kyoto.lg.jp/file/9898/download?token=bxb0_vYW"
    df = pd.read_excel(excel_url)
    return df
