class Book:
    def __init__(self, title, author, id = None, image_url = None):
        self.id = id
        self.title = title
        self.author = author
        self.image_url = image_url if image_url else "https://placehold.co/150x150/EEE/31343C"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.author}, {self.image_url})"