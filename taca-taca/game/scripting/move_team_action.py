from constants import *
import random
from game.casting.point import Point
from game.scripting.action import Action


class MoveTeamAction(Action):
    """The actiom which applies to the movement of both teams(red & black)."""

    def __init__(self):
        pass  

    def execute(self, cast, script, callback):
        teams = cast.get_actors(TEAM_GROUP)

        for team in teams:
            body = team.get_body()
            velocity = body.get_velocity()
            position = body.get_position()
            x = position.get_x()
        
            position = position.add(velocity)

            if x < 0:
                self._body.set_velocity(velocity)
                position = Point(0, position.get_y())
            elif x > (SCREEN_WIDTH - TEAM_WIDTH):
                position = Point(SCREEN_WIDTH - TEAM_WIDTH, position.get_y())
        
            if any(t.get_body().get_position().get_y() < FIELD_TOP for t in teams):
                body.set_position(Point(position.get_x(), position.get_y() + 1))

            elif any(t.get_body().get_position().get_y() >= FIELD_BOTTOM for t in teams):
                body.set_position(Point(position.get_x(), position.get_y() - 1))

            else:
                body.set_position(position)


        team2 = cast.get_actors(TEAM_TWO_GROUP)

        for team in team2:
            body = team.get_body()
            velocity = body.get_velocity()
            position = body.get_position()
            x = position.get_x()
        
            position = position.add(velocity)

            if x < 0:
                position = Point(0, position.get_y())
            elif x > (SCREEN_WIDTH - TEAM_WIDTH):
                position = Point(SCREEN_WIDTH - TEAM_WIDTH, position.get_y())
            
            if any(t.get_body().get_position().get_y() < FIELD_TOP for t in team2):
                body.set_position(Point(position.get_x(), position.get_y() + 1))

            elif any(t.get_body().get_position().get_y() >= FIELD_BOTTOM for t in team2):
                body.set_position(Point(position.get_x(), position.get_y() - 1))

            else:
                body.set_position(position)
            
        