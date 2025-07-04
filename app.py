import streamlit as st

# Sample minion card pool
minion_card_pool = {
    'block_ranged': {'name': 'Block Ranged', 'type': 'defense', 'counter': 'ranged'},
    'reflect_magic': {'name': 'Reflect Magic', 'type': 'defense', 'counter': 'magic'},
    'dodge_melee': {'name': 'Dodge Melee', 'type': 'defense', 'counter': 'melee'},
    'rush_attack': {'name': 'Rush Attack', 'type': 'offense', 'focus': 'aggression'},
    'drain_life': {'name': 'Drain Life', 'type': 'offense', 'focus': 'magic'},
}

# AI logic
def build_minion_deck(player_deck, card_pool):
    minion_deck = []

    if player_deck['ranged'] >= 3:
        minion_deck.append(card_pool['block_ranged'])
    if player_deck['magic'] >= 2:
        minion_deck.append(card_pool['reflect_magic'])

    minion_deck.append(card_pool['rush_attack'])

    return minion_deck

# Streamlit UI
st.title("Minion AI Deck Builder")
st.write("Enter player deck stats to generate a counter minion deck.")

ranged = st.slider("Ranged Cards", 0, 10, 3)
melee = st.slider("Melee Cards", 0, 10, 1)
magic = st.slider("Magic Cards", 0, 10, 2)
defense = st.slider("Defense Cards", 0, 10, 0)

player_deck = {
    'ranged': ranged,
    'melee': melee,
    'magic': magic,
    'defense': defense
}

if st.button("Generate Minion Deck"):
    minion_deck = build_minion_deck(player_deck, minion_card_pool)

    st.subheader("Generated Minion Deck")
    for card in minion_deck:
        st.markdown(f"- **{card['name']}** ({card['type']})")
