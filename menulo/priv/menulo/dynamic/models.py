from django.db import models
from django.shortcuts import reverse
from autoslug import AutoSlugField
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.conf import settings
from main.models import *


class Home(models.Model):     
    slider1 =models.ForeignKey(
        Image, on_delete=models.SET_NULL,blank=True, null=True,related_name="home_slider1",verbose_name='Slider 1 Image')
    slider1_text1 = models.CharField(max_length=100,blank=True,verbose_name='Slider 1 Text 1')
    slider1_text2 = models.CharField(max_length=100,blank=True,verbose_name='Slider 1 Text 2')
    slider1_text3 = models.CharField(max_length=100,blank=True,verbose_name='Slider 1 Text 3')
    button1_text = models.CharField(max_length=100,blank=True,verbose_name='Button 1 Text')
    slider2 =models.ForeignKey(
        Image, on_delete=models.SET_NULL,blank=True, null=True,related_name="home_slider2",verbose_name='Slider 2 Image')
    slider2_text1 = models.CharField(max_length=100,blank=True,verbose_name='Slider 2 Text 1')
    slider2_text2 = models.CharField(max_length=100,blank=True,verbose_name='Slider 2 Text 2')
    slider2_text3 = models.CharField(max_length=100,blank=True,verbose_name='Slider 2 Text 3')
    button2_text = models.CharField(max_length=100,blank=True,verbose_name='Button 2 Text')

    welcome =models.TextField(blank=True,verbose_name='Text Below Slider')  
    img1 =models.ForeignKey(
        Image, on_delete=models.SET_NULL,blank=True, null=True,related_name="home_img1",verbose_name='Image 1')
    title_text1 = models.CharField(max_length=400,blank=True,verbose_name='Title Text 1')
    desc_text1 = models.CharField(max_length=400,blank=True,verbose_name='Description Text 1')

    img2 =models.ForeignKey(
        Image, on_delete=models.SET_NULL,blank=True, null=True,related_name="home_img2",verbose_name='Image 2')
    title_text2 = models.CharField(max_length=400,blank=True,verbose_name='Title Text 2')
    desc_text2 = models.CharField(max_length=400,blank=True,verbose_name='Description Text 2')

    img3 =models.ForeignKey(
        Image, on_delete=models.SET_NULL,blank=True, null=True,related_name="home_img3",verbose_name='Image 3')
    title_text3 = models.CharField(max_length=400,blank=True,verbose_name='Title Text 3')
    desc_text3 = models.CharField(max_length=400,blank=True,verbose_name='Description Text 3')

    img4 =models.ForeignKey(
        Image, on_delete=models.SET_NULL,blank=True, null=True,related_name="home_img4",verbose_name='Image 4')
    title_text4 = models.CharField(max_length=400,blank=True,verbose_name='Title Text 4')
    desc_text4 = models.CharField(max_length=400,blank=True,verbose_name='Description Text 4')

    bottom_text=models.CharField(max_length=400,blank=True,verbose_name='Bottom Text')


    class Meta:
        verbose_name_plural = "1. Home"
        verbose_name = "Home"
       

    def __str__(self):
        return self.welcome    

    def sliderImg1(self):
        if self.slider1:
            return mark_safe('<img src="%s" width="50" height="50" />' % (self.slider1.img.url))
    sliderImg1.short_description='Slider 1 Image'

    def sliderImg2(self):
        if self.slider2:
            return mark_safe('<img src="%s" width="50" height="50" />' % (self.slider2.img.url))
    sliderImg2.short_description='Slider 2 Image'

    def Imag1(self):
        if self.img1:
            return mark_safe('<img src="%s" width="50" height="50" />' % (self.img1.img.url))
    Imag1.short_description='Image 1'

    def Imag2(self):
        if self.img2:
            return mark_safe('<img src="%s" width="50" height="50" />' % (self.img2.img.url))
    Imag2.short_description='Image 2'

    def Imag3(self):
        if self.img3:
            return mark_safe('<img src="%s" width="50" height="50" />' % (self.img3.img.url))
    Imag3.short_description='Image 3'

    def Imag4(self):
        if self.img4:
            return mark_safe('<img src="%s" width="50" height="50" />' % (self.img4.img.url))
    Imag4.short_description='Image 4'



class contact(models.Model):
    page_title = models.CharField(max_length=400,blank=True,verbose_name='Page Title')
    detail_html =models.TextField(blank=True,verbose_name='Detail Html') 

    class Meta:
        verbose_name_plural = "2. Kontakt"
        verbose_name = "Kontakt" 

    def __str__(self):
        return self.page_title 

class AGB(models.Model):
    page_title = models.CharField(max_length=400,blank=True,verbose_name='Page Title')
    detail_html =models.TextField(blank=True,verbose_name='Detail Html') 

    class Meta:
        verbose_name_plural = "3. AGB"
        verbose_name = "AGB" 

    def __str__(self):
        return self.page_title 

class data_protection(models.Model):
    page_title = models.CharField(max_length=400,blank=True,verbose_name='Page Title')
    detail_html =models.TextField(blank=True,verbose_name='Detail Html') 

    class Meta:
        verbose_name_plural = "4. Datenschutz"
        verbose_name = "Datenschutz" 

    def __str__(self):
        return self.page_title 

class imprint(models.Model):
    page_title = models.CharField(max_length=400,blank=True,verbose_name='Page Title')
    detail_html =models.TextField(blank=True,verbose_name='Detail Html') 

    class Meta:
        verbose_name_plural = "5. Impressum"
        verbose_name = "Impressum" 

    def __str__(self):
        return self.page_title 


