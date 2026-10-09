import subprocess
import sys

from .git import git
from .ai import generate

def main():
    diff = git("diff", "--staged")
    if not diff.strip():
        sys.exit("Nothing staged.")

    while True:
        message = generate(diff)
        print(f"\n{message}\n")
        choice = input("[c]ommit, [r]egenerate, [q]uit? ").strip().lower()
        if choice == "c":
            subprocess.run(["git", "commit", "-m", message])
            break
        if choice == "r":
            message = generate(diff)
        if choice == "q":
            break