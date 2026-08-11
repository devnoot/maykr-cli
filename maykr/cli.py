import argparse
import logging
from maykr.new_item import new_item
from maykr.new_mod import new_mod
from maykr.new_weapon import new_weapon
from maykr.new_sprite import new_sprite

def configure_logging(debug):
    """Configures logging based on the debug flag."""
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level, format='%(message)s')

def main():
    parser = argparse.ArgumentParser(prog="maykr", description="Maykr CLI - Doom modding tools")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # "dm new" command
    new_parser = subparsers.add_parser("new", help="Create a new resource")
    new_subparsers = new_parser.add_subparsers(dest="type", required=True)

    # "dm new mod" command
    new_mod_parser = new_subparsers.add_parser("mod", help="Create a new Doom mod")
    new_mod_parser.add_argument("--name", required=True, help="Mod name")
    new_mod_parser.add_argument("--path", default=".", help="Path to bootstrap the mod")
    new_mod_parser.add_argument("--no-git", action="store_true", help="Do not initialize Git repository")
    new_mod_parser.add_argument("--decorate", action="store_true", help="Use DECORATE instead of ZScript")
    new_mod_parser.add_argument("--debug", action="store_true", help="Enable debug logging")

    # "dm new weapon" command
    new_weapon_parser = new_subparsers.add_parser("weapon", help="Create a new ZScript weapon")
    new_weapon_parser.add_argument("--name", required=True, help="Weapon class name")
    new_weapon_parser.add_argument("--extend", help="Base class to extend (default: Weapon)")
    new_weapon_parser.add_argument("--mod-path", help="Path to the mod folder")
    new_weapon_parser.add_argument("--debug", action="store_true", help="Enable debug logging")

    # "dm new sprite" command
    new_sprite_parser = new_subparsers.add_parser("sprite", help="Create a new sprite")
    new_sprite_parser.add_argument("--name", required=True, help="Sprite name (without extension)")
    new_sprite_parser.add_argument("--width", type=int, required=True, help="Sprite width")
    new_sprite_parser.add_argument("--height", type=int, required=True, help="Sprite height")
    new_sprite_parser.add_argument("--anim", action="store_true", help="Add sprite to ANIMDEFS for animation")
    new_sprite_parser.add_argument("--duration", type=int, help="Animation frame duration (default: 4 tics)")
    new_sprite_parser.add_argument("--mod-path", help="Path to the mod folder")
    new_sprite_parser.add_argument("--debug", action="store_true", help="Enable debug logging")

    # "dm new item" command
    new_item_parser = new_subparsers.add_parser("item", help="Create a new inventory item")
    new_item_parser.add_argument("--name", required=True, help="Item class name")
    new_item_parser.add_argument("--extend", help="Base class to extend (default: Inventory)")
    new_item_parser.add_argument("--mod-path", help="Path to the mod folder")
    new_item_parser.add_argument("--debug", action="store_true", help="Enable debug logging")

    args = parser.parse_args()
    configure_logging(args.debug)

    if args.command == "new":
        if args.type == "mod":
            new_mod(args)
        elif args.type == "weapon":
            new_weapon(args)
        elif args.type == "sprite":
            new_sprite(args)
        elif args.type == "item":
            new_item(args)

if __name__ == "__main__":
    main()