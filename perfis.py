# ============================================================
# LISTAS DE PERFIS
# ============================================================

# Perfis Rodoviários
RODOVIARIOS = [
    "Arteris Litoral Sul",
    "Arteris Fluminense",
    "Arteris Fernão Dias",
    "Arteris ViaPaulista",
    "Arteris Régis Bittencourt",
    "Arteris Intervias",
    "Arteris Planalto Sul",
    "DER-SP",
    "Ecovias Imigrantes",
    "Ecovias Cerrado",
    "Triunfo Concebra",
    "Rodovias Paraná",
    "Cia de Concessão Rodoviária Juiz de Fora - Rio",
    "Rota das Bandeiras",
    "EPR Litoral Pioneiro",
    "eprviamineira",
    "PRF MINAS GERAIS"
]

# Perfis Urbanos
URBANOS = [
    "Centro de Operações Rio"
]

# Perfis Clima / Meteorologia
CLIMA = [
    "INMET"
]

# ============================================================
# MAPA INTELIGENTE DE PERFIS
# Quando rodovia/UF não vier no texto
# ============================================================

MAPA_PERFIS = {
    "Arteris Litoral Sul": {"rodovia": "BR-116/PR, BR-376/PR, BR-101/SC, CFN", "uf": "PR/SC"},
    "Arteris Fluminense": {"rodovia": "BR-101", "uf": "RJ"},
    "Arteris Fernão Dias": {"rodovia": "BR-381", "uf": "SP/MG"},
    "Arteris ViaPaulista": {"rodovia": "SP-249, SP-255, SP-257, SP-281, SP-304, SP-318, SP-328, SP-330, SP-334, SP-345", "uf": "SP"},
    "Arteris Régis Bittencourt": {"rodovia": "BR-116", "uf": "SP/PR"},
    "Arteris Intervias": {"rodovia": "SP-215, SP-330, SP-147, SP-191, SP-352, SPI-165, SPI-054", "uf": "SP"},
    "Arteris Planalto Sul": {"rodovia": "BR-116", "uf": "PR/SC"},
    "DER-SP": {"rodovia": "Rodovias Estaduais SP", "uf": "SP"},
    "Ecovias Imigrantes": {"rodovia": "SP-160, SP-248, SP-055", "uf": "SP"},
    "Ecovias Cerrado": {"rodovia": "BR-364, BR-365", "uf": "GO/MG"},
    "Triunfo Concebra": {"rodovia": "BR-060, BR-153, BR-262", "uf": "GO/MG/DF"},
    "Rodovias Paraná": {"rodovia": "Rodovias Estaduais PR", "uf": "PR"},
    "Cia de Concessão Rodoviária Juiz de Fora - Rio": {"rodovia": "BR-040", "uf": "RJ/MG"},
    "Rota das Bandeiras": {"rodovia": "SP-340, SP-348, SP-330, SP-065", "uf": "SP"},
    "EPR Litoral Pioneiro": {"rodovia": "BR-277, PR-092, PR-151, PR-239, PR-407, PR-508", "uf": "PR"},
    "eprviamineira": {"rodovia": "BR-040", "uf": "MG"},
    "PRF MINAS GERAIS": {"rodovia": "Rodovias Federais", "uf": "MG"}
}

# ============================================================
# PERFIL → UFs PERMITIDAS
# ============================================================

PERFIL_UFS = {
    "Arteris Litoral Sul": ["PR", "SC"],
    "Arteris Fluminense": ["RJ"],
    "Arteris Fernão Dias": ["SP", "MG"],
    "Arteris ViaPaulista": ["SP"],
    "Arteris Régis Bittencourt": ["SP", "PR"],
    "Arteris Intervias": ["SP"],
    "Arteris Planalto Sul": ["PR", "SC"],
    "DER-SP": ["SP"],
    "Ecovias Imigrantes": ["SP"],
    "Ecovias Cerrado": ["GO", "MG"],
    "Triunfo Concebra": ["GO", "MG", "DF"],
    "Rodovias Paraná": ["PR"],
    "Cia de Concessão Rodoviária Juiz de Fora - Rio": ["RJ", "MG"],
    "Rota das Bandeiras": ["SP"],
    "EPR Litoral Pioneiro": ["PR"],
    "eprviamineira": ["MG"],
    "PRF MINAS GERAIS": ["MG"]
}


# ============================================================
# RODOVIA → UFs POSSÍVEIS
# ============================================================

RODOVIA_UFS = {

    # Federais
    "BR-101": ["RJ", "SC"],
    "BR-116": ["SP", "PR", "SC", "MG"],
    "BR-376": ["PR"],
    "BR-381": ["SP", "MG"],
    "BR-364": ["GO", "MG"],
    "BR-365": ["GO", "MG"],
    "BR-060": ["GO", "DF"],
    "BR-153": ["GO", "MG"],
    "BR-262": ["MG"],
    "BR-277": ["PR"],
    "BR-040": ["RJ", "MG"],

    # Estaduais SP
    "SP-160": ["SP"],
    "SP-248": ["SP"],
    "SP-055": ["SP"],
    "SP-249": ["SP"],
    "SP-255": ["SP"],
    "SP-257": ["SP"],
    "SP-281": ["SP"],
    "SP-304": ["SP"],
    "SP-318": ["SP"],
    "SP-328": ["SP"],
    "SP-330": ["SP"],
    "SP-334": ["SP"],
    "SP-345": ["SP"],
    "SP-215": ["SP"],
    "SP-147": ["SP"],
    "SP-191": ["SP"],
    "SP-352": ["SP"],
    "SPI-165": ["SP"],
    "SPI-054": ["SP"],
    "SP-340": ["SP"],
    "SP-348": ["SP"],
    "SP-065": ["SP"],

    # Estaduais PR
    "PR-092": ["PR"],
    "PR-151": ["PR"],
    "PR-239": ["PR"],
    "PR-407": ["PR"],
    "PR-508": ["PR"],

}


