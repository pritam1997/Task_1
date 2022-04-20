from rest_framework import serializers
from .models import Book, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_title']



class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Book
        fields = ['id', 'title', 'pages','category']

    def create(self, validated_data):   # post method
        category_data = validated_data.pop('category')
        
        instance_category = Category.objects.create(**category_data)    # created new category
        get_book, created = Book.objects.get_or_create(**validated_data ,category=instance_category)    #   create new Book data and return Book instance
        return get_book


    def update(self, instance, validated_data):
        
        c_data = validated_data.pop('category')
        
        b = Book.objects.get(id=validated_data['id'])
        Category.objects.filter(id=b.category.id).update(category_title=c_data['category_title'])   # updating category as per id
        c_obj = Category.objects.get(id=b.category.id)  # get category object
        
        instance.category = c_obj       # set category object to instance object i.e Book
        instance.title = validated_data['title']
        instance.pages = validated_data['pages']
        instance.save() # saving to Book class
        return instance


"""
class BookserializerWrite(serializers.ModelSerializer):
   # Category=categoryserializer()
    class Meta:
        model=Book
        fields='__all__'


class BookserializerRead(serializers.ModelSerializer):
   # Category=categoryserializer()
    class Meta(BookserializerWrite.Meta):
        depth=1 #all
"""