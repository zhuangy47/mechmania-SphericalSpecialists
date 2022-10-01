from random import Random
from game.game_state import GameState
import game.character_class

from game.item import Item
from util import utility as util

from game.position import Position
from strategy.strategy import Strategy

class StarterStrategy(Strategy):
    def strategy_initialize(self, my_player_index: int):
        return game.character_class.CharacterClass.ARCHER

    def move_action_decision(self, game_state: GameState, my_player_index: int) -> Position:
        return game_state.player_state_list[my_player_index].position

    def attack_action_decision(self, game_state: GameState, my_player_index: int) -> int:
        return Random().randint(0, 3)

    def buy_action_decision(self, game_state: GameState, my_player_index: int) -> Item:
        return Item.NONE

    def use_action_decision(self, game_state: GameState, my_player_index: int) -> bool:
        return False

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

    def rotatePosCounterClockwise(self, my_player_index: int, pos: Position) -> Position:
        new_pos = pos
        for i in range(my_player_index):
            new_pos = Position(new_pos.y, 9 - new_pos.x)
        return new_pos

    def rotatePosClockwise(self, my_player_index: int, pos: Position) -> Position:
        new_pos = pos
        for i in range(my_player_index):
            new_pos = Position(9 - new_pos.y, new_pos.x)
        return new_pos
        
