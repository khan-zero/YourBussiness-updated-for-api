from django.db import models

# Create your models here.

class HeroSection(models.Model):

    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    yt_link = models.URLField()
    img = models.ImageField(upload_to='Media/img')

    class Meta:
        verbose_name_plural = 'HeroSections'
        verbose_name = 'HeroSection'

class Client(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='Media/clients')

    class Meta:
        verbose_name_plural = 'Clients'
        verbose_name = 'Client'


class AboutUs(models.Model):
    description = models.CharField(max_length=255)
    body = models.TextField()


    class Meta:
        verbose_name_plural = 'AboutUs'
        verbose_name = 'AboutUs'

class AboutUsOpp(models.Model):
    about = models.ForeignKey(AboutUs, on_delete=models.CASCADE)
    opportunities = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'AboutUsOpp'
        verbose_name = 'AboutUsOpp'

class WhyUS(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    img = models.ImageField(upload_to="media/why us")

    class Meta:
        verbose_name_plural = 'WhyUS'
        verbose_name = 'WhyUS'

class WhyUsQA(models.Model):            #questions and answers
    why_us = models.ForeignKey(WhyUS, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.TextField()

    class Meta:
        verbose_name_plural = 'WhyUsQA'
        verbose_name = 'WhyUsQA'

class Skills(models.Model):
    Title = models.CharField(max_length=255)
    Sub_Title = models.CharField(max_length=255)
    img = models.ImageField(upload_to="media/Skills")

    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

class SkillsUsage(models.Model):
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    usage = models.IntegerField()

    class Meta:
        verbose_name_plural = 'SkillsUsage'
        verbose_name = 'SkillsUsage'


class Service(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()
    icon = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Services'
        verbose_name = 'Service'


class CallToAction(models.Model):
    img = models.ImageField(upload_to='media/call to action')
    body = models.TextField()

    class Meta:
        verbose_name_plural = 'CallToAction'
        verbose_name = 'CallToAction'


class Portfolio(models.Model):
    img = models.ImageField(upload_to="media/portfolio")
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Member(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='media/profile pictures')

    x_link = models.URLField(null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.full_name


class Subscribe(models.Model):
    plan_name = models.CharField(max_length=255)
    price = models.IntegerField()

    list_item1 = models.CharField(max_length=255)
    list_item2 = models.CharField(max_length=255)
    list_item3 = models.CharField(max_length=255)
    list_item4 = models.CharField(max_length=255)
    list_item5 = models.CharField(max_length=255)


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    class Meta:
        verbose_name_plural = 'FAQ'
        verbose_name = 'FAQ'

    def __str__(self):
        return self.question

class Contact(models.Model):
    address = models.CharField(max_length=255)
    call_center = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Contact'
        verbose_name = 'Contact'

class FooterLiks(models.Model):
    x_link = models.URLField(null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#dashboard


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class DashActivities(models.Model):
    message = models.IntegerField()
    notifications = models.IntegerField()

    class Meta:
        verbose_name_plural = 'DashActivities'
        verbose_name = 'DashActivity'




