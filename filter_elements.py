import pandas as pd

df = pd.read_csv("pokemon.csv")

df = df[
    [
        "against_bug",
        "against_dark",
        "against_dragon",
        "against_electric",
        "against_fairy",
        "against_fight",
        "against_fire",
        "against_flying",
        "against_ghost",
        "against_grass",
        "against_ground",
        "against_ice",
        "against_normal",
        "against_poison",
        "against_psychic",
        "against_rock",
        "against_steel",
        "against_water",
        "type1",
    ]
]

df.to_csv("pokemon_filte.csv")
