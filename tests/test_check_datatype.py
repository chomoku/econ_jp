import pandas as pd

from econ_jp import econ_jp, econ_kyoto, econ_osaka


def test_dataframe():
    funcs = [
        econ_jp.boj_monetary_base,
        econ_jp.boueki_total_monthly,
        econ_jp.global_covid_daily_data,
        econ_jp.jp_covid_daily_data,
        econ_jp.kakei_chosa,
        econ_jp.supermarkets_di,
        econ_jp.supermarkets_num,
        econ_jp.supermarkets_sales,
        econ_kyoto.kyoto_jinko_doutai,
        econ_kyoto.kyotofu_jinko,
        econ_kyoto.kyotoshi_biyosho_ichiran,
        econ_kyoto.kyotoshi_cleaning_ichiran,
        econ_kyoto.kyotoshi_hotels,
        econ_kyoto.kyotoshi_riyosho_ichiran,
        econ_kyoto.kyotoshi_shokuhin_eigyo_ichiran,
        econ_kyoto.kyotoshi_hinanjo,
        econ_osaka.osaka_shukuhaku_shisetsu,
        econ_osaka.osaka_akachan_eki,
        econ_osaka.osaka_shokuhin_eigyo_kyoka,
        econ_osaka.osaka_riyo,
        econ_osaka.osaka_biyo,
        econ_osaka.osaka_kanko_shisetsu,
        econ_osaka.osaka_hinanjo,
        econ_osaka.osaka_ippankaike_shushi,
        econ_osaka.osaka_kodomo_hondana,
        econ_osaka.osaka_shuseiritsu
    ]
    for func in funcs:
        df = func()
        assert type(df) == pd.DataFrame
