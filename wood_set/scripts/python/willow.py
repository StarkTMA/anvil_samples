"""The willow wood set: a complete wood set with a tree its saplings grow into, and
leaves that sometimes drop sticks.

Textures: the `willow_*` textures in `assets/bbmodels/wood_set.bbmodel` and
`wood_set_boat.bbmodel`, and the item icons `willow_door`, `willow_sign`,
`willow_hanging_sign`, `willow_boat` and `willow_chest_boat` in `assets/textures/items`.
"""

from anvil.api.features import TreeFeature
from anvil.api.vanilla.blocks import MinecraftBlockTypes
from anvil.api.vanilla.items import MinecraftItemTypes
from anvil.kit.blocks.wood_set import WoodSet

STICK_CHANCE = 0.02
"""The chance that a leaf drops a stick when it is broken or decays."""


def create_willow_tree(willow: WoodSet) -> TreeFeature:
    """A small tree like an oak: a straight willow log trunk under a layered canopy.

    Its leaves are placed natural, so they decay once the trunk is cut.
    """
    log = willow["log"].block
    leaves = willow["leaves"].block
    tree = (
        TreeFeature("willow_tree")
        .trunk(log, trunk_height=(5, 7))
        .canopy(
            leaves.descriptor(natural=True),
            min_width=0,
            canopy_offset_min=-3,
            canopy_offset_max=0,
            slope_rise=1,
            slope_run=2,
            variation_chance=[(1, 2), (1, 2), (1, 2), (1, 1)],
        )
        .may_grow_on(
            [
                MinecraftBlockTypes.Dirt(),
                MinecraftBlockTypes.GrassBlock(),
                MinecraftBlockTypes.Podzol(),
            ]
        )
        .may_replace([MinecraftBlockTypes.Air(), leaves])
    )
    tree.queue()
    return tree


def register_willow() -> WoodSet:
    """Builds and queues the willow wood set and its tree."""
    return (
        WoodSet("willow")
        .tree(create_willow_tree)
        .leaf_drop(MinecraftItemTypes.Stick(), STICK_CHANCE)
        .build()
    )
