class Book:
    def __init__(self, id, title, author, image_url = None):
        self.id = id
        self.title = title
        self.author = author
        self.image_url = image_url if image_url else "https://via.placeholder.com/300x450?text=No+Cover"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.author}, {self.image_url})"