class NotImplementedError(RuntimeError):
    
    def __init__(self, message:str):
        self.message = message
    
    def __str__(self):
        return f"Not implemented: {self.message}"