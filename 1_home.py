import streamlit as st
import pandas as pd
import webbrowser

if "data" not in st.session_state:
    df_pokemon = pd.read_excel("database/pokemon.xlsx")
    st.session_state["data"] = df_pokemon

st.set_page_config(page_title="Pókemon Dashboard")
st.write("## Pokémon Database Official ❄️🔥💧")
st.sidebar.markdown("[Desenvolvido por Rxz1Eaco](https://github.com/Rxz1Eaco)")
btn = st.button("Acesse a minha base de dados")
if btn:
    webbrowser.open_new_tab(
        "https://drive.google.com/drive/folders/1AfHJ-kEzj21-nAjz4yBP2lBWeVMlVzhG?usp=sharing"
    )

# st.image("https://kanto.legiaodosherois.com.br/w750-q95-k1/wp-content/uploads/2021/10/legiao_gEQ9YRsnFa3I.jpg.webp",caption="Imagem Pókemon",use_column_width=True,)
st.image(
    "https://media.tenor.com/rN2I0a3XqeAAAAAC/pokemon-pikachu.gif",
    caption="Imagem Pókemon",
    width=400,
    use_column_width=True,
)

st.write(
    "Este conjunto de dados contém informações sobre todos os 802 Pokémon de todas as Sete Gerações de Pokémon. As informações contidas neste conjunto de dados incluem estatísticas básicas, desempenho em relação a outros tipos, altura, peso, classificação, etapas do ovo, pontos de experiência, habilidades, etc.As informações foram extraídas de http://serebii.net/"
)
