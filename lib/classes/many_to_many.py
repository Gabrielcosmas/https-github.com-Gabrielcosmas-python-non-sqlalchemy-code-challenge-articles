# many_to_many.py

class Article:
    all = []  # tracks all articles

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not isinstance(author, Author):
            raise TypeError("Author must be an Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be a Magazine")

        self._title = title
        self.author = author
        self.magazine = magazine

        # Add this article to author and magazine
        author._articles.append(self)
        magazine._articles.append(self)

        # Track all articles
        Article.all.append(self)

    @property
    def title(self):
        return self._title


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Author name must be a string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = {article.magazine.category for article in self._articles}
        return list(mags) if mags else None


class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category
        self._articles = []

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
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        titles = [article.title for article in self._articles]
        return titles if titles else None

    def contributing_authors(self):
        authors = [author for author in self.contributors() if sum(1 for a in self._articles if a.author == author) > 2]
        return authors if authors else None