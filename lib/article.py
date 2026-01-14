class Article:
    all = []

    def __init__(self, author, magazine, title):
        from lib.author import Author
        from lib.magazine import Magazine
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine instance")
        if not isinstance(title, str) or not 5 <= len(title) <= 50:
            raise Exception("title must be a string 5-50 chars")
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # title cannot be changed after instantiation
        pass