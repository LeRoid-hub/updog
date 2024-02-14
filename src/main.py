import sys

def syntaxerror() -> None:
    print("Usage: main.py <argument>")
    sys.exit(1)

def main():
    if len(sys.argv) != 2:
        syntaxerror()

if __name__ == '__main__':
    main()
