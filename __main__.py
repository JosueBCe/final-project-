from constants import *
from game.directing.director import Director
from game.directing.scene_manager import SceneManager


def main():
    director = Director(SceneManager.VIDEO_SERVICE)
    director.start_game()

if __name__ == "__main__":
    main()



    # =====================        ====================

    #                   *****(blocks)a
    #                     # players
    


    #                   # players
    #                   *****(blocks)
    # ==================     =======================


    """ TABLE HOKEY 
    1) 2 players (Josue)
    2) the goals, 3 points wins the player (Daniel) 
    3) movements 2 players (Isaias, Joshua)
    4) appearing blocks (randomly if possible)
    5) Comments and Readme (Each Member of the Team)
    6) Sounds ( Goals, Blocks )

     """