from contextlib import nullcontext
from datetime import datetime

class task:
    def __init__(self, _due_date, _name, _description, _priority):
        self.created_date = str(datetime.now())
        self.name = _name
        self.due_date = _due_date
        self.description = _description
        self.priority = _priority
        self._is_done = False
