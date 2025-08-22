import sys

def main(*args):
    print(f"Foram passados {len(args)} argumentos:")
    for i, arg in enumerate(args, start=1):
        print(f"Argumento {i}: {arg}")

if __name__ == "__main__":
    # sys.argv[0] é o nome do script, os demais são os argumentos
    if len(sys.argv) < 2:
        print("Uso: python programa.py <arg1> [<arg2> ... <argN>]")
        sys.exit(1)
    
    main(*sys.argv[1:])

