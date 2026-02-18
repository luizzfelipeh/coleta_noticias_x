# gerador_noticia.py — COLETA X 5.0

import re

# Tipos que geram risco real imediato
TIPOS_IMINENTES = {
    "Acidente",
    "Bloqueio Total",
    "Manifestação / Protesto",
    "Incêndio",
    "Derramamento de Carga",
    "Obstáculo na Pista"
}


# ============================================================
# DEFINE PROBABILIDADE DE IMPACTO
# ============================================================

def definir_probabilidade(tipo_incidente):
    if tipo_incidente in TIPOS_IMINENTES:
        return "Iminente"
    return "Potencial"


# ============================================================
# GERA A NOTÍCIA FORMATADA PARA WHATSAPP
# ============================================================

def gerar_noticia(resultado):
    tipo = resultado["Tipo_Incidente"]
    prob = definir_probabilidade(tipo)

    # ✅ USA DIRETO O DICIONÁRIO (motor_extracao)
    cidade = resultado.get("Cidade 1", "")
    uf = resultado.get("UF", "")

    if cidade and uf and uf != "Não informado":
        cidade_uf = f"{cidade}/{uf}"
    else:
        cidade_uf = cidade if cidade else "Não informado"

    lead = resultado["Texto Completo"].strip()

    noticia = f"""*Tipo de incidente:* {tipo}
*Probabilidade de impacto:* {prob}
*Cidade/UF:* {cidade_uf}

*Lead:*
{lead}

*Fonte:*"""

    return noticia
