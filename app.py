import streamlit as st
from datetime import datetime, timedelta

# Sample minion card pool with weights
minion_card_pool = [
    {'name': 'Block Ranged', 'type': 'defense', 'counter': 'ranged', 'weight': 0},
    {'name': 'Reflect Magic', 'type': 'defense', 'counter': 'magic', 'weight': 0},
    {'name': 'Dodge Melee', 'type': 'defense', 'counter': 'melee', 'weight': 0},
    {'name': 'Rush Attack', 'type': 'offense', 'focus': 'aggression', 'weight': 0},
    {'name': 'Drain Life', 'type': 'offense', 'focus': 'magic', 'weight': 0},
]

# Weighted AI logic (Tier 2)
def build_minion_deck_weighted(player_deck, card_pool):
    for card in card_pool:
        weight = 0
        if 'counter' in card:
            weight = player_deck.get(card['counter'], 0)
        elif 'focus' in card:
            if card['focus'] == 'magic':
                weight = player_deck.get('magic', 0)
            elif card['focus'] == 'aggression':
                weight = player_deck.get('ranged', 0)
        card['weight'] = weight

    sorted_cards = sorted(card_pool, key=lambda c: c['weight'], reverse=True)
    return sorted_cards[:3]  # Top 3 cards

# Daylight timer session state
if 'start_time' not in st.session_state:
    st.session_state.start_time = datetime.now()
    st.session_state.end_time = st.session_state.start_time + timedelta(minutes=30)

# Sidebar: Daylight timer
st.sidebar.header("🌞 Daylight Timer")
now = datetime.now()
time_left = st.session_state.end_time - now

if time_left.total_seconds() > 0:
    mins, secs = divmod(int(time_left.total_seconds()), 60)
    st.sidebar.success(f"Time left: {mins}m {secs}s")
    if time_left.total_seconds() <= 600:
        st.sidebar.warning("⚠️ 10-minute warning!")
else:
    st.sidebar.error("🌒 Time is up! Night has fallen!")

# Main UI
st.title("Minion AI Deck Builder (Tier 2: Weighted AI)")
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
    minion_deck = build_minion_deck_weighted(player_deck, minion_card_pool)

    st.subheader("Generated Minion Deck")
    for card in minion_deck:
        st.markdown(f"- **{card['name']}** ({card['type']}) — weight: {card['weight']}")
