import os
import logging
from maykr.utils import create_directory, initialize_git

DEFAULT_DIRS = [
    "acs", "colormaps", "filter", "flats", "graphics", "hires",
    "maps", "music", "patches", "sounds", "sprites", "textures",
    "voices", "voxels",
    # these next ones are not by spec, but are common
    "weapons", "items", "monsters"
]

def new_mod(args):

    """Creates the Doom mod structure."""
    mod_root = os.path.abspath(args.path) if args.path else os.getcwd()
    mod_folder = os.path.join(mod_root, args.name)

    logging.info(f"🎯 Creating Doom mod: {args.name}")

    # Create root and PK3 folder
    create_directory(mod_folder)

    # Handle optional directories
    for folder in DEFAULT_DIRS:
        if not getattr(args, f"no_{folder}", False):
            create_directory(os.path.join(mod_folder, folder))

    if args.decorate:
        create_directory(os.path.join(mod_folder, "decorate"))

    # Create MAPINFO
    with open(os.path.join(mod_folder, "mapinfo.txt"), "w") as f:
        f.write(f"// MAPINFO for {args.name}\n")
    logging.debug("✅ Created: mapinfo.txt")

    # Create ZMAPINFO
    with open(os.path.join(mod_folder, "zmapinfo.txt"), "w") as f:
        f.write(f"// ZMAPINFO for {args.name}\n")
    logging.debug("✅ Created: zmapinfo.txt")

    # Create ZSCRIPT.txt if using ZScript
    if not args.decorate:
        with open(os.path.join(mod_folder, "zscript.txt"), "w") as f:
            f.write(f'// Entry point for {args.name}\nVersion "4.8";\n')
        logging.debug("✅ Created: zscript.txt")

    # Initialize Git unless --no-git is passed
    if not args.no_git:
        initialize_git(mod_folder)

    logging.info(f"\n🎉 '{args.name}' successfully created at: {mod_folder}")
