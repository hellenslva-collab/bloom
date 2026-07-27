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


habitos = {
    "Academia": {
        "feito": False,
        "categoria": "Saúde",
        "meta": 1,
        "icone": "🌱",
        "dias_seguidos": 0,
        "total_concluido": 0,
        "criado_em": str(date.today())
    },

    "Python": {
        "feito": False,
        "categoria": "Estudo",
        "meta": 1,
        "icone": "🌱",
        "dias_seguidos": 0,
        "total_concluido": 0,
        "criado_em": str(date.today())
    },

    "SQL": {
        "feito": False,
        "categoria": "Estudo",
        "meta": 1,
        "icone": "🌱",
        "dias_seguidos": 0,
        "total_concluido": 0,
        "criado_em": str(date.today())
    }
}

if "habitos" not in st.session_state:
    st.session_state["habitos"] = habitos


novo_habito = st.text_input("Novo hábito")

clicou = st.button("Adicionar")

if clicou:
    if novo_habito == "":
        st.write("⚠ Digite um hábito antes de adicionar.")
    elif novo_habito in st.session_state["habitos"]:
        st.write("⚠ Esse hábito já foi incluído.")
    else:
        st.session_state["habitos"][novo_habito] = {
    "feito": False,
    "categoria": "Outros",
    "meta": 1,
    "icone": "🌱",
    "dias_seguidos": 0,
    "total_concluido": 0,
    "criado_em": str(date.today())
}


total = 0

for habito in st.session_state["habitos"]:
    resposta = st.checkbox(
    habito,
    key=f"check_{habito}"
)
    st.session_state["habitos"][habito]["feito"] = resposta
    if resposta:
	    total += 1
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
