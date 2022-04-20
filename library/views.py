from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer # BookserializerRead, BookserializerWrite


# function based view using @api_view
@api_view(['GET', 'POST'])    # access on get method
def home(request):

    print(request.data)
    if request.method == 'GET':     # checks if method is GET
        obj = Book.objects.all()    # get all tabular data similar like Select query e.g SELECT * FROM BOOK
        serializer = BookSerializer(obj, many=True)    # serialize Book object and because Book object get more than 1 data
        return Response(serializer.data, status=status.HTTP_200_OK) # response serialize data i.e JSON data with status 200 code

    elif request.method == 'POST':      # checks if method is POST
        
        s = BookSerializer(data =request.data)     # passing requested data in BookSerializer class as parameter
        if s.is_valid():    # validating BookSerailizer object 
            s.save()    # save BookSerialize object
            return Response(s.data, status = status.HTTP_201_CREATED)   # responsing serialize data i.e JSON data with status 201 created code
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)   # responsing serialize error with status 400 code


@api_view(['GET', 'PUT','PATCH', 'DELETE'])
def update(request, pk):
    #   retrieve, update and delete
    try:
        book = Book.objects.get(pk=pk)     
    except book.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        book = Book.objects.get(pk=pk)  
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        book = Book.objects.get(id=request.data['id'])
        # serialize = BookSerializer(book, data=request.data)
        serialize = BookSerializer(book, data=request.data)

        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_200_OK)
        return Response(serialize.errors, status=status.HTTP_404_NOT_FOUND)        

    elif request.method == 'PATCH':            
        serializer = BookSerializer(book, data = request.data, partial=True)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)

        

    elif request.method=='DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])    # access on get method
def get_category(request):
    obj = Category.objects.all()    # get all tabular data similar like Select query e.g SELECT * FROM BOOK
    serializer = CategorySerializer(obj, many=True)    # serialize Book object and because Book object get more than 1 data
    return Response(serializer.data, status=status.HTTP_200_OK)

