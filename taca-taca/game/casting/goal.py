from game.casting.actor import Actor


class Goal(Actor):
    """A solid, rectangular object that can be broken."""

    def __init__(self, body, image, player, debug = False):
        """Constructs a new Brick.
        
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image 
        self._points = 0
        self._player = player
        
    # def get_animation(self):
    #     """Gets the brick's image.
        
    #     Returns:
    #         An instance of Image.
    #     """
    #     return self._animation

    def get_player(self):
        """Gets the player.
        
        Returns:
            An instance of PLayer.
        """
        return self._player

    def get_image(self):
        """Gets the ball's image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    def get_body(self):
        """Gets the brick's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_points(self):
        """Gets the brick's points.
        
        Returns:
            A number representing the brick's points.
        """
        return self._points