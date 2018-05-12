class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, settings):
        """Initialize stasistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start game in active state
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit

    