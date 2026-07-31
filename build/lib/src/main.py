from src.cli import main as cli_main
from src.storage import create_table


def main():
    create_table()
    cli_main()


if __name__ == "__main__":
    main()
