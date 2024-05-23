from pathlib import Path
from platform import system
from stat import S_IXUSR
from subprocess import Popen

SYSTEM: str = system()

def get_neovim_path() -> str:
    if SYSTEM == "Linux":
        return "/usr/local/bin/nvim"
    elif SYSTEM == "Darwin":
        return "/opt/homebrew/bin/nvim"
    elif SYSTEM == "Windows":
        return "Unknown"
    else:
        return ""


if __name__ == "__main__":
    raw_path: str = input(
        f"Enter Neovim executable path, empty for default ({SYSTEM} default is {get_neovim_path()}): "
    )
    if len(raw_path) == 0:
        raw_path = get_neovim_path()

    neovim_path: Path = Path(raw_path)

    if not neovim_path.is_file():
        raise FileNotFoundError(f"Neovim executable at {neovim_path} doesn't exist!")

    if not (neovim_path.stat().st_mode & S_IXUSR):
        raise PermissionError("Specified path doesn't have execute permissions!")

    nvim_proc: Popen = Popen([neovim_path])  # , *argv])

    counter: int = 0
    while nvim_proc.poll() is None:
        counter += 1
