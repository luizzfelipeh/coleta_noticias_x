import tkinter as tk
from tkinter import scrolledtext, messagebox

from motor_extracao import processar_texto
from contexto_perfis import CONTEXT_PERFIS
from salvamento import salvar_ocorrencia
from gerador_noticia import gerar_noticia

# ============================================================
# VARIÁVEL GLOBAL PARA GUARDAR RESULTADO TEMPORÁRIO
# ============================================================

resultado_atual = None


# ============================================================
# PROCESSAR (NÃO SALVA)
# ============================================================

def processar():
    global resultado_atual

    texto = entrada_texto.get("1.0", tk.END).strip()
    perfil_input = entrada_perfil.get().strip()

    if not texto or not perfil_input:
        messagebox.showwarning("Atenção", "Preencha o texto e o perfil!")
        return

    perfil_final = CONTEXT_PERFIS.get(perfil_input, perfil_input)

    resultado = processar_texto(texto, perfil_final)
    resultado_atual = resultado

    # Preenche campos editáveis
    entry_cidade1.delete(0, tk.END)
    entry_cidade1.insert(0, resultado["Cidade 1"])

    entry_cidade2.delete(0, tk.END)
    entry_cidade2.insert(0, resultado["Cidade 2"])

    entry_cidade3.delete(0, tk.END)
    entry_cidade3.insert(0, resultado["Cidade 3"])

    entry_cidade4.delete(0, tk.END)
    entry_cidade4.insert(0, resultado["Cidade 4"])

    entry_uf.delete(0, tk.END)
    entry_uf.insert(0, resultado["UF"])

    entry_rodovia.delete(0, tk.END)
    entry_rodovia.insert(0, resultado["Rodovia"])

    entry_km.delete(0, tk.END)
    entry_km.insert(0, resultado["KM"])

    # Atualiza notícia
    noticia = gerar_noticia(resultado)
    campo_noticia.config(state=tk.NORMAL)
    campo_noticia.delete("1.0", tk.END)
    campo_noticia.insert(tk.END, noticia)
    campo_noticia.config(state=tk.DISABLED)

    messagebox.showinfo("Processado", "Revise os campos antes de registrar.")


# ============================================================
# REGISTRAR (AGORA SIM SALVA)
# ============================================================

def registrar():
    global resultado_atual

    if not resultado_atual:
        messagebox.showwarning("Atenção", "Nenhuma ocorrência processada.")
        return

    # Atualiza dicionário com valores editados
    resultado_atual["Cidade 1"] = entry_cidade1.get()
    resultado_atual["Cidade 2"] = entry_cidade2.get()
    resultado_atual["Cidade 3"] = entry_cidade3.get()
    resultado_atual["Cidade 4"] = entry_cidade4.get()
    resultado_atual["UF"] = entry_uf.get()
    resultado_atual["Rodovia"] = entry_rodovia.get()
    resultado_atual["KM"] = entry_km.get()

    salvar_ocorrencia(resultado_atual)

    messagebox.showinfo("Sucesso", "Ocorrência registrada com sucesso!")

    limpar_campos()


# ============================================================
# LIMPAR
# ============================================================

def limpar_campos():
    global resultado_atual
    resultado_atual = None

    entrada_texto.delete("1.0", tk.END)
    entrada_perfil.delete(0, tk.END)

    for entry in [
        entry_cidade1, entry_cidade2, entry_cidade3, entry_cidade4,
        entry_uf, entry_rodovia, entry_km
    ]:
        entry.delete(0, tk.END)

    campo_noticia.config(state=tk.NORMAL)
    campo_noticia.delete("1.0", tk.END)
    campo_noticia.config(state=tk.DISABLED)


# ============================================================
# INTERFACE
# ============================================================

root = tk.Tk()
root.title("Coleta X 5.1 — Revisão Inteligente")
root.geometry("900x950")

# Texto
tk.Label(root, text="Texto:").pack(anchor="w", padx=10, pady=(10, 0))
entrada_texto = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=8)
entrada_texto.pack(fill=tk.BOTH, padx=10, pady=5)

# Perfil
tk.Label(root, text="Perfil (@ ou nome completo):").pack(anchor="w", padx=10, pady=(10, 0))
entrada_perfil = tk.Entry(root)
entrada_perfil.pack(fill=tk.X, padx=10, pady=5)

# Botões
frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="Processar", command=processar).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botoes, text="Registrar", command=registrar).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botoes, text="Limpar", command=limpar_campos).pack(side=tk.LEFT, padx=5)

# Campos editáveis
tk.Label(root, text="Revisão Manual:").pack(anchor="w", padx=10, pady=(10, 0))

def criar_campo(label_texto):
    frame = tk.Frame(root)
    frame.pack(fill=tk.X, padx=10, pady=2)
    tk.Label(frame, text=label_texto, width=15, anchor="w").pack(side=tk.LEFT)
    entry = tk.Entry(frame)
    entry.pack(fill=tk.X, expand=True)
    return entry

entry_cidade1 = criar_campo("Cidade 1")
entry_cidade2 = criar_campo("Cidade 2")
entry_cidade3 = criar_campo("Cidade 3")
entry_cidade4 = criar_campo("Cidade 4")
entry_uf = criar_campo("UF")
entry_rodovia = criar_campo("Rodovia")
entry_km = criar_campo("KM")

# Notícia
tk.Label(root, text="Notícia pronta para WhatsApp:").pack(anchor="w", padx=10, pady=(10, 0))
campo_noticia = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=12, state=tk.DISABLED)
campo_noticia.pack(fill=tk.BOTH, padx=10, pady=5)

root.mainloop()
