from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class Bootstrap:
    """Inicializa la estructura base del proyecto."""

    def __init__(self) -> None:
        self.root = Path(__file__).resolve().parent
        self.manifest_path = self.root / "config" / "manifest.json"
        self.manifest = self._load_manifest()

    def _load_manifest(self) -> dict[str, Any]:
        """Carga el archivo manifest.json."""
        try:
            with self.manifest_path.open("r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"No se encontró el archivo: {self.manifest_path}"
            )
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"El manifest.json no tiene un formato válido.\n{exc}"
            )

    def _create_directories(self) -> int:
        """Crea las carpetas indicadas en el manifest."""
        created = 0

        for directory in self.manifest["directories"]:
            path = self.root / directory["path"]

            if not path.exists():
                path.mkdir(parents=True, exist_ok=True)
                created += 1

        return created

    def _create_files(self) -> int:
        """Crea los archivos iniciales si no existen."""
        created = 0

        for file in self.manifest["files"]:
            path = self.root / file["path"]

            if path.exists():
                continue

            path.parent.mkdir(parents=True, exist_ok=True)

            with path.open("w", encoding="utf-8") as output:
                json.dump(
                    file["content"],
                    output,
                    indent=4,
                    ensure_ascii=False,
                )

            created += 1

        return created

    def run(self) -> None:
        """Ejecuta el bootstrap."""
        print("=" * 50)
        print("Pokemon Monitor Bootstrap")
        print("=" * 50)

        directories = self._create_directories()
        files = self._create_files()

        print(f"Carpetas creadas : {directories}")
        print(f"Archivos creados : {files}")
        print("\nProyecto inicializado correctamente.\n")


if __name__ == "__main__":
    Bootstrap().run()