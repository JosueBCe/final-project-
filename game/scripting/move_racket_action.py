from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRacketAction(Action):

    def __init__(self, player):
        self._player = player
        pass

    def execute(self, cast,script, callback): 
        playing = 0
        if self._player == "player_1":
            playing = 0
        elif self._player == "player_2":
            playing = 1 
        racket = cast.get_actors(RACKET_GROUP)[playing]
        body = racket.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        
        position = position.add(velocity)

        if x < 0:
            position = Point(0, position.get_y())
        elif x > (SCREEN_WIDTH - RACKET_WIDTH):
            position = Point(SCREEN_WIDTH - RACKET_WIDTH, position.get_y())
            
        body.set_position(position)
        