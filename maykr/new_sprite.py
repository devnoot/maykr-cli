import os
import logging
from PIL import Image
from maykr.utils import create_directory

def new_sprite(args):
    """Creates a transparent PNG sprite with optional ANIMDEFS entry."""
    # mod_name = os.path.basename(args.mod_path) if args.mod_path else os.path.basename(os.getcwd())
    mod_root = args.mod_path if args.mod_path else os.getcwd()
    sprites_folder = os.path.join(mod_root, "sprites")

    sprite_filename = f"{args.name}.png"
    sprite_path = os.path.join(sprites_folder, sprite_filename)

    # Create transparent PNG
    img = Image.new("RGBA", (args.width, args.height), (0, 0, 0, 0))
    img.save(sprite_path)

    logging.info(f"✅ Created sprite: {sprite_path} ({args.width}x{args.height})")

    # Optionally add to ANIMDEFS
    if args.anim:
        animdefs_path = os.path.join(mod_root, "animdefs.txt")
        frame_duration = args.duration if args.duration else 4

        anim_entry = f"""
texture {args.name}
{{
    XScale 1.0
    YScale 1.0
    Pic {args.name} Tics {frame_duration}
}}
"""
        with open(animdefs_path, "a") as f:
            f.write(anim_entry)
        logging.info(f"✅ Added to animdefs.txt: {animdefs_path}")

    logging.info("🎨 Sprite setup complete!")

