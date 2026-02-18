# motor_extracao.py — COLETA X 5.0 (VERSÃO INTELIGENTE COMPLETA)

import re
import datetime
from perfis import RODOVIARIOS, URBANOS, CLIMA, MAPA_PERFIS, PERFIL_UFS, RODOVIA_UFS
from cidades import CIDADES_BRASIL


# ============================================================
# PALAVRAS-CHAVE (NEGATIVAS + POSITIVAS)
# ============================================================

PALAVRAS_CHAVE = {

    "Acidente": [
        "acidente", "colisão", "batida", "engavetamento",
        "capotamento", "tombamento", "choque", "abalroamento",
        "sinistro", "atropelamento",
        "colidiu", "colidiram", "acidente envolvendo",
        "colisão traseira", "colisão lateral",
        "veículo acidentado", "veículos colidiram"
    ],

    "Veículo com Pane": [
        "pane mecânica", "pane elétrica", "pane seca",
        "veículo quebrado", "veículo parado",
        "pane", "problema mecânico",
        "pane no veículo", "caminhão com pane",
        "ônibus com pane", "veículo imobilizado",
        "veículo com defeito"
    ],

    "Bloqueio Total": [
        "bloqueio total", "interdição total", "pista interditada",
        "rodovia interditada", "fechamento total",
        "tráfego interrompido", "sem passagem",
        "pista totalmente bloqueada",
        "bloqueada nos dois sentidos",
        "ambos os sentidos interditados",
        "via fechada", "interditada totalmente"
    ],

    "Bloqueio Parcial": [
        "bloqueio parcial", "faixa interditada", "interdição parcial",
        "faixa bloqueada", "apenas uma faixa liberada",
        "meia pista", "siga e pare",
        "bloqueio de faixa", "apenas faixa da direita",
        "apenas faixa da esquerda",
        "uma faixa bloqueada",
        "liberação parcial"
    ],

    "Fila / Lentidão": [
        "fila", "lentidão", "retenção", "congestionamento",
        "engarrafamento", "trânsito lento", "pare e siga",
        "reflexo", "tráfego intenso",
        "km de fila", "fila de",
        "lentidão no trecho",
        "trânsito carregado",
        "tráfego congestionado"
    ],

    "Obra / Manutenção": [
        "obra", "manutenção", "serviço na pista",
        "obras na pista", "recapeamento",
        "operação tapa-buraco",
        "intervenção na pista",
        "serviços de manutenção"
    ],

    "Manifestação / Protesto": [
        "manifestação", "protesto", "ato",
        "manifestantes", "bloqueio por manifestantes",
        "ato público", "mobilização",
        "protesto na rodovia"
    ],

    "Clima / Pista Molhada": [
        "chuva", "garoa", "tempestade", "alagamento",
        "neblina", "baixa visibilidade",
        "vento forte", "granizo", "pista molhada",
        "pista escorregadia", "chuva intensa",
        "chuva forte", "tempo chuvoso"
    ],

    "Obstáculo na Pista": [
        "queda de barreira", "deslizamento",
        "árvore na pista", "objeto na pista",
        "animal na pista", "detritos na pista",
        "queda de árvore", "material na pista",
        "barreira caída"
    ],

    "Derramamento de Carga": [
        "derramamento de carga", "óleo na pista",
        "carga na pista", "material espalhado",
        "vazamento de carga",
        "carga derramada",
        "derramamento na pista"
    ],

    "Incêndio": [
        "incêndio", "veículo em chamas",
        "fogo em veículo", "fumaça na pista",
        "incêndio em caminhão",
        "incêndio em veículo"
    ],

    # 🟢 POSITIVAS (avaliadas por último no motor ideal)
    "Fluxo Normal": [
        "sem fila", "fluxo normal", "trânsito normal",
        "tráfego normal", "sem lentidão",
        "pista liberada", "faixas liberadas",
        "rodovia liberada", "trânsito fluindo",
        "ocorrência finalizada", "situação normalizada",
        "via totalmente liberada",
        "tráfego liberado", "liberado para o tráfego"
    ]
}


