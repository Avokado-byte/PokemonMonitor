from utils.json_manager import JsonManager

KEYWORDS = "data/keywords/keywords.json"


def main() -> None:
    data = JsonManager.read(KEYWORDS)

    print("Contenido de keywords.json:")
    print(data)


if __name__ == "__main__":
    main()