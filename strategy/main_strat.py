from random import Random
from game.game_state import GameState
import game.character_class

from game.item import Item

from game.position import Position
from strategy.strategy import Strategy

class MainStrategy(Strategy):
    MID_GAME = 9
    END_GAME = 80
    spawn = Position(0, 0)
    center = [Position(4,4), Position(4,5), Position(5,4), Position(5,5)]
    def strategy_initialize(self, my_player_index: int):
        if my_player_index == 1:
            spawn = Position(9, 0)
        elif my_player_index == 2:
            spawn = Position(9, 9)
        elif my_player_index == 3:
            spawn = Position(0,9)
        return game.character_class.CharacterClass.KNIGHT

    def move_action_decision(self, game_state: GameState, my_player_index: int) -> Position:
        current_pos = game_state.player_state_list[my_player_index].position
        if game_state.turn < MID_GAME:
            if current_pos in center:
                return current_pos
            else:
                return move_towards_center(self, game_state, my_player_index)
        elif game_state.turn < END_GAME:

        return game_state.player_state_list[my_player_index].position

    def attack_action_decision(self, game_state: GameState, my_player_index: int) -> int:
        return Random().randint(0, 3)

    def buy_action_decision(self, game_state: GameState, my_player_index: int) -> Item:
        player = game_state.player_state_list[my_player_index]
        if player.item == Item.NONE and player.gold >= 8 and player.position 
        return Item.NONE

    def use_action_decision(self, game_state: GameState, my_player_index: int) -> bool:
        return False

    def move_towards_center(self, game_state: GameState, my_player_index: int) -> Position:
        current_pos = game_state.player_state_list[my_player_index].position
        if my_player_index == 1:
            Position(current_pos.x - 1, current_pos.y + 1)
        elif my_player_index == 2:
            Position(current_pos.x - 1, current_pos.y - 1)
        elif my_player_index == 3:
            Position(current_pos.x + 1, current_pos.y - 1)
        else:
            Position(current_pos.x + 1, current_pos.y + 1)
    
    def is_in_my_range(self, game_state: GameState, my_player_index: int, opponent_index: int) -> bool:
        player_pos = game_state.player_state_list[opponent_index].position
        my_pos = game_state.player_state_list[my_player_index].position
        my_range = game_state.player_state_list[my_player_index].stat_set.range
        return util.chebyshev_distance(player_pos, my_pos) < my_range

    def am_i_in_range(self, game_state: GameState, my_player_index: int, opponent_index: int) -> bool:
        player_pos = game_state.player_state_list[opponent_index].position
        my_pos = game_state.player_state_list[my_player_index].position
        their_range = game_state.player_state_list[opponent_index].stat_set.range
        return util.chebyshev_distance(player_pos, my_pos) < their_range

    def which_opponent_in_range(self, game_state: GameState, my_player_index:int, player_state_list) -> int:
        for i in player_state_list:
            if i.position != game_state.player_state_list[my_player_index].position:
                is_in_my_range