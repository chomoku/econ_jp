import sys
sys.path.append("../econ_jp")

import pandas as pd

from econ_jp import econ_jp


class TestClass:
    def test_read_df(self):
        df = econ_jp.boj_monetary_base()
        assert type(df) == pd.DataFrame

    def test_check_read_boj(self):
        df = econ_jp.boj_monetary_base()
        df_shape_wide = df.shape[1]
        assert df_shape_wide == 6
