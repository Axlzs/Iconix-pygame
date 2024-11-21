import pygame
import json
import os

# Path to the configuration file
CONFIG_PATH = "config.json"

class GameManager:
    def __init__(self):
        # Load settings and initialize screen
        self.settings = self.load_settings()
        self.screen = self.apply_settings()
        self.update_dimensions()

    def load_settings(self):
        """Load settings from the configuration file or use defaults."""
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, 'r') as file:
                return json.load(file)
        else:
            # Default settings if config doesn't exist
            return {
                "screen_mode": "windowed",
                "resolution": [1280, 720]
            }

    def save_settings(self):
        """Save current settings to the configuration file."""
        with open(CONFIG_PATH, 'w') as file:
            json.dump(self.settings, file)

    def apply_settings(self):
        """Apply settings to create or update the screen."""
        if self.settings["screen_mode"] == "fullscreen":
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN,display=0)
        else:
            width, height = self.settings["resolution"]
            self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    def update_dimensions(self):
        """Update cached screen dimensions."""
        self.WIDTH, self.HEIGHT = self.screen.get_size()

# Create a singleton instance of GameManager
game_manager = GameManager()
