# Importações
import streamlit as st
from datetime import date

# Configurações da página
st.set_page_config(
    page_title="Bloom",
    page_icon="🌸",
    layout="wide"
)

# Mensagem

st.title("🌸 Bloom")

st.header("Bem-vinda, Hellen! 💙")

st.subheader("🌱 Adicione um novo hábito")

# Variaveis  gerais
hoje = str(date.today())


# Funções
def calcular_dias_seguidos(datas):
    if not datas:
        return 0
    datas = sorted(datas)
    ultima_data = datas[-1]   
    dias_desde_ultima = hoje - ultima_data
    if dias_desde_ultima.days > 1:
        return 0

    data_anterior = None
    total = 1

    for data in datas:
        if data_anterior is None:
            data_anterior = data
        else:
            sequencia = data - data_anterior
            if sequencia.days == 1:
                total += 1
            else: 
                total = 1
        data_anterior = data
    return total
st.write(calcular_dias_seguidos([]))
# Dados iniciais dos habitos
if "habitos" not in st.session_state: st.session_state["habitos"]  = {
    "Academia": {
        "datas": [],
        "categoria": "Saúde",
        "meta_semanal": 1,
        "dias_seguidos": 0,
        "criado_em": hoje
    },

    "Python": {
        "datas": [],
        "categoria": "Estudo",
        "meta_semanal": 1,
        "dias_seguidos": 0,
        "criado_em": hoje
    },

    "Dados": {
        "datas": [],
        "categoria": "Estudo",
        "meta_semanal": 1,
        "dias_seguidos": 0,
        "criado_em": hoje
    }
}


# ==========================
# NOVO HÁBITO
# ==========================
novo_habito = st.text_input("Novo hábito")

clicou = st.button("Adicionar")

if clicou:
    if novo_habito == "":
        st.write("⚠ Digite um hábito antes de adicionar.")
    elif novo_habito in st.session_state["habitos"]:
        st.write("⚠ Esse hábito já foi incluído.")
    else:
        st.session_state["habitos"][novo_habito] = {
    "datas": [],
    "categoria": "Outros",
    "meta_semanal": 1,
    "dias_seguidos": 0,
    "criado_em": hoje
}


total = 0
habito_excluir = None

for habito in st.session_state["habitos"]: 
    col1, col2 = st.columns(2) 
    with col1: 
        resposta = st.checkbox(habito, key=f"check_{habito}" ) 
    with col2: 
        if st.button( "🗑️", key=f"excluir_{habito}" ): 
            habito_excluir = habito
    if resposta:
        if hoje not in st.session_state["habitos"][habito]["datas"]: 
            st.session_state["habitos"][habito]["datas"].append(hoje)
        total += 1
    else:
       if hoje in habito["datas"]:
            [habito]["datas"].remove(hoje) 
if habito_excluir is not None: 
    st.session_state["habitos"].pop(habito_excluir) 
    st.rerun()



st.write(f"Você concluiu {total} hábitos hoje!")

st.divider()

st.write("### Resultado")

st.divider()
st.subheader(f"🌱 Você concluiu {total} hábitos hoje!")

if total == 0:
    st.write("Vamos começar a cultivar bons hábitos! 🌱")
elif total <= 3:
    st.write("Bom trabalho! Continue assim! 🌿")
else:
    st.write("Excelente! Você está florescendo! 🌸")

st.write("TESTE - Datas registradas: ")
st.write(st.session_state["habitos"])