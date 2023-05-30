# pip install a-pandas-ex-bs4df
# https://github.com/hansalemaos/a_pandas_ex_bs4df
from a_pandas_ex_bs4df import pd_add_bs4_to_df

import pandas as pd

pd_add_bs4_to_df()

from PrettyColorPrinter import add_printer  # optional

add_printer(True)  # optional
# url=r"C:\scraping\ibissp.html"
url = r"C:\scraping\hotel2.html"
df = pd.Q_bs4_to_df(url).copy()
bubble_df = df.loc[df.bb_class.str.contains("bubble", na=False)]
title_df = bubble_df.loc[
    bubble_df.aa_next_element.astype("string").str.contains("H5 _a", na=False)
]
titeldf_main = df.loc[df.aa_soup.isin(title_df.aa_next_element)]
descricao = titeldf_main.aa_parent.apply(lambda x: x.text)
titulos = title_df.aa_next_element.apply(lambda x: x.text)
avaliacao = title_df.bb_class.str.split("_").str[-1].astype("Float64") / 10
dffinal = pd.concat(
    [
        titulos.reset_index(drop=True),
        avaliacao.reset_index(drop=True),
        descricao.reset_index(drop=True),
    ],
    axis=1,
    ignore_index=True,
)
dffinal.columns = "aa_title", "aa_grade", "aa_description"
dffinal.aa_description = dffinal.apply(
    lambda x: x.aa_description[len(x.aa_title) :], axis=1
)
