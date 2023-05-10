from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    #描述，简介
    brief = models.CharField(null=True,blank=True,max_length=255)
    #外键的这个表用引号的原因是程序从上往下走的，这时候没有这个表，为了不报错，所以用引号
    category = models.ForeignKey("Category",on_delete=models.CASCADE)
    content = models.TextField(u"文章内容")
    author = models.ForeignKey("UserProfile",on_delete=models.CASCADE)
    pub_date = models.DateTimeField(blank=True,null=True)
    last_modify = models.DateTimeField(auto_now=True)
    #帖子置顶，给个优先级就行
    priority = models.IntegerField(u"优先级",default=1000)
    head_img = models.ImageField(u"文章标题图片",upload_to="uploads",blank=True,null=True)

    status_choices = (('draft',u"草稿"),
                      ('published',u"已发布"),
                      ('hidden',u"隐藏"),
                      )
    status = models.CharField(choices=status_choices,default='published',max_length=32)
    def __str__(self):
        return self.title
    #官网地址复制过来的:https://docs.djangoproject.com/en/3.2/ref/models/instances/#django.db.models.Model.clean
    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if self.status == 'draft' and self.pub_date is not None:
            raise ValidationError(('Draft entries may not have a publication date.'))
        # Set the pub_date for published items if it hasn't been set already.
        if self.status == 'published' and self.pub_date is None:
            self.pub_date = datetime.date.today()
class Comment(models.Model):
    article = models.ForeignKey(Article,verbose_name=u"所属文章",on_delete=models.CASCADE)
    #评论的层级关系字段
    parent_comment = models.ForeignKey('self',related_name='my_children',blank=True,null=True,on_delete=models.CASCADE)
    comment_choices = ((1,u'评论'),
                       (2,u"点赞"))
    comment_type = models.IntegerField(choices=comment_choices,default=1)
    user = models.ForeignKey("UserProfile",on_delete=models.CASCADE)
    comment = models.TextField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.comment_type == 1 and len(self.comment) ==0:
            raise ValidationError(u'评论内容不能为空，sb')


    def __str__(self):
        return "C:%s" %(self.comment)

class Category(models.Model):
    name = models.CharField(max_length=64,unique=True)
    #板块描述，简介
    brief = models.CharField(null=True,blank=True,max_length=255)
    #动态展示板块
    set_as_top_menu = models.BooleanField(default=False)
    #板块展示的顺序
    position_index = models.SmallIntegerField()
    #版主
    admins = models.ManyToManyField("UserProfile",blank=True)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=32)
    signature= models.CharField(max_length=255,blank=True,null=True)
    head_img = models.ImageField(height_field=150,width_field=150,blank=True,null=True)
    #for web qq
    friends = models.ManyToManyField('self',related_name="my_friends",blank=True)

    def __str__(self):
        return self.name

