from typing import List
import pandas as pd
import sqlite3


df_espumantes: pd.DataFrame = pd.read_csv(
    "tmp/ImpEspumantes.csv", sep=";", engine="python"
)

df_espumantes["grupo"] = "Espumantes"

df_suco: pd.DataFrame = pd.read_csv(
    "tmp/ImpSuco.csv", sep=";", engine="python"
)

df_suco["grupo"] = "Suco de uva"

df_vinho: pd.DataFrame = pd.read_csv(
    "tmp/ImpVinhos.csv", sep=";", engine="python"
)

df_vinho["grupo"] = "Vinhos de mesa"

df_uva_passas: pd.DataFrame = pd.read_csv(
    "tmp/ImpPassas.csv", sep=";", engine="python"
)

df_uva_passas["grupo"] = "Uvas passas"

df_uva_frescas: pd.DataFrame = pd.read_csv(
    "tmp/ImpFrescas.csv", sep=";", engine="python"
)

df_uva_frescas["grupo"] = "Uvas frescas"

df_list: List[pd.DataFrame] = [
    df_espumantes,
    df_suco,
    df_vinho,
    df_uva_passas,
    df_uva_frescas,
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
    name="importacao",
    schema="scrapping",
    con=conn,
    if_exists="replace",
    index=False,
)