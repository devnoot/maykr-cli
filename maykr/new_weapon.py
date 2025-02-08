import os
import logging


def new_weapon(args):
    """Bootstraps a new ZScript weapon class."""
    # mod_name = os.path.basename(args.mod_path) if args.mod_path else os.path.basename(os.getcwd())
    mod_root = args.mod_path if args.mod_path else os.getcwd()
    weapons_folder = os.path.join(mod_root, "weapons")
    weapon_name = args.name
    parent_class = args.extend if args.extend else "Weapon"
    weapon_file = os.path.join(weapons_folder, f"{weapon_name}.zs")

    weapon_code = f"""\
class {weapon_name} : {parent_class} {{

    Default {{
        Weapon.SlotNumber 3;
        Weapon.AmmoUse 1;
        Weapon.AmmoGive 30;
        Weapon.AmmoType "Clip";
        Weapon.Kickback 100;

        Inventory.PickupMessage "You got the {weapon_name}";
    }}

    States {{

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
            TNT1 A 0 {{
                A_Print("Firing {weapon_name}");
            }}
            Goto Ready;
        
        Flash:
            TNT1 A 1 Bright A_Light1;
            TNT1 A 1 Bright A_Light2;
            Goto LightDone;

    }}
}}"""

    with open(weapon_file, "w") as f:
        f.write(weapon_code)

    logging.info(f"✅ Created weapon: {weapon_file}")