# maykr

## Usage

The `maykr` CLI tool helps you bootstrap and manage your Doom mods. Below are the available commands and their usage:

### Creating a New Mod

To create a new Doom mod, use the `dm new mod` command:

```sh
dm new mod --name <mod_name> [--path <path>] [--no-git] [--decorate] [--debug]
```

* `--name`: The name of the mod (required).
* `--path`: The path where the mod will be created (default: current directory).
* `--no-git`: Do not initialize a Git repository.
* `--decorate`: Use DECORATE instead of ZScript.
* `--debug`: Enable debug logging.

### Creating a New Weapon

To create a new ZScript weapon, use the dm new weapon command:

```sh
dm new weapon --name <weapon_name> [--extend <base_class>] [--mod-path <mod_path>] [--debug]
```


* `--name`: The name of the weapon class (required).
* `--extend`: The base class to extend (default: Weapon).
* `--mod`-path: The path to the mod folder.
* `--debug`: Enable debug logging.

### Creating a New Sprite

To create a new sprite, use the dm new sprite command:

```sh
dm new sprite --name <sprite_name> --width <width> --height <height> [--anim] [--duration <duration>] [--mod-path <mod_path>] [--debug]
```

* `--name`: The name of the sprite (without extension, required).
* `--width`: The width of the sprite (required).
* `--height`: The height of the sprite (required).
* `--anim`: Add the sprite to ANIMDEFS for animation.
* `--duration`: The animation frame duration (default: 4 tics).
* `--mod`-path: The path to the mod folder.
* `--debug`: Enable debug logging.

### Creating a New Item

To create a new inventory item, use the dm new item command:

```sh
dm new item --name <item_name> [--extend <base_class>] [--mod-path <mod_path>] [--debug]
```

* `--name`: The name of the item class (required).
* `--extend`: The base class to extend (default: Inventory).
* `--mod`-path: The path to the mod folder.
* `--debug`: Enable debug logging.