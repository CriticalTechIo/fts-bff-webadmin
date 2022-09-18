from uuid import UUID


class InstanceService():
    """
    Will enable functionality for handling of multiple fts instances.
    """
    def __init__(self, db, logger):
        self.db = db
        self.logger = logger

    def add_instance(self, things):
        pass

    def change_instance(self, things):
        pass
  
    def get_instance(self, uuid: UUID):
        pass

    def get_instances(self, uuid: UUID):
        pass
