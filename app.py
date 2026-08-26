from config import Config


def main():

    print(Config.project_name)

    print(Config.version)

    print(Config.scan_interval)

    print(Config.headless)

    print(Config.timeout)

    print(Config.discord_enabled)


if __name__ == "__main__":
    main()