 #!/usr/bin/python3
"""
Class State that inherits from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class to save the state where are the
    avaliables places to stay
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of the state"""
        super().__init__(**kwargs)
