from django.db import models

# Create your models here.




from django.db import models
from django.contrib.auth.models import User

course_type_choices = (('online', u'网络班'),
                       ('offline_weekend', u'面授班(周末)',),
                       ('offline_fulltime', u'面授班(脱产)',),
                       )


class School(models.Model):
    name = models.CharField(max_length=128,unique=True)
    city = models.CharField(max_length=64)
    addr = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    #关联django的user表，使用django的用户权限等功能,
    #最好使用onetoone,因为我自己关联django的表，我自己可以设置很多相同用户的名称，那么就乱了，所以这里我自己对django的user表也有限制，说一对一就是一对一
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    school = models.ForeignKey('School',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Customer(models.Model):
    qq = models.CharField(max_length=64,unique=True)
    name = models.CharField(max_length=32,blank=True,null=True)
    phone = models.BigIntegerField(blank=True,null=True)
    course = models.ForeignKey('Course',on_delete=models.CASCADE)

    course_type = models.CharField(max_length=64,choices=course_type_choices,default="offline_weekend")
    consult_memo = models.TextField()
    source_type_choices = (('qq',u"qq群"),
                   ('referral',u"内部转介绍"),
                   ('51cto',u"51cto"),
                   ('agent',u"招生代理"),
                   ('others',u"其它"),
                   )
    source_type = models.CharField(max_length=64,choices=source_type_choices)
    #自己关联自己，因为介绍人可能是内部人员，所以这里要自己关联自己
    referral_from = models.ForeignKey('self',blank=True,null=True,related_name="referraled_who",on_delete=models.CASCADE)
    status_choices = (('signed',u"已报名"),
                      ('unregistered',u"未报名"),
                      ('graduated',u"已毕业"),
                      ('drop-off','已退学')
                      )
    status = models.CharField(choices=status_choices,max_length=64)
    consultant = models.ForeignKey("UserProfile",on_delete=models.CASCADE,verbose_name='课程顾问')
    class_list = models.ManyToManyField("ClassList",blank=True,null=True)
    date = models.DateField(auto_now_add=True,verbose_name="咨询日期")

    def __str__(self):
        return "%s(%s)" %(self.qq,self.name)

class CustomerTrackRecord(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    track_record = models.TextField(verbose_name="跟踪记录")
    track_date = models.DateField(auto_now_add=True)
    follower = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    status_choices = ((1,u"近期无报名计划"),
                      (2,u"2个月内报名"),
                      (3,u"1个月内报名"),
                      (4,u"2周内报名"),
                      (5,u"1周内报名"),
                      (6,u"2天内报名"),
                      (7,u"已报名"),
                      )
    status = models.IntegerField(choices=status_choices, verbose_name="状态",help_text=u"选择客户此时的状态")
    def __str__(self):
        return self.customer

class Course(models.Model):
    name = models.CharField(max_length=64,unique=True)
    online_price = models.IntegerField()
    offine_price = models.IntegerField()
    introduction = models.TextField()

    def __str__(self):
        return self.name

class ClassList(models.Model):
    course = models.ForeignKey(Course,verbose_name="课程",on_delete=models.CASCADE)
    semester = models.IntegerField(verbose_name="学期")
    course_type = models.CharField(max_length=64,choices=course_type_choices,default="offline_weekend")
    teachers = models.ManyToManyField(UserProfile)
    start_date = models.DateField()
    graduate_date = models.DateField()

    def __str__(self):
        return "%s(%s)(%s)" %(self.course.name,self.course_type,self.semester)

    class Meta:
        #网络班，面授班，课程三个字段唯一，因为课程里面一个成员可能存在网络和面授班同时存在，所以不能2个字段唯一
        unique_together = ('course','semester','course_type')

class CourseRecord(models.Model):
    class_obj = models.ForeignKey(ClassList,on_delete=models.CASCADE)
    day_num = models.IntegerField(verbose_name="第几节课")
    course_date = models.DateField(auto_now_add=True,verbose_name="上课时间")
    teacher = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return "%s,%s" %(self.class_obj,self.day_num)

    class Meta:
        unique_together = ('class_obj','day_num')

class StudyRecord(models.Model):
    course_record = models.ForeignKey(CourseRecord,on_delete=models.CASCADE)
    student = models.ForeignKey(Customer,on_delete=models.CASCADE)
    record_choices = (('checked', u"已签到"),
                      ('late',u"迟到"),
                      ('noshow',u"缺勤"),
                      ('leave_early',u"早退"),
                      )
    record = models.CharField(choices=record_choices,default="checked",max_length=64,verbose_name="上课记录")
    score_choices = ((100, 'A+'),
                     (90,'A'),
                     (85,'B+'),
                     (80,'B'),
                     (70,'B-'),
                     (60,'C+'),
                     (50,'C'),
                     (40,'C-'),
                     (0,'D'),
                     (-1,'N/A'),
                     (-100,'COPY'),
                     (-1000,'FAIL'),
                     )
    score = models.IntegerField(choices=score_choices,default=-1,verbose_name="本节成绩")
    date = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=255,blank=True,null=True,verbose_name="备注")

    def __str__(self):
        return "%s,%s,%s" %(self.course_record,self.student,self.record)











