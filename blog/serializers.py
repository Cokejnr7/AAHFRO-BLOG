from rest_framework import serializers
from .models import Post,Tag,Section,Image,Interview



class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = '__all__'
    
class ImageSerializer(serializers.ModelSerializer):
    
     class Meta:
        model = Image
        fields = '__all__'
        
class SectionSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True,read_only=True) 
       
    class Meta:
        model = Section
        fields = '__all__'
        
        
class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True,read_only=True)
    sections = SectionSerializer(many=True,read_only=True)
    
    class Meta:
        model = Post
        fields = '__all__'
                

class InterviewSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True,read_only=True)
    sections = SectionSerializer(many=True,read_only=True)
    
    class Meta:
        model = Interview
        fields = '__all__'
        



