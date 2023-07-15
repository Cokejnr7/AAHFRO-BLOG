from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Post,Section,Tag,Image
from .serializers import PostSerializer,SectionSerializer
import json
# Create your views here.


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = (MultiPartParser,FormParser)
    
    def list(self,request,*args, **kwargs):
        posts = Post.objects.all()
        serializer = self.serializer_class(posts,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def create(self,request,*args, **kwargs):
        data = dict(request.data)
        user = request.user
        author = data.get("author")[0]
        title = data.get("title")[0]
        main_image = data["main_image"][0]
        tags = data.get("tags")[0].split(",")
        sections = data.get("sections")[0]
        
        #Creates new post
        # post = Post.objects.create(title=title,main_image=main_image,author=author)
        
        #loops through the tags in the request data and converts it to python objects
        # for tag in enumerate(tags):
        #     tag= json.loads(tag)
        #     tag = Tag.objects.get(name=tag.get("name"))
        #     post.tag.add(tag)
            
        print(user.is_staff)
            
            
        # print(dir(main_image))
    
        # with open(main_image.name,mode='wb') as img:
        #     for chunks in main_image.chunks():
        #         img.write(chunks)
        
       
        
            
        
        
        # print(post.title,post.author,post.main_image,post.tag)
        # print(data)
        # print()
            
        
        return Response("hello",status=status.HTTP_201_CREATED)
        
    # def get_queryset(self):
    #     return super().get_queryset()
    

class PostRetrieveUpdateDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    


class SectionList(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer 
    