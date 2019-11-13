 #!/usr/bin/python3
"""
Class Review that inherits from BaseModel
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    Class to save the reviews of the places
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialization of the review"""
        super().__init__(**kwargs)
