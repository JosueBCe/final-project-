from constants import *
from game.scripting.action import Action


class DrawRacketAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        racket = cast.get_actors(RACKET_GROUP)[0]
        body = racket.get_body()
        racket_2 = cast.get_actors(RACKET_GROUP)[1]
        body_2 = racket_2.get_body()

        if racket.is_debug():
            rectangle = body.get_rectangle()
            rectangle_2 = body_2.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            self._video_service.draw_rectangle(rectangle_2, BLUE)
            
        animation = racket.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)
        animation_2 = racket_2.get_animation()
        image_2 = animation_2.next_image()
        position_2 = body_2.get_position()
        self._video_service.draw_image(image_2, position_2)