# maykr

maykr is a command line tool that can bootstrap various aspects of your classic doom mod.

[![Latest Release](https://img.shields.io/github/v/release/devnoot/maykr-cli?label=Latest)](https://github.com/devnoot/maykr-cli/releases/latest)
[![Build Status](https://img.shields.io/github/actions/workflow/status/devnoot/maykr-cli/release.yml?branch=main)](https://github.com/devnoot/maykr-cli/actions)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-blue)](https://github.com/devnoot/maykr-cli/releases)
[![Python Version](https://img.shields.io/badge/python-3.14+-blue.svg)](https://www.python.org/)

## Installation

Download the standalone executable for your operating system:

- [macOS (Universal)](https://github.com/devnoot/maykr-cli/releases/latest/download/maykr-macos-universal)
- [Linux (amd64)](https://github.com/devnoot/maykr-cli/releases/latest/download/maykr-linux-amd64)
- [Windows (amd64)](https://github.com/devnoot/maykr-cli/releases/latest/download/maykr-windows-amd64.exe)

*(After downloading on macOS/Linux, remember to make the file executable: `chmod +x maykr-*`)*

## Developers

Clone the repo, install from requirements from `requirements.txt`, and run `maykr/cli.py`

## Usage

### Creating a New Mod

To create a new Doom mod, use the `maykr new mod` command:

```sh
maykr new mod --name <mod_name> [--path <path>] [--no-git] [--decorate] [--debug]
```

* `--name`: The name of the mod (required).
* `--path`: The path where the mod will be created (default: current directory).
* `--no-git`: Do not initialize a Git repository.
* `--decorate`: Use DECORATE instead of ZScript.
* `--debug`: Enable debug logging.

This will bootstrap your mod into the path specified. Folders for various types of assets will be created, as well as files for mapinfo, zmapinfo, and the ZScript entry point.

<details>
<summary>An empty mod folder will look like this:</summary>
```
MyMod/
├── acs         
├── colormaps   
├── filter      
├── flats       
├── graphics      
├── hires         
├── items         
├── maps       
├── monsters   
├── patches    
├── music      
├── sprites    
├── textures   
├── sounds     
├── voxels
├── voices    
├── weapons
├── mapinfo.txt
├── zmapinfo.txt
└── zscript.txt
```

</details>

### Creating a New Weapon

To create a new ZScript weapon, use the maykr new weapon command:

```sh
maykr new weapon --name <weapon_name> [--extend <base_class>] [--mod-path <mod_path>] [--debug]
```


* `--name`: The name of the weapon class (required).
* `--extend`: The base class to extend (default: Weapon).
* `--mod-path`: The path to the mod folder (required if not running from within the mod folder).
* `--debug`: Enable debug logging.

<details>
  <summary>Example: weapons/ChickenCannon9000.zs</summary>

```
class ChickenCannon9000 : Weapon {

    Default {
        Weapon.SlotNumber 3;
        Weapon.AmmoUse 1;
        Weapon.AmmoGive 30;
        Weapon.AmmoType "Clip";
        Weapon.Kickback 100;

        Inventory.PickupMessage "You got the ChickenCannon9000";
    }

    States {

        Spawn:
            Stop;

        Ready:
            TNT1 A 1 A_WeaponReady;
            Loop;

        Select:
            TNT1 A 1 A_Raise;
            Goto Ready;

        Deselect:
            TNT1 A 1 A_Lower;
            Goto Ready;

        Fire:
            TNT1 A 0 {
                A_Print("Firing ChickenCannon9000");
            }
            Goto Ready;

        Flash:
            TNT1 A 1 Bright A_Light1;
            TNT1 A 1 Bright A_Light2;
            Goto LightDone;

    }
}
```

</details>

### Creating a New Sprite

To create a new sprite, use the maykr new sprite command:

```sh
maykr new sprite --name <sprite_name> --width <width> --height <height> [--anim] [--duration <duration>] [--mod-path <mod_path>] [--debug]
```

* `--name`: The name of the sprite (without extension, required).
* `--width`: The width of the sprite (required).
* `--height`: The height of the sprite (required).
* `--anim`: Add the sprite to ANIMDEFS for animation.
* `--duration`: The animation frame duration (default: 4 tics).
* `--mod-path`: The path to the mod folder (required if not running from within the mod folder).
* `--debug`: Enable debug logging.
 
### Creating a New Item

To create a new inventory item, use the maykr new item command:

```sh
maykr new item --name <item_name> [--extend <base_class>] [--mod-path <mod_path>] [--debug]
```

* `--name`: The name of the item class (required).
* `--extend`: The base class to extend (default: Inventory).
* `--mod-path`: The path to the mod folder (required if not running from within the mod folder).
* `--debug`: Enable debug logging.

<details>
  <summary>Example: items/SuperClip.zs</summary>

```
class SuperClip : Inventory
{
    Default
    {
        Inventory.MaxAmount 1;
        +INVENTORY.PICKUPFLASH;
    }

    States
    {
    Spawn:
        TNT1 A 1;
        Loop;
    Pickup:
        TNT1 A 0
        {
            A_Log("Picked up SuperClip!");
            A_GiveInventory("SuperClip");
        }
        Stop;
    }
}
```

</details>