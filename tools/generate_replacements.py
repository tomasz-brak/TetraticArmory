import json
from typing import Callable


tetra_data_url = "src/main/resources/data/tetra"

########################
# DEFINE DEFAULT PARTS #
########################

boots = lambda material: {
    "predicate": {
        "items": [f"minecraft:{material if not material == 'gold' else 'golden'}_boots"]
    },
    "item": "tetratic_armory:modular_boots",
    "modules": {
        "boots/foot_left": ["boots/basic_foot_left", f"basic_foot/{material}"],
        "boots/foot_right": ["boots/basic_foot_right", f"basic_foot/{material}"],
    },
}
boots.__name__ = "boots"


leggings = lambda material: {
    "predicate": {
        "items": [
            f"minecraft:{material if not material == 'gold' else 'golden'}_leggings"
        ]
    },
    "item": "tetratic_armory:modular_leggings",
    "modules": {
        "leggings/leg_left": ["leggings/basic_leg_left", f"basic_leg/{material}"],
        "leggings/leg_right": ["leggings/basic_leg_right", f"basic_leg/{material}"],
    },
}
leggings.__name__ = "leggings"


chestplate = lambda material: {
    "predicate": {
        "items": [
            f"minecraft:{material if not material == 'gold' else 'golden'}_chestplate"
        ]
    },
    "item": "tetratic_armory:modular_chestplate",
    "modules": {
        "chestplate/breastplate": [
            "chestplate/basic_breastplate",
            f"basic_breastplate/{material}",
        ],
        "chestplate/pauldron_left": [
            "chestplate/pauldron_left",
            f"pauldron_left/{material}",
        ],
        "chestplate/pauldron_right": [
            "chestplate/pauldron_right",
            f"pauldron_right/{material}",
        ],
    },
}
chestplate.__name__ = "chestplates"


helmet = lambda material: {
    "predicate": {
        "items": [
            f"minecraft:{material if not material == 'gold' else 'golden'}_helmet"
        ]
    },
    "item": "tetratic_armory:modular_helmet",
    "modules": {
        "helmet/skull": ["helmet/basic_skull", f"basic_skull/{material}"]
    },  ### overide if turle = true
}
helmet.__name__ = "helmets"

####################
# DEFINE MATERIALS #
####################

generic_materials = ["leather", "chainmail", "iron", "gold", "diamond", "netherite"]

part_materials: dict[Callable, list[str]] = {
    helmet: generic_materials + ["turtle"],
    chestplate: generic_materials + [],
    leggings: generic_materials + [],
    boots: generic_materials + [],
}


#####################
# RUN THE GENERATOR #
#####################

for part, materials in part_materials.items():
    items = []
    for material in materials:
        items.append(part(material))
    #############
    # OVERRIDES #
    #############

    # Change Scute
    if part.__name__ == "helmets":
        items[items.index(helmet("turtle"))]["modules"] = {
            "helmet/skull": ["helmet/basic_skull", f"basic_skull/turtle_scute"]
        }

    with open(f"{tetra_data_url}/replacements/{part.__name__}.json", "w") as file:

        json.dump(items, file, indent=4)
