import os
import logging
import subprocess

def detect_mod_name():
    """Automatically detects the mod name by checking for a .pk3 folder."""
    cwd = os.getcwd()
    for entry in os.listdir(cwd):
        if entry.endswith(".pk3") and os.path.isdir(entry):
            return entry[:-4]  # Remove '.pk3' suffix
    logging.error("❌ Could not detect a .pk3 folder in the current directory.")
    exit(1)

def create_directory(path):
    """Creates a directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)
    logging.debug(f"✅ Created: {path}")

def initialize_git(mod_path):
    """Initializes a Git repository in the mod folder."""
    try:
        subprocess.run(["git", "init", "-q"], cwd=mod_path, check=True)
        logging.debug("✅ Initialized Git repository.")
    except Exception as e:
        logging.debug(f"⚠️ Git initialization failed: {e}")
