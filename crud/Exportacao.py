from typing import List
import pandas as pd
import sqlite3


df_espumantes: pd.DataFrame = pd.read_csv(
    "tmp/ExpEspumantes.csv", sep=";", engine="python"
)

df_espumantes["grupo"] = "Espumantes"

df_suco: pd.DataFrame = pd.read_csv(
    "tmp/ExpSuco.csv", sep=";", engine="python"
)

df_suco["grupo"] = "Suco de uva"

df_vinho: pd.DataFrame = pd.read_csv(
    "tmp/ExpVinho.csv", sep=";", engine="python"
)

df_vinho["grupo"] = "Vinhos de mesa"

df_uva: pd.DataFrame = pd.read_csv(
    "tmp/ExpUva.csv", sep=";", engine="python"
)

df_uva["grupo"] = "Uvas frescas"

df_list: List[pd.DataFrame] = [
    df_espumantes,
    df_suco,
    df_vinho,
    df_uva,
]

years_kg = [
    str(year) for year in df_espumantes.columns if year not in ("Id","País") and year.split(".")[-1] != "1"
]

years_value = [
    str(year) for year in df_espumantes.columns if year not in ("Id","País") and year.split(".")[-1] == "1"
]

df_union = pd.concat(df_list)

df_unpivot_kg = df_union.melt(
    id_vars=["Id","País","grupo"],
    value_vars=years_kg,
    var_name="ano",
    value_name="qtd_kg",
)

df_unpivot_value = df_union.melt(
    id_vars=["Id","País","grupo"],
    value_vars=years_value,
    var_name="ano",
    value_name="vl_dolar",
)

df_unpivot_value["ano"] = df_unpivot_value["ano"].str.slice(stop=4)

df_final = pd.merge(
     df_unpivot_value, df_unpivot_kg, on=["Id","País","grupo","ano"]
)

df_final = df_final.rename(columns={'País': 'pais', 'Id': 'id'}) 

conn = sqlite3.connect("instance/Database.db")

df_final.to_sql(
    name="exportacao",
    schema="scrapping",
    con=conn,
    if_exists="replace",
    index=False,
)