import pandas as pd 
from . import util
from datetime import datetime

def kobe_zeishu() -> pd.DataFrame:
    '''
    市税の科目別決算額
    URL: https://data.city.kobe.lg.jp/data/dataset/25470-2-2-0-10-70de74abe376d90a-e623e9107864966b

    '''
    data_url = 'https://www.city.kobe.lg.jp/documents/25470/kamokubetukessan.csv'
    df = pd.read_csv(data_url, encoding='cp932')
    df['科目'] = df['科目'].map(lambda x: x.replace(' ', '') if x[-1] == ' ' else x)
    return df


def kobe_key_data() -> pd.DataFrame:
    '''
    神戸市の主要項目の長期推移データ
    URL: https://data.city.kobe.lg.jp/data/dataset/39728-2-2-0-10/resource/8fb67137-7729-4b93-95f1-648a96672671
    '''
    data_url = 'https://www.city.kobe.lg.jp/documents/39728/toukeisyo.csv'
    df = pd.read_csv(data_url, encoding='cp932')
    return df


def kobe_sannomiya_zinryu() -> pd.DataFrame:
    '''
    三宮エリアの赤外線センサの歩行者数データ
    2020年2月1日から2021年3月23日まで　1時間おきのデータ
    URL: https://data.city.kobe.lg.jp/data/dataset/33478-3-2-0-16-b65ac8befcec1bf2d344a6ec090a38ef-f2190a6cc9fe1922-c2a37f853c67136d/resource/e62be104-81b5-4942-971b-8d318c88147b
    '''
    data_url= 'https://www.city.kobe.lg.jp/documents/33478/sannomiya_hokosha_data.csv'
    df = pd.read_csv(data_url, encoding='cp932', parse_dates=['日時'])
    return df


def kobe_harbor_shipnum() -> pd.DataFrame:
    '''
    神戸港入港数　2012年から2021年
    URL: https://data.city.kobe.lg.jp/data/dataset/11957-3-2-0-10-cc552aa6f4ee98f9b07b58292308a300-33e2bf65b7eda01d-794792196c02f2d2/resource/724a006f-b92e-42a3-9de9-d0b79a3b6633
    '''
    data_url = 'https://www.city.kobe.lg.jp/documents/11957/2021_ships_arrival.csv'
    df = pd.read_csv(data_url, encoding='shift-jis')
    return df



def kobe_harbor_containers_num_by_country() -> pd.DataFrame:
    '''
    神戸港国別扱いコンテナ数 2012年から2021年
    URL：https://data.city.kobe.lg.jp/data/dataset/11957-3-2-0-10-cc552aa6f4ee98f9b07b58292308a300-33e2bf65b7eda01d-4d5ecac1f9266fc6/resource/7fe81784-4c06-48d0-b1c1-a185b61a65d3
    '''
    data_url = 'https://www.city.kobe.lg.jp/documents/11957/2021_container_throughput.csv'
    df = pd.read_csv(data_url, encoding='shift-jis')
    return df


def kobe_harbor_cargo_volume_by_country_and_product() -> pd.DataFrame:
    '''
    神戸港　国別品種別取り扱い貨物量　2012年から2021年
    URL：https://data.city.kobe.lg.jp/data/dataset/11957-3-2-0-10-cc552aa6f4ee98f9b07b58292308a300-33e2bf65b7eda01d-a525b97d8ca9e7e9/resource/449b42da-0f06-4294-88ec-f15c02d6b37f
    '''
    data_url = 'https://www.city.kobe.lg.jp/documents/11957/2021_cargo_traffic.csv'
    df = pd.read_csv(data_url, encoding='shift-jis')
    return df


def kobe_traffic_accident() -> pd.DataFrame:
    '''
    神戸市の交通事故データ　2017年から2020年
    URL：https://data.city.kobe.lg.jp/data/dataset/kotsujiko
    '''
    data_url = 'https://data.city.kobe.lg.jp/data/dataset/86d1aa36-9b70-4a8e-9971-5ae221bb6a6e/resource/6e0a0f44-cc57-421a-8a96-b5113b7fbe0a/download/kotsujiko20172020.csv'
    df = pd.read_csv(data_url, encoding='shift-jis', parse_dates=['発生年月日'])
    df['dt'] = df.apply(lambda x: datetime(x['発生年月日'].year, x['発生年月日'].month, x['発生年月日'].day, x['発生時間']), axis=1)
    return df


def kobe_restaurant() -> pd.DataFrame:
    '''
    神戸市の生活衛生許可施設　令和4年3月末現在
    URL: https://data.city.kobe.lg.jp/data/dataset/6359-7-2-0-3-913cbb207ab34ab6-0906fbdf034b0c7e/resource/be02237c-64ac-4e8e-afc0-3997951cd2e3
    '''
    data_url ='https://www.city.kobe.lg.jp/documents/6359/-r403_all--.csv'
    df = pd.read_csv(data_url, encoding='cp932')
    df['許可決定日_dt'] = df['許可決定日'].map(util._wareki_to_seireki)
    df['許可満了日_dt'] = df['許可満了日'].map(util._wareki_to_seireki)
    return df


def kobe_riyo() -> pd.DataFrame:
    '''
    神戸市の理容店　令和4年3月末
    URL: https://data.city.kobe.lg.jp/data/dataset/6359-7-2-0-3-913cbb207ab34ab6-17cb723d8f27feb3/resource/9cc918ed-ea34-4fd3-90bb-296f176f272d
    '''
    data_url = 'https://www.city.kobe.lg.jp/documents/6359/r3_riyousho.csv'
    df = pd.read_csv(data_url, encoding='utf-16', sep='\t')
    df['確認日_dt'] = df['確認日'].map(util._wareki_to_seireki)
    return df


def kobe_biyo() -> pd.DataFrame:
    '''
    神戸市の美容店　令和4年3月末
    URL: https://data.city.kobe.lg.jp/data/dataset/6359-7-2-0-3-913cbb207ab34ab6-d511d5bfd733a29d/resource/8ad7e0d2-1420-48a6-ba1b-30c3adada9ef
    '''
    data_url = 'https://www.city.kobe.lg.jp/documents/6359/r3_biyousho.csv'
    df = pd.read_csv(data_url, encoding='utf-16', sep='\t')
    df['確認日_dt'] = df['確認日'].map(util._wareki_to_seireki)
    return df


def kobe_subway_passanger() -> pd.DataFrame():
    '''
    市営地下鉄の乗客数
    https://data.city.kobe.lg.jp/data/dataset/33478-5-2-0-2-0dad50e574a02b2cb29d051072c3cb39-daf5ca9891d135e0-10fa08a05d8b0ce4/resource/13cd7ee8-e2af-4ea3-b377-234653af258a
    
    '''
    data_url = 'https://www.city.kobe.lg.jp/documents/33478/subwaydata.csv'
    df = pd.read_csv(data_url, encoding='cp932', parse_dates=['日付'])
    df = df.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9'], axis=1)
    df = df.dropna(how='all')
    return df
