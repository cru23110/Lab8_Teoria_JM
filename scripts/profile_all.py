import subprocess
import sys

cmds = [
    [sys.executable, "src/ex1.py"],
    [sys.executable, "src/ex2.py"],
    [sys.executable, "src/ex3.py"],
]

def main():
    for c in cmds:
        print("==>", " ".join(c))
        subprocess.run(c, check=True)
    print("\nListo. Revisa la carpeta 'results/'.\n")

if __name__ == "__main__":
    main()
