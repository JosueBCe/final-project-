from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideRacketAction(Action):

    def __init__(self, physics_service, audio_service, player):
        self._physics_service = physics_service
        self._audio_service = audio_service
        self._player = player
        
    def execute(self, cast, script, callback):
        playing = 0
        if self._player == "player_1":
            playing = 0
        elif self._player == "player_2":
            playing = 1 

        ball = cast.get_first_actor(BALL_GROUP)
        racket = cast.get_actors(RACKET_GROUP)[playing]
        
        ball_body = ball.get_body()
        racket_body = racket.get_body()

        if self._physics_service.has_collided(ball_body, racket_body):
            ball.bounce_y()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)    