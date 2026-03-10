from code.Constants import OBJECT_SCORE
from code.Player import Player


class ObjectMediator:

    @staticmethod
    def handle_collision(player : Player, object_list : list):
        for obj in object_list:
            if player.check_collision(obj.rect.center):
                player.score += OBJECT_SCORE[obj.name]
                object_list.remove(obj)
