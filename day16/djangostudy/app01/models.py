from django.db import models

# Create your models here.


from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50,null=True,blank=True,help_text="输入地址就行")
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    def __str__(self):
        return "<%s %s>" %(self.name,self.address)
    class Meta:
        verbose_name_plural = "出版社"


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    def __str__(self):
        return "<%s %s %s>" %(self.first_name,self.last_name,self.email)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    publication_date = models.DateField()
    def __str__(self):
        return "<%s %s %s >" %(self.title,self.authors,self.publisher)