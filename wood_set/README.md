# Wood Set

Two complete custom wood types built with the Anvil wood set kit, `anvil.kit.blocks.wood_set`.

- **Maple**: the whole set from one call, without saplings, so it needs no tree.
- **Willow**: the whole set, with a tree its saplings grow into, and leaves that sometimes drop sticks.

## What you get

For each wood: planks, logs, stripped logs, wood, stripped wood, stairs, slabs, fences, fence gates, doors, trapdoors, buttons, pressure plates, signs, hanging signs, leaves, boats and chest boats, plus saplings for willow. Recipes, vanilla wood tags, fuel values and creative menu placement are included.

The blocks behave like vanilla wood: doors and trapdoors open, slabs stack into double slabs, axes strip logs, signs can be edited, leaves decay once their log is gone, and saplings grow into the tree.

## The code

[`scripts/python/maple.py`](scripts/python/maple.py): one call.

```python
create_wood_set("maple", WoodBlock.SAPLING)
```

`WoodBlock.SAPLING` leaves the saplings out. A set with saplings needs the tree they grow into.

[`scripts/python/willow.py`](scripts/python/willow.py): a tree and a leaf drop.

```python
WoodSet("willow").tree(create_willow_tree).leaf_drop("minecraft:stick", STICK_CHANCE).build()
```

`create_willow_tree` receives the built set and makes a `TreeFeature` from its log and leaves. The leaves are placed with their `natural` state on, so they decay when the trunk is cut.

[`scripts/python/main.py`](scripts/python/main.py) registers both sets and compiles the project.

[`scripts/javascript/main.ts`](scripts/javascript/main.ts) registers the scripts the blocks use (doors, signs, slabs, stripping, leaves, saplings, boats):

```ts
system.beforeEvents.startup.subscribe((init) => {
	registerWoodSet(init);
});
```

The signs use `@minecraft/server-ui`, so `scriptui` is on in `anvilconfig.json`.

## Textures

All wood sets share two Blockbench models:

- `assets/bbmodels/wood_set.bbmodel`: the blocks, with the `maple_*` and `willow_*` textures
- `assets/bbmodels/wood_set_boat.bbmodel`: both boats

The item icons are in `assets/textures/items`: `<wood>_door`, `<wood>_sign`, `<wood>_hanging_sign`, `<wood>_boat`, `<wood>_chest_boat`, and `willow_sapling`.

The textures in this sample were generated with math functions: noise and sine patterns on fixed colour palettes.

## Make your own wood

1. Pick a name, for example `ash`, and call `create_wood_set("ash", WoodBlock.SAPLING)`, or build a `WoodSet` with a tree.
2. In Blockbench, add the `ash_*` textures to `wood_set.bbmodel` and `ash_boat` to `wood_set_boat.bbmodel`, named like the maple ones.
3. Add the `ash_*` item icons to `assets/textures/items`.
4. Run `anvil build`.

In a new project, the first build copies Anvil's base models into `assets/bbmodels` for you to paint.

## Build

```bash
npm install
anvil build
```

See the [kit documentation](https://anvil.starktma.net/kit/) for every option: leaving parts out, map colours, sound groups, a creative tab of its own, and more.
