# econ_jp

[![Image from Gyazo](https://i.gyazo.com/7cb486e1e9bf24d184eb9f3e5b0a7696.png)](https://gyazo.com/7cb486e1e9bf24d184eb9f3e5b0a7696)
## 日本のオープンデータの民主化

econ_jpは日本の経済指標をデータフレームで扱えるPythonのパッケージです。日本の経済指標を前処理無しに使えます。

現在扱えるデータは次の8つです。

- 家計調査: 2人以上家計　2000年からの支出額（小分類）
  - 出典：家計調査（家計収支編）　時系列データ（二人以上の世帯）（https://www.stat.go.jp/data/kakei/longtime/index.html）
  - データURL: "https://www.stat.go.jp/data/kakei/longtime/csv/h-mon-a.csv"
- 貿易収支: 1979年からの月次推移
  - 出典: 財務省　貿易統計: https://www.customs.go.jp/toukei/suii/html/time.htm
  - csv url: https://www.customs.go.jp/toukei/suii/html/data/d41ma.csv
- 日銀　マネタリーベース　1970年からの月次推移
  - 出典: 日本銀行　マネタリーベース　https://www.boj.or.jp/statistics/boj/other/mb/index.htm/
  - excel url: https://www.boj.or.jp/statistics/boj/other/mb/mblong.xlsx
- 日本の各都道府県のコロナ感染者数など
  - 出典 新型コロナ関連の情報提供:NHK
  - データURL: "https://www3.nhk.or.jp/n-data/opendata/coronavirus/nhk_news_covid19_prefectures_daily_data.csv"
- 世界のコロナ感染者数
  - データソース: Johns Hopkins University https://github.com/CSSEGISandData/COVID-19
  - データURL: "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
- 日本のスーパーマーケット数
  - 統計・データで見るスーパーマーケット:
    スーパーマーケット店舗数より: http://www.j-sosm.jp/tenpo/index.html
  - データURL: "http://www.j-sosm.jp/dl/tenpo2204.xlsx"
- 日本のスーパーマーケットの販売動向データ
  - 統計・データで見るスーパーマーケット: スーパーマーケット店舗数より: http://www.j-sosm.jp/news/index.html
  - データURL: "http://www.j-sosm.jp/dl/hanbai_month.xlsx"
- 日本のスーパーマーケットの各種DI
  - 統計・データで見るスーパーマーケット: スーパーマーケット店舗数より: http://www.j-sosm.jp/news/index.html
  - データURL: "http://www.j-sosm.jp/dl/keieidoukou.xlsx"

## 使い方

```
$ pip install econ_jp
```

- 家計調査
  
```
from econ_jp import econ_jp

df = econ_jp.kakei_chosa()
```

- 貿易収支

```
from econ_jp import econ_jp

df = econ_jp.boeki_total_monthly()
```

- マネタリーベース

```
from econ_jp import econ_jp

df = econ_jp.boj_monetary_base()
```

- 日本の各都道府県のコロナ感染者数など

```
from_econ_jp import econ_jp
df = econ_jp.jp_covid_daily_data()
```

- 世界のコロナ感染者数

```
from_econ_jp import econ_jp
df = econ_jp.global_covid_daily_data()
```

- 日本のスーパーマーケット数

```
from_econ_jp import econ_jp
df = econ_jp.supermarkets_num()
```

- 日本のスーパーマーケットの販売動向データ

```
from_econ_jp import econ_jp
df = econ_jp.supermarkets_sales()
```

- 日本のスーパーマーケットの各種DI

```
from_econ_jp import econ_jp
df = econ_jp.supermarkets_di()
```

## サンプルノートブック

- [jupyter_notebook](https://github.com/chomoku/econ_jp/blob/main/sample/econ_jp_sample.ipynb)