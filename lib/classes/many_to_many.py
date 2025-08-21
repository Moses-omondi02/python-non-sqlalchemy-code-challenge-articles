class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        # Silently fail instead of raising exception
        pass
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            # Silently fail instead of raising exception
            return
        self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            # Silently fail instead of raising exception
            return
        self._magazine = value


class Author:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        # Silently fail instead of raising exception
        pass
    
    def articles(self):
        return [article for article in Article.all if article.author == self]
    
    def magazines(self):
        magazines = [article.magazine for article in self.articles()]
        return list(set(magazines)) if magazines else []
    
    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article
    
    def topic_areas(self):
        categories = [article.magazine.category for article in self.articles()]
        return list(set(categories)) if categories else None


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            # Silently fail instead of raising exception
            return
        self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            # Silently fail instead of raising exception
            return
        self._category = value
    
    def articles(self):
        return [article for article in Article.all if article.magazine == self]
    
    def contributors(self):
        authors = [article.author for article in self.articles()]
        return list(set(authors)) if authors else []
    
    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None
    
    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1
        
        result = [author for author, count in author_count.items() if count > 2]
        return result if result else None
    