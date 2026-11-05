# Anvil Samples

Free sample projects for [Anvil](https://github.com/StarkTMA/Anvil), the Python framework for Minecraft Bedrock add-ons. Each folder is a complete Anvil project you can build as is, read, and copy into your own add-ons.

## Samples

| Sample | What it shows |
| --- | --- |
| [Wood Set](wood_set/) | Two complete custom wood types from `anvil.kit.blocks.wood_set`: maple from one call, and willow with its own tree and leaves that drop sticks. |

## Requirements

- [Python 3.15](https://www.python.org/downloads/) or newer
- [Node.js](https://nodejs.org/), for the Script API bundle
- Anvil 1.0.1 or newer:

```bash
pip install mcanvil
```

## Building a sample

```bash
git clone https://github.com/StarkTMA/anvil_samples.git
cd anvil_samples/wood_set
npm install
anvil build
```

Anvil writes the behavior and resource packs into Minecraft's development pack folders. Each sample's README explains what to look at in game.

## Learn more

- [Anvil documentation](https://anvil.starktma.net)
- [Anvil on GitHub](https://github.com/StarkTMA/Anvil)

## License

Everything in this repository, code and assets, is under the [MIT License](LICENSE): use it in your own add-ons, free or paid.
