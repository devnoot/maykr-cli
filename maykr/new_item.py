import os
import logging

def new_item(args):
    """Bootstraps a new ZScript inventory item class."""
    mod_root = args.mod_path if args.mod_path else os.getcwd()
    items_folder = os.path.join(mod_root, "items")
    item_name = args.name
    parent_class = args.extend if args.extend else "Inventory"
    item_file = os.path.join(items_folder, f"{item_name}.zs")

    item_code = f"""
class {item_name} : {parent_class}
{{
    Default
    {{
        Inventory.MaxAmount 1;
        +INVENTORY.PICKUPFLASH;
    }}

    States
    {{
    Spawn:
        TNT1 A 1;
        Loop;
    Pickup:
        TNT1 A 0
        {{
            A_Log("Picked up {item_name}!");
            A_GiveInventory("{item_name}");
        }}
        Stop;
    }}
}}"""

    # Ensure the directory exists
    os.makedirs(items_folder, exist_ok=True)
    
    with open(item_file, "w") as f:
        f.write(item_code)

    logging.info(f"✅ Created item: {item_file}")
