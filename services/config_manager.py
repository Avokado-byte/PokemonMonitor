from __future__ import annotations

from pathlib import Path
from typing import Any

from utils.json_manager import JsonManager


class ConfigManager:
    """Carga y expone la configuración del proyecto."""

    def __init__(self) -> None:
        root = Path(__file__).resolve().parent.parent
        settings_path = root / "config" / "settings.json"

        self._settings = JsonManager.read(settings_path)

    def get(self, *keys: str, default: Any = None) -> Any:
        """
        Obtiene un valor del settings.json.

        Ejemplo:
            get("application", "timeout")
        """

        value = self._settings

        for key in keys:

            if not isinstance(value, dict):
                return default

            value = value.get(key)

            if value is None:
                return default

        return value