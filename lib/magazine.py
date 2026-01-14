class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not 2 <= len(name) <= 16:
            raise Exception("Magazine name must be a string 2-16 chars")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a non-empty string")
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        from lib.article import Article
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        authors = [article.author for article in self.articles()]
        return list(set(authors)) if authors else []

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [
            author for author in self.contributors()
            if sum(1 for a in self.articles() if a.author == author) > 2
        ]
        return authors if authors else None

    # Optional: uncomment for bonus
    # @classmethod
    # def top_publisher(cls):
    #     if not cls.all or not any(cls.all):
    #         return None
    #     return max(cls.all, key=lambda mag: len(mag.articles()))