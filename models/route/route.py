import datetime
from ..climber.climber import Climber


class Route:

    def __init__(self, name: str, climber: Climber, grade: str, climb_type: str, wall: str, crag: str,  style: str, ascent: str, height: int, pitches: int,  timestamp: datetime) -> None:
        """ Route Constructor.

        Args:
            name (str): The name of the route.
            climber (str): The climber of the route.
            grade (str): The grade of the route.
            climb_type (str): The type of the route. Sport, Trad, Mixed, Boulder.
            wall (str): The wall the route is located on.
            crag (str): The crag the route is located in.
            style (str): The style of the climb. Lead, Follow, Toprope, Solo.
            ascent (str): The type of ascent of the route. Onsight, Flash, Redpoint, Fell/Hung.
            height (int): The height of the route.
            pitches (int): The number of pitches in the route.
            timestamp (datetime): The timestamp of the climb.
        """

        self.name = name
        self.grade = grade
        self.climb_type = climb_type
        self.wall = wall
        self.crag = crag
        self.style = style
        self.ascent = ascent
        self.height = height
        self.pitches = pitches
        self.timestamp = timestamp

    def __str__(self) -> str:
        """" Returns route as a string"""
        return (
            f'{__name__}\n'
            f'name: {self.name}\n'
            f'grade: {self.grade}\n'
            f'climb type: {self.climb_type}\n'
            f'wall: {self.wall}\n'
            f'crag: {self.crag}\n'
            f'style: {self.style}\n'
            f'ascent: {self.ascent}\n'
            f'height: {self.height}\n'
            f'pitches: {self.pitches}\n'
            f'timestamp: {self.timestamp}\n'
        )
