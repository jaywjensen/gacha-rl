import tcod
from gacha_rl.actions import EscapeAction, MovementAction
from gacha_rl.input_handlers import EventHandler
from gacha_rl.entity import Entity
from gacha_rl.engine import Engine
from gacha_rl.game_map import GameMap

def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    tileset = tcod.tileset.load_tilesheet(
        "resources/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width/2), int(screen_height/2), "@", (255, 0, 0))
    npc = Entity(int(screen_width/2 - 5), int(screen_height/2), "G", (0, 200, 0))
    entities = {npc, player}
    game_map = GameMap(map_width, map_height)

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset = tileset,
        title = "roguelike tutorial",
        vsync = True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)
            events = tcod.event.wait()
            engine.handle_events(events)


if __name__ == "__main__":
    main()