# ============================================================
# RODOVIAS COM NOME DE CIDADE
# ============================================================

RODOVIAS_COM_NOME_DE_CIDADE = [
    "anhanguera",
    "bandeirantes",
    "castelo branco",
    "washington luiz",
    "dutra",
    "fernão dias",
    "régis bittencourt"
]


# ============================================================
# LOCAL DE REFERÊNCIA (urbano)
# ============================================================

PADROES_LOCAL = [
    r'linha amarela',
    r'linha vermelha',
    r'avenida [\w\s]+',
    r'av\.? [\w\s]+',
    r'rua [\w\s]+',
    r'túnel [\w\s]+',
    r'ponte [\w\s]+',
    r'elevado [\w\s]+',
    r'viaduto [\w\s]+',
]

def extrair_local_referencia(texto):
    texto_lower = texto.lower()
    for padrao in PADROES_LOCAL:
        match = re.search(padrao, texto_lower)
        if match:
            return match.group(0).title()
    return ""


# ============================================================
# DEFINE TIPO INCIDENTE (POSITIVO PRIMEIRO)
# ============================================================

def definir_tipo_incidente(texto):
    texto_lower = texto.lower()

    for kw in PALAVRAS_CHAVE["Fluxo Normal"]:
        if re.search(r'\b' + re.escape(kw) + r'\b', texto_lower):
            return "Fluxo Normal"

    for tipo, keywords in PALAVRAS_CHAVE.items():
        if tipo == "Fluxo Normal":
            continue
        for kw in keywords:
            if re.search(r'\b' + re.escape(kw) + r'\b', texto_lower):
                return tipo

    return "Não informado"


# ============================================================
# EXTRAI CIDADES DA BASE OFICIAL (VERSÃO INTELIGENTE 2.0)
# ============================================================

def extrair_cidades_do_texto(texto, perfil=None, rodovia=None):
    texto_lower = texto.lower()

    # ============================================================
    # DEFINE UFs PERMITIDAS (FILTRO INTELIGENTE)
    # ============================================================

    ufs_permitidas = None

    ufs_perfil = PERFIL_UFS.get(perfil)
    ufs_rodovia = RODOVIA_UFS.get(rodovia)

    if ufs_perfil and ufs_rodovia:
        ufs_permitidas = list(set(ufs_perfil) & set(ufs_rodovia))
    elif ufs_perfil:
        ufs_permitidas = ufs_perfil
    elif ufs_rodovia:
        ufs_permitidas = ufs_rodovia

    # Remove rodovias com nome de cidade
    for nome in RODOVIAS_COM_NOME_DE_CIDADE:
        texto_lower = re.sub(rf'rodovia\s+{nome}', '', texto_lower)

    cidades_contexto = []

    for uf, lista_cidades in CIDADES_BRASIL.items():

        # 🔥 FILTRO POR UF
        if ufs_permitidas and uf not in ufs_permitidas:
            continue

        for cidade in lista_cidades:
            cidade_lower = cidade.lower()

            # ============================================================
            # MATCH INTELIGENTE (NOME COMPLETO + INÍCIO DO NOME)
            # ============================================================

            nome_oficial = cidade_lower

            primeira_parte = (
                nome_oficial
                .split(" de ")[0]
                .split(" da ")[0]
                .split(" do ")[0]
            )

            padroes = [
                r'\b' + re.escape(nome_oficial) + r'\b',   # nome completo
                r'\b' + re.escape(primeira_parte) + r'\b'  # nome abreviado
            ]

            for padrao in padroes:
                for match in re.finditer(padrao, texto_lower):

                    inicio = match.start()
                    trecho_antes = texto_lower[max(0, inicio-40):inicio]

                    if re.search(r'(em|no|na|próximo a|nas proximidades de)\s+$', trecho_antes):
                        prioridade = 1
                    elif re.search(r'(sentido|rumo a|acesso a|ligação com)\s+$', trecho_antes):
                        prioridade = 3
                    else:
                        prioridade = 2

                    cidades_contexto.append((cidade, uf, prioridade, inicio))

    # Ordena por prioridade → tamanho da cidade → posição no texto
    cidades_contexto.sort(key=lambda x: (x[2], -len(x[0]), x[3]))

    cidades_ordenadas = []

    for cidade, uf, _, inicio in cidades_contexto:

        # 🚫 evita cidade contida dentro de outra já aceita
        if any(cidade.lower() in c_existente.lower()
               for c_existente, _ in cidades_ordenadas):
            continue

        cidades_ordenadas.append((cidade, uf))

        if len(cidades_ordenadas) == 4:
            break

    return cidades_ordenadas




