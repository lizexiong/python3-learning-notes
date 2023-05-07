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


from django.utils.html import format_html
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    publication_date = models.DateField()
    status_choices = (('published','已出版'),
                      ('producing','待出版'),
                                         )
    #choices这个字段一定要有一个默认值，否则报错
    status = models.CharField(choices=status_choices,max_length=32,default='producing')

    def __str__(self):
        return "<%s %s %s >" %(self.title,self.authors,self.publisher)

    def colored_status(self):
        if self.status == "published":
            format_td = format_html('<span style="padding:2px;background-color:yellowgreen;color:white">已出版</span>')
        elif self.status == "producing":
            format_td = format_html('<span style="padding:2px;background-color:pink;color:white">待出版</span>')
        return format_td

    #把colored_status字段显示成为status
    colored_status.short_description = 'status'
