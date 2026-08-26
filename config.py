from services.config_manager import ConfigManager


_manager = ConfigManager()


class Config:
    project_name = _manager.get("project", "name")
    version = _manager.get("project", "version")

    headless = _manager.get("application", "headless")
    scan_interval = _manager.get("application", "scan_interval")
    timeout = _manager.get("application", "timeout")
    log_level = _manager.get("application", "log_level")

    discord_enabled = _manager.get("discord", "enabled")