# ============================================================
# FUNÇÃO PRINCIPAL
# ============================================================

def processar_texto(texto, perfil):

    # 🔥 REGRA COR
    if perfil == "Centro de Operações Rio":
        return {
            "Data": datetime.date.today().strftime("%d/%m/%Y"),
            "Hora": datetime.datetime.now().strftime("%H:%M:%S"),
            "Tipo_Incidente": definir_tipo_incidente(texto),
            "Perfil": perfil,
            "Tipo_Perfil": "Urbano",
            "KM": "Não informado",
            "Rodovia": "Não informado",
            "Cidade 1": "Rio de Janeiro",
            "Cidade 2": "",
            "Cidade 3": "",
            "Cidade 4": "",
            "UF": "RJ",
            "Local_Referencia": extrair_local_referencia(texto),
            "Texto Completo": texto
        }

    # ============================================================
    # 🔎 IDENTIFICA RODOVIA ANTES DE EXTRAIR CIDADES
    # ============================================================

    rodovia = "Não informado"
    rodovia_match = re.search(r'\b([A-Z]{2}-\d{1,3}(/[A-Z]{2})?)\b', texto)

    if rodovia_match:
        rodovia = rodovia_match.group(1).split("/")[0]
    elif perfil in MAPA_PERFIS:
        rodovia = MAPA_PERFIS[perfil]["rodovia"]

    # ============================================================
    # 🧠 AGORA EXTRAI CIDADES COM FILTRO INTELIGENTE
    # ============================================================

    cidades = extrair_cidades_do_texto(texto, perfil, rodovia)

    cidade_cols = ["", "", "", ""]
    ufs_cidades = set()

    for i, (cidade, uf) in enumerate(cidades):
        cidade_cols[i] = cidade
        ufs_cidades.add(uf)

    # ============================================================
    # DEFINE UF FINAL
    # ============================================================

    ufs_texto = set(re.findall(r'/([A-Z]{2})\b', texto))

    if ufs_texto:
        uf_final = "/".join(sorted(ufs_texto))
    elif ufs_cidades:
        uf_final = "/".join(sorted(ufs_cidades))
    else:
        uf_final = "Não informado"

    # ============================================================
    # DEFINE TIPO PERFIL
    # ============================================================

    if perfil in RODOVIARIOS:
        tipo_perfil = "Rodoviário"
    elif perfil in URBANOS:
        tipo_perfil = "Urbano"
    elif perfil in CLIMA:
        tipo_perfil = "Clima"
    else:
        tipo_perfil = "Não informado"

    # ============================================================
    # EXTRAI KM
    # ============================================================

    km = "Não informado"
    km_matches = re.findall(r'km\s*(\d{1,4})', texto.lower())
    if km_matches:
        km = "-".join(km_matches)

    # ============================================================
    # RETORNO FINAL
    # ============================================================

    return {
        "Data": datetime.date.today().strftime("%d/%m/%Y"),
        "Hora": datetime.datetime.now().strftime("%H:%M:%S"),
        "Tipo_Incidente": definir_tipo_incidente(texto),
        "Perfil": perfil,
        "Tipo_Perfil": tipo_perfil,
        "KM": km,
        "Rodovia": rodovia,
        "Cidade 1": cidade_cols[0],
        "Cidade 2": cidade_cols[1],
        "Cidade 3": cidade_cols[2],
        "Cidade 4": cidade_cols[3],
        "UF": uf_final,
        "Local_Referencia": "",
        "Texto Completo": texto
    }

















