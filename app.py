import streamlit as st
from datetime import date

# Configurações da página
st.set_page_config(
    page_title="Bloom",
    page_icon="🌸",
    layout="wide"
)

st.title("🌸 Bloom")

# Mensagem
st.header("Bem-vinda, Hellen! 💙")

st.subheader("🌱 Adicione um novo hábito")

hoje = str(date.today())

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


