class Book():
    """
    doc string
    """
    @classmethod
    def from_file(cls, filename):
        print("Class method")
        pass

    def __init__(self, title):
        self.title = title


Book.from_file('haha')
