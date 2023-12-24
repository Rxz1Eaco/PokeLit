import streamlit as st

st.set_page_config(page_title="Pokédex:")
st.write("## Pokédex:")

df_pokemon = st.session_state["data"]

name = df_pokemon["english_name"].unique()
nome_pokemon = st.sidebar.selectbox("Nome Pokémon", name)
# Filtrar o DataFrame para o Pokémon selecionado
pokemon_selecionado = df_pokemon[df_pokemon["english_name"] == nome_pokemon]

# Obter a geração correspondente ao Pokémon selecionado
gen_pokemon = pokemon_selecionado["gen"].values[0]
national = df_pokemon[df_pokemon["english_name"] == nome_pokemon][
    "national_number"
].unique()


# Obtendo os tipo  correspondente ao Pokémon selecionado
ptype = df_pokemon[df_pokemon["english_name"] == nome_pokemon]["primary_type"].unique()
stype = df_pokemon[df_pokemon["english_name"] == nome_pokemon][
    "secondary_type"
].unique()

# Obtendo os gêneros  correspondente ao Pokémon selecionado
male = df_pokemon[df_pokemon["english_name"] == nome_pokemon]["percent_male"].unique()
female = df_pokemon[df_pokemon["english_name"] == nome_pokemon][
    "percent_female"
].unique()


# Obtendo os hp,attack,defense,sp_attack,sp_defense,speed correspondente ao Pokémon selecionado
hp = pokemon_selecionado["hp"].values[0]
attack = pokemon_selecionado["attack"].values[0]
defense = pokemon_selecionado["defense"].values[0]
sp_attack = pokemon_selecionado["sp_attack"].values[0]
sp_defense = pokemon_selecionado["sp_defense"].values[0]
speed = pokemon_selecionado["speed"].values[0]


# Obtendo todas as fraquezas correspondente ao Pokémon selecionado
against_normal = pokemon_selecionado["against_normal"].values[0]
against_fire = pokemon_selecionado["against_fire"].values[0]
against_water = pokemon_selecionado["against_water"].values[0]
against_electric = pokemon_selecionado["against_electric"].values[0]
against_grass = pokemon_selecionado["against_grass"].values[0]
against_ice = pokemon_selecionado["against_ice"].values[0]
against_fighting = pokemon_selecionado["against_fighting"].values[0]
against_poison = pokemon_selecionado["against_poison"].values[0]
against_ground = pokemon_selecionado["against_ground"].values[0]
against_flying = pokemon_selecionado["against_flying"].values[0]
against_psychic = pokemon_selecionado["against_psychic"].values[0]
against_bug = pokemon_selecionado["against_bug"].values[0]
against_rock = pokemon_selecionado["against_rock"].values[0]
against_ghost = pokemon_selecionado["against_dragon"].values[0]
against_dragon = pokemon_selecionado["against_normal"].values[0]
against_dark = pokemon_selecionado["against_dark"].values[0]
against_steel = pokemon_selecionado["against_steel"].values[0]
against_fairy = pokemon_selecionado["against_fairy"].values[0]

st.markdown(f"### **Nome Pokémon:** {nome_pokemon}")  # Apresentando o Nome do Pokémon

col_national, col_gen = st.columns(2)
col_national.markdown(
    f"##### **Número Pokédex:** {national[0]}"
)  # Apresentando a Geração do Pokémon
col_gen.markdown(
    f"##### **Geração:** {gen_pokemon}"
)  # Apresentando a Geração do Pokémon

col_ptype, col_stype = st.columns(2)
col_ptype.markdown(
    f"##### **Primerio Tipo:** {ptype[0]}"
)  # Apresentando o Primeiro Tipo do Pokémon
col_stype.markdown(
    f"##### **Segundo Tipo:** {stype[0]}"
)  # Apresentando o Segundo Tipo do Pokémon

col_male, col_female = st.columns(2)
col_male.markdown(
    f"##### **Porcentagem Masculino:** {male[0]}"
)  # Apresentando a Porcentagem Masculino do Pokémon
col_female.markdown(
    f"##### **Porcentagem Feminina:** {female[0]}"
)  # Apresentando a Porcentagem Feminina do Pokémon

st.markdown(f"### **Status base:**")

col_hp, col_attack, col_defense = st.columns(3)
col_hp.markdown(f"##### **Hp:** {hp}")  # Apresentando a HP do Pokémon
col_attack.markdown(f"##### **Attack:** {attack}")  # Apresentando o ATTACK do Pokémon
col_defense.markdown(
    f"##### **Defense:** {defense}"
)  # Apresentando o DEFENSE do Pokémon

col_speed, col_sp_attack, col_sp_defense = st.columns(3)
col_speed.markdown(
    f"##### **Speed:** {speed}"
)  # Apresentando o SUPER DEFENSE do Pokémon
col_sp_attack.markdown(
    f"##### **Sp Attack:** {sp_attack}"
)  # Apresentando o SUPER ATTACK do Pokémon
col_sp_defense.markdown(
    f"##### **Sp Defense:** {sp_defense}"
)  # Apresentando o SUPER DEFENSE do Pokémon

st.markdown(f"### **Fraquezas:**")
col_against_normal, col_against_fire, col_against_water = st.columns(3)
col_against_normal.markdown(f"##### **Contra Normal:** {against_normal}")
col_against_fire.markdown(f"##### **Contra Fire🔥:** {against_fire}")
col_against_water.markdown(f"##### **Contra Água💧:** {against_water}")

col_against_electric, col_against_grass, col_against_ice = st.columns(3)
col_against_electric.markdown(f"##### **Contra Életrico⚡:** {against_electric}")
col_against_grass.markdown(f"#####  **Contra Grama🌱:** {against_grass}")
col_against_ice.markdown(f"##### **Contra Gelo🧊:** {against_ice}")

col_against_fighting, col_against_poison, col_against_ground = st.columns(3)
col_against_fighting.markdown(f"##### **Contra Lutador🥋:** {against_fighting}")
col_against_poison.markdown(f"##### **Contra Venososo☣️:** {against_poison}")
col_against_ground.markdown(f"##### **Contra Terra:** {against_ground}")

col_against_flying, col_against_psychic, col_against_bug = st.columns(3)
col_against_flying.markdown(f"##### **Contra Voador🐦:** {against_flying}")
col_against_psychic.markdown(f"##### **Contra Psíquico🔮:** {against_psychic}")
col_against_bug.markdown(f"##### **Contra Inseto🐛:** {against_bug}")

col_against_rock, col_against_ghost, col_against_dragon = st.columns(3)
col_against_rock.markdown(f"##### **Contra Pedra:** {against_ground}")
col_against_ghost.markdown(f"##### **Contra Fantasma👻:** {against_flying}")
col_against_dragon.markdown(f"##### **Contra Dragão🐉:** {against_psychic}")

col_against_dark, col_against_steel, col_against_fairy = st.columns(3)
col_against_dark.markdown(f"##### **Contra Sombrio🌃:** {against_bug}")
col_against_steel.markdown(f"##### **Contra Metal ⛓️:** {against_steel}")
col_against_fairy.markdown(f"##### **Contra Fada🦄:** {against_fairy}")
