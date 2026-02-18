import pandas as pd
import os

CSV_FILE = "ocorrencias_coleta_x_4.csv"
XLSX_FILE = "ocorrencias_coleta_x_4.xlsx"

ORDEM_COLUNAS = [
    "Data",
    "Hora",
    "Tipo_Incidente",
    "Cidade 1",
    "Cidade 2",
    "Cidade 3",
    "Cidade 4",
    "UF",
    "Rodovia",
    "KM",
    "Perfil",
    "Tipo_Perfil",
    "Local_Referencia",
    "Texto Completo"
]

def salvar_ocorrencia(dados):
    df_novo = pd.DataFrame([dados])

    # Garante que todas as colunas existam
    for col in ORDEM_COLUNAS:
        if col not in df_novo.columns:
            df_novo[col] = ""

    if os.path.exists(CSV_FILE):
        df_existente = pd.read_csv(CSV_FILE)
        df_combined = pd.concat([df_existente, df_novo], ignore_index=True)
        df_combined.drop_duplicates(
            subset=["Perfil", "Texto Completo"],
            inplace=True
        )
    else:
        df_combined = df_novo

    # Reordena exatamente como você quer
    df_combined = df_combined[ORDEM_COLUNAS]

    df_combined.to_csv(CSV_FILE, index=False, encoding="utf-8-sig")
    df_combined.to_excel(XLSX_FILE, index=False)



