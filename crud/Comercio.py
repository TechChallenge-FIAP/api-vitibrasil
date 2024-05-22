import pandas as pd
import numpy as np
import sqlite3


df_comercio: pd.DataFrame = pd.read_csv("tmp/Comercio.csv", sep=None, engine="python")

info_cols = 3

years_col = [
    year for year in range(1970, 1970 + (len(df_comercio.columns) - info_cols))
]


df_columns = ["id", "produtos_ext", "produto"] + years_col

df_comercio.columns = df_columns


df_unpivot = df_comercio.melt(
    id_vars=["id", "produto"],
    value_vars=years_col,
    var_name="ano",
    value_name="quantidade_l",
)

df_unpivot["categoria"] = np.where(
    df_unpivot["produto"].str.isupper(), df_unpivot["produto"], None
)

df_unpivot["categoria"] = df_unpivot["categoria"].ffill()

df_categories = df_unpivot.copy()
df_categories = df_categories[df_categories["produto"].str.isupper()]
df_categories = df_categories[["id", "categoria", "ano", "quantidade_l"]]
df_categories["id"] = np.arange(0, len(df_categories))

df_products = df_unpivot[~df_unpivot["produto"].str.isupper()]
df_products = df_products[["id", "produto", "categoria", "ano", "quantidade_l"]]
df_products["id"] = np.arange(0, len(df_products))
df_products["produto"] = df_products["produto"].str.strip()


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

conn.close()
