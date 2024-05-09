from typing import List
import pandas as pd
import numpy as np
import sqlite3


df_viniferas: pd.DataFrame = pd.read_csv(
    "tmp/ProcessaViniferas.csv", sep=None, engine="python"
)

df_viniferas["grupo"] = "Viníferas"

df_americanas_hibridas: pd.DataFrame = pd.read_csv(
    "tmp/ProcessaAmericanas.csv", sep=None, engine="python"
)

df_americanas_hibridas["grupo"] = "Americanas e Híbridas"

df_uva_de_mesa: pd.DataFrame = pd.read_csv(
    "tmp/ProcessaMesa.csv", sep=None, engine="python"
)

df_uva_de_mesa["grupo"] = "Uvas de Mesa"

df_sem_class: pd.DataFrame = pd.read_csv(
    "tmp/ProcessaSemclass.csv", sep=None, engine="python"
)

df_sem_class["grupo"] = "Sem Classificação"

info_cols = 4

years_col = [
    str(year) for year in range(1970, 1970 + (len(df_viniferas.columns) - info_cols))
]

df_list: List[pd.DataFrame] = [
    df_viniferas,
    df_americanas_hibridas,
    df_uva_de_mesa,
    df_sem_class,
]

df_union = pd.concat(df_list)

df_union = df_union.rename(columns={"cultivar": "tipo_uva"})

df_union["2019"] = df_union["2019"].replace("nd", "0").astype(int)

df_union["2022"] = df_union["2022"].replace("*", "0").astype(int)

df_unpivot = df_union.melt(
    id_vars=["id", "grupo", "tipo_uva"],
    value_vars=years_col,
    var_name="ano",
    value_name="quantidade_kg",
)

df_unpivot["sub_categoria"] = np.where(
    (df_unpivot["tipo_uva"].str.isupper())
    | (df_unpivot["tipo_uva"].str.contains("Sem classificação")),
    df_unpivot["tipo_uva"],
    None,
)

df_unpivot["sub_categoria"] = df_unpivot["sub_categoria"].ffill()

df_categories = df_unpivot.copy()
df_categories = df_categories[
    (df_categories["tipo_uva"].str.isupper())
    | (df_unpivot["tipo_uva"].str.contains("Sem classificação"))
]
df_categories = df_categories[["id", "grupo", "sub_categoria", "ano", "quantidade_kg"]]
df_categories["id"] = np.arange(0, len(df_categories))

df_products = df_unpivot[
    ~(df_unpivot["tipo_uva"].str.isupper())
    & ~(df_unpivot["tipo_uva"].str.contains("Sem classificação"))
]
df_products = df_products[
    ["id", "grupo", "sub_categoria", "tipo_uva", "ano", "quantidade_kg"]
]
df_products["id"] = np.arange(0, len(df_products))
df_products["tipo_uva"] = df_products["tipo_uva"].str.strip()


conn = sqlite3.connect("instance/Database.db")

df_categories.to_sql(
    name="processamento_categorias",
    schema="scrapping",
    con=conn,
    if_exists="replace",
    index=False,
)
df_products.to_sql(
    name="processamento_tipo_uva",
    schema="scrapping",
    con=conn,
    if_exists="replace",
    index=False,
)

conn.close()
