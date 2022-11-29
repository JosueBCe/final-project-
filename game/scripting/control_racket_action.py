from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        racket = cast.get_actors(RACKET_GROUP)[0]
        racket_2 = cast.get_actors(RACKET_GROUP)[1]
        if self._keyboard_service.is_key_down(LEFT): 
            racket.swing_left()
        
        elif self._keyboard_service.is_key_down(RIGHT): 
            racket.swing_right()
            
        elif self._keyboard_service.is_key_down(LEFT_2): 
            racket_2.swing_left()
        
        elif self._keyboard_service.is_key_down(RIGHT_2): 
            racket_2.swing_right()
        
        else: 
            racket.stop_moving()
            racket_2.stop_moving()        