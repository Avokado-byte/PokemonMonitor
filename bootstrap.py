from pathlib import Path
import json


class Bootstrap:

    def __init__(self):

        self.root = Path(__file__).parent

        self.manifest_path = self.root / "config" / "manifest.json"

        self.manifest = self.load_manifest()

    def load_manifest(self):

        with open(self.manifest_path, "r", encoding="utf-8") as file:

            return json.load(file)

    def create_directories(self):

        created = 0

        for directory in self.manifest["directories"]:

            path = self.root / directory["path"]

            if not path.exists():

                path.mkdir(parents=True, exist_ok=True)

                created += 1

        return created

    def create_files(self):

        created = 0

        for file in self.manifest["files"]:

            path = self.root / file["path"]

            if not path.exists():

                path.parent.mkdir(parents=True, exist_ok=True)

                with open(path, "w", encoding="utf-8") as f:

                    json.dump(
                        file["content"],
                        f,
                        indent=4,
                        ensure_ascii=False
                    )

                created += 1

        return created

    def run(self):

        print("\nPokemon Monitor Bootstrap\n")

        directories = self.create_directories()

        files = self.create_files()

        print(f"Carpetas creadas : {directories}")

        print(f"Archivos creados : {files}")

        print("\nProyecto listo.\n")


if __name__ == "__main__":

    Bootstrap().run()