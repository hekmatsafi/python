import json
import os

CONFIG_FILE = "config.json"

DEFAULT_CONFIG = {
    "app_name": "MyAwesomeApp",
    "version": "1.0.0",
    "settings": {
        "theme": "dark",
        "notifications": True,
        "max_users": 50
    }
}


def load_configuration():
    if not os.path.exists(CONFIG_FILE) or os.path.getsize(CONFIG_FILE) == 0:
        save_configuration(DEFAULT_CONFIG)
        return DEFAULT_CONFIG
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return DEFAULT_CONFIG


def save_configuration(data):
    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    config = load_configuration()

    # Read nested setting
    current_theme = config["settings"]["theme"]

    # Modify one setting in memory
    config["settings"]["theme"] = "light"

    # Write back to file
    save_configuration(config)
