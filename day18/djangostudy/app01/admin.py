from django.contrib import admin

# Register your models here.



from app01 import models


#actions的主函数，这里面几个参数基本都是固定的，直接使用就行
def make_published(modelAdmin,request,queryset):
    print ("---->",request,queryset)
    #2.把status的值改为"published"
    queryset.update(status='published')
    #3.在选项框的描述
    make_published.short_description = "Set to published"



class BookAdmin(admin.ModelAdmin):
    #1.status字段一定要在后台显示出来啊，不然改什么？
    list_display = ('id','title','publisher','status','colored_status')
    #这里为什么有publisher__name,如果要上搜索publisher，上面的list_display只显示了publisher的name，如果不加上 __name，那么就会报错，需要搜索的东西一定要在页面上能显示
    search_fields = ('title','publisher__name')
    #过滤条件只能是list或者tuple，看报错（<class 'app01.admin.BookAdmin'>: (admin.E112) The value of 'list_filter' must be a list or tuple.）
    #就是如果只有个选择，一定要在屁股后面加个逗号，不然报错
    list_filter = ('title','publisher')
    list_per_page = 10
    #如果只有一个参数，一定要加上  逗号 ，否则报错
    filter_horizontal = ('authors',)
    #这里一定要有一个不可变唯一参数，不然无法进入编辑，所以，在list_display，新增了一个id的显示
    list_editable = ('title','publisher')
    #4.把actions关联到book表上面
    actions = [make_published,]


admin.site.register(models.Author)
admin.site.register(models.Book,BookAdmin)
admin.site.register(models.Publisher)