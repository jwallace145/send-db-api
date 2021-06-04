class Climber:

    def __init__(self, email: str, username: str, first_name: str, last_name: str) -> None:
        """ Climber Constructor.

        Args:
            email (str): The climber's email.
            username (str): The climber's username.
            first_name (str): The climber's first name.
            last_name (str): The climber's last name.
        """

        self.email = email
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        """ Returns climber as a string """

        return (
            f'{__name__}\n'
            f'{self.email}\n'
            f'{self.username}\n'
            f'{self.first_name}\n'
            f'{self.last_name}\n'
        )
