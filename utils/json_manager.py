from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class JsonManager:
    """Utilidades para leer y escribir archivos JSON."""

    @staticmethod
    def read(path: str | Path) -> Any:
        """Lee un archivo JSON y devuelve su contenido."""
        file_path = Path(path)

        if not file_path.exists():
            raise FileNotFoundError(f"No existe el archivo: {file_path}")

        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def write(path: str | Path, data: Any) -> None:
        """Escribe datos en un archivo JSON."""
        file_path = Path(path)

        file_path.parent.mkdir(parents=True, exist_ok=True)

        with file_path.open("w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )

    @staticmethod
    def exists(path: str | Path) -> bool:
        """Indica si el archivo existe."""
        return Path(path).exists()