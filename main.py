from assets import load_assets
from game import Game

assets = load_assets()
game = Game(assets)
game.run()