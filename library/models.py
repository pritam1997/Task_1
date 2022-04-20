from django.db import models


"""
    Django uses ORM (Object relational mapping)
    Object is mapping with database table with their fields
    ORM using some techniques to convert object (Book) to database table
"""


class Category(models.Model):
    category_title = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.category_title


class Book(models.Model):   # database table name is Book
    title = models.CharField(max_length=100)    # this is title field in Book table
    pages = models.IntegerField()   # this is pages field in Book table
    category = models.ForeignKey(Category, related_name="categorys", on_delete=models.CASCADE)

    # title string visbile to admin site
    def __str__(self):
        return self.title   

