import pandas as pd
import numpy as np
import sqlite3


df_comercio: pd.DataFrame = pd.read_csv(
    "tmp/Comercio.csv", sep=None, engine="python", header=None
)

info_cols = 3

years_col = [
    year for year in range(1970, 1970 + (len(df_comercio.columns) - info_cols))
]

df_columns = ["index", "produtos_ext", "produtos"] + years_col

df_comercio.columns = df_columns

df_unpivot = df_comercio.melt(
    id_vars="produtos", value_vars=years_col, var_name="ano", value_name="quantidade"
)

df_unpivot["categoria"] = np.where(
    df_unpivot["produtos"].str.isupper(), df_unpivot["produtos"], None
)

df_unpivot["categoria"] = df_unpivot["categoria"].ffill()

df_categories = df_unpivot.copy()

df_categories = df_categories[df_categories["produtos"].str.isupper()]

df_categories = df_categories[["categoria", "ano", "quantidade"]]

df_products = df_unpivot[~df_unpivot["produtos"].str.isupper()]

df_products = df_products[["produtos", "categoria", "ano", "quantidade"]]


conn = sqlite3.connect("instance/Database.db")

df_categories.to_sql(
    name="comercio_categorias",
    schema="scrapping",
    con=conn,
    if_exists="replace",
    index=False,
)
df_products.to_sql(
    name="comercio_produtos",
    schema="scrapping",
    con=conn,
    if_exists="replace",
    index=False,
)