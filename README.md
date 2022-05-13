# econ_jp

## 日本の経済指標をデータフレームで扱える

econ_jpは日本の経済指標をデータフレームで扱えるPythonのパッケージです。日本の経済指標を前処理無しに使えます。

現在扱えるデータは次の3つです。

- 家計調査: 2人以上家計　2000年からの支出額（小分類）
  - 出典：家計調査（家計収支編）　時系列データ（二人以上の世帯）（https://www.stat.go.jp/data/kakei/longtime/index.html）
  - データURL: "https://www.stat.go.jp/data/kakei/longtime/csv/h-mon-a.csv"
- 貿易収支: 1979年からの月別推移
  - 出典: 財務省　貿易統計: https://www.customs.go.jp/toukei/suii/html/time.htm
  - csv url: https://www.customs.go.jp/toukei/suii/html/data/d41ma.csv
- 日銀　マネタリーベース
  - 出典: 日本銀行　マネタリーベース　https://www.boj.or.jp/statistics/boj/other/mb/index.htm/
  - excel url: https://www.boj.or.jp/statistics/boj/other/mb/mblong.xlsx

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

