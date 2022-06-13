import pandas as pd


def osaka_shukuhaku_shisetsu() -> pd.DataFrame:
    '''
    民泊など宿泊施設一覧より　旅館業・特区民泊・住宅宿泊事業の施設等一覧
    令和4年2月28日時点データ
    https://www.city.osaka.lg.jp/contents/wdu290/opendata/#cat-all_data-00000375
    '''
    target_url = 'https://www.city.osaka.lg.jp/contents/wdu290/opendata/dataset/data-00000375/202202ketsugo.csv'
    df = pd.read_csv(target_url)
    return df


def osaka_akachan_eki() -> pd.DataFrame:
    '''
    大阪市赤ちゃんの駅
    令和4年3月16日現在
    https://www.city.osaka.lg.jp/contents/wdu290/opendata/#cat-all_data-00000431
    
    '''
    koukyo_url = 'https://www.city.osaka.lg.jp/contents/wdu290/opendata/dataset/data-00000431/akachaneki_koukyou_20220316.csv'
    minkan_url = 'https://www.city.osaka.lg.jp/contents/wdu290/opendata/dataset/data-00000431/akachaneki_minkan_20220316.csv'
    def _read_akachan(target_url: str, _type: str) -> pd.DataFrame:
        df = pd.read_csv(target_url, on_bad_lines='skip')
        df['種類'] = _type
        return df
    df1 = _read_akachan(koukyo_url, '公共')
    df2 = _read_akachan(minkan_url, '民間')
    df = pd.concat([df1, df2]).reset_index(drop=True)
    return df


def osaka_shokuhin_eigyo_kyoka() -> pd.DataFrame:
    '''
    食品営業許可施設一覧（推奨データセットA-1）
    令和3年12月31日現在
    https://www.city.osaka.lg.jp/contents/wdu290/opendata/#cat-all_data-00000382

    '''

    target_url = 'https://www.city.osaka.lg.jp/contents/wdu290/opendata/dataset/data-00000382/271004_food_business_all_20211231.csv'
    df = pd.read_csv(target_url)
    return df


def osaka_riyo() -> pd.DataFrame:
    '''
    理容所一覧
    令和3年3月時点まで
    https://www.city.osaka.lg.jp/contents/wdu290/opendata/#cat-all_data-00000025
    
    '''
    target_url = 'https://www.city.osaka.lg.jp/contents/wdu290/opendata/dataset/data-00000025/ri20210331.csv'
    df = pd.read_csv(target_url)
    return df


def osaka_biyo() -> pd.DataFrame:
    '''
    美容所一覧

    '''
    target_url = 'https://www.city.osaka.lg.jp/contents/wdu290/opendata/dataset/data-00000025/bi20210331.csv'
    df = pd.read_csv(target_url)
    return df


def osaka_kanko_shisetsu() -> pd.DataFrame:
    '''
    観光施設一覧　推奨データセット05
    令和3年12月末まで
    https://www.city.osaka.lg.jp/contents/wdu290/opendata/#cat-all_data-00000518
    '''
    target_url = 'https://www.city.osaka.lg.jp/contents/wdu290/opendata/dataset/data-00000518/271004_tourism_202112.csv'
    df = pd.read_csv(target_url)
    return df


def osaka_hinanjo() -> pd.DataFrame:
    '''
    指定緊急避難場所一覧　推奨データセット10
    令和3年12月末
    https://www.city.osaka.lg.jp/contents/wdu290/opendata/#cat-all_data-00000520
    '''
    target_url = 'https://www.city.osaka.lg.jp/contents/wdu290/opendata/dataset/data-00000520/271004_evacuation_space_202112.csv'
    df = pd.read_csv(target_url)
    return df


def osaka_ippankaike_shushi() -> pd.DataFrame:
    '''
    一般会計収支状況の推移
    1989年から2020年
    https://www.city.osaka.lg.jp/contents/wdu290/opendata/#cat-all_data-00000620
    '''
    target_url = 'https://www.city.osaka.lg.jp/contents/wdu290/opendata/dataset/data-00000620/syushi.csv'
    df = pd.read_csv(target_url)
    return df


def osaka_kodomo_hondana() -> pd.DataFrame:
    '''
    大阪市立図書館「こどものほんだな」（児童図書）
    2022年4月現在
    https://www.city.osaka.lg.jp/contents/wdu290/opendata/#cat-all_data-00000371
    '''
    target_url = 'https://www.city.osaka.lg.jp/contents/wdu290/opendata/dataset/data-00000371/kodomohon.csv'
    df = pd.read_csv(target_url)
    return df

def osaka_shuseiritsu() -> pd.DataFrame:
    '''
    出生数・出生率
    https://www.city.osaka.lg.jp/contents/wdu290/opendata/#cat-91_data-00000421
    '''
    target_url = 'https://www.city.osaka.lg.jp/contents/wdu290/opendata/dataset/data-00000421/data_01_1_shusshousuuritu.csv'
    df = pd.read_csv(target_url)
    return df
