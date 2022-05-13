import pandas as pd


def kakei_chosa(multi_index: bool = True) -> pd.DataFrame:
    """
    2人以上家計の家計調査の2000年からの支出金額(小分類まで)
    のデータを返す関数

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
        print('家計調査のCSVファイルが読み込めません')
    data = df.loc[3:, "1":]
    data = data.astype(float)
    index_col = df.loc[3:, "Unnamed: 1":"Unnamed: 5"]
    index_name = df.loc[2, "Unnamed: 1":"Unnamed: 5"].values
    index_col.columns = index_name
    cols = pd.date_range("2000-01-01", freq="M", periods=int(df.columns[-1]))
    data.columns = cols
    if multi_index:
        data.index = pd.MultiIndex.from_frame(index_col)
        return data
    else:
        single_index = index_col["品目分類"].values
        data.index = single_index
        return data
