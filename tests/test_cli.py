import subprocess
import os
import pytest

def run_cli_command(command):
    """Helper function to run a CLI command and return the output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result

@pytest.fixture
def setup_mod():
    """Fixture to set up the test mod environment."""
    mod_name = "test_mod"
    test_dir = os.path.join(os.getcwd(), "tests")
    mod_path = os.path.join(test_dir, mod_name)
    command = f"dm new mod --name {mod_name} --path {test_dir} --debug"
    run_cli_command(command)
    return mod_name, mod_path

def test_new_mod(setup_mod):
    """Test the 'dm new mod' command."""
    _, mod_path = setup_mod
    assert os.path.isdir(mod_path)
    assert os.path.isfile(f"{mod_path}/mapinfo.txt")
    assert os.path.isfile(f"{mod_path}/zmapinfo.txt")
    assert os.path.isfile(f"{mod_path}/zscript.txt")

def test_new_weapon(setup_mod):
    """Test the 'dm new weapon' command."""
    _, mod_path = setup_mod
    weapon_name = "TestWeapon"
    command = f"dm new weapon --name {weapon_name} --mod-path {mod_path} --debug"
    result = run_cli_command(command)
    assert result.returncode == 0
    assert os.path.isfile(os.path.join(mod_path, "weapons", f"{weapon_name}.zs"))

def test_new_sprite(setup_mod):
    """Test the 'dm new sprite' command."""
    _, mod_path = setup_mod
    sprite_name = "TestSprite"
    command = f"dm new sprite --name {sprite_name} --width 64 --height 64 --mod-path {mod_path} --debug"
    result = run_cli_command(command)
    assert result.returncode == 0
    assert os.path.isfile(os.path.join(mod_path, "sprites", f"{sprite_name}.png"))

def test_new_item(setup_mod):
    """Test the 'dm new item' command."""
    _, mod_path = setup_mod
    item_name = "TestItem"
    command = f"dm new item --name {item_name} --mod-path {mod_path} --debug"
    result = run_cli_command(command)
    assert result.returncode == 0
    assert os.path.isfile(os.path.join(mod_path, "items", f"{item_name}.zs"))
