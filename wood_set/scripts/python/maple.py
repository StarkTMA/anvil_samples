"""The maple wood set: a complete wood set from one call.

Saplings are left out, so the set needs no tree.

Textures: the `maple_*` textures in `assets/bbmodels/wood_set.bbmodel` and
`wood_set_boat.bbmodel`, and the item icons `maple_door`, `maple_sign`,
`maple_hanging_sign`, `maple_boat` and `maple_chest_boat` in `assets/textures/items`.
"""

from anvil.kit.blocks.wood_set import WoodBlock, WoodSet, create_wood_set


def register_maple() -> WoodSet:
    """Builds and queues every maple block except saplings."""
    return WoodSet("maple", exclude=[WoodBlock.SAPLING]).build()
