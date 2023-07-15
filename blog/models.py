from django.db import models

# Create your models here.


class Post(models.Model):
    main_image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    published = models.BooleanField(default=False)
    author = models.CharField(max_length=100)
    contributors = models.CharField(max_length=200,null=True,blank=True)
    tags = models.ManyToManyField("Tag",blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    
    
 
class Interview(models.Model):
    interviewee_name = models.CharField(max_length=100)
    main_image = models.ImageField(upload_to='images/')
    stylist =models.CharField(max_length=50)
    hair = models.CharField(max_length=50)
    photography = models.CharField(max_length=50)
    brief_overview = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField("Tag",blank=True)
    
    def __str__(self) -> str:
        return self.interviewee_name
    
class Section(models.Model):
    paragraph = models.TextField() 
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='sections',null=True,blank=True)
    interview = models.ForeignKey(Interview,on_delete=models.CASCADE,related_name='sections',null=True,blank=True)
    
    def __str__(self) -> str:
        if self.post:
            return self.post.title
        
        return self.interview.interviewee_name
    
    
class Image(models.Model):
    image_url = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=150)
    section = models.ForeignKey(Section,on_delete=models.CASCADE,related_name='images')
    
    def __str__(self) -> str:
        return str(self.section)
    

    
class Tag(models.Model):
    name= models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name