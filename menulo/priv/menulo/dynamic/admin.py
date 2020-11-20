from django.contrib import admin
from .models import *
from main.admin import SliderInline



class HomeAdmin(admin.ModelAdmin):
    list_display = ('id','sliderImg1', 'slider1_text1','slider1_text2','slider1_text3','button1_text',
                    'sliderImg2','slider2_text1','slider2_text2','slider2_text3','button2_text','welcome',
                    'Imag1','title_text1','desc_text1','Imag2','title_text2','desc_text2','Imag3','title_text3','desc_text3','Imag4','title_text4','desc_text4','bottom_text')
    search_fields = ['welcome']
    list_display_links = ('slider1_text1',)
    raw_id_fields = ( 'slider1','slider2','img1','img2','img3','img4',)


class contactAdmin(admin.ModelAdmin):
    list_display = ('id', 'page_title','detail_html')
    search_fields = ['page_title']
    list_display_links = ('page_title',)

class AGBAdmin(admin.ModelAdmin):
    list_display = ('id', 'page_title','detail_html')
    search_fields = ['page_title']
    list_display_links = ('page_title',)

class data_protectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'page_title','detail_html')
    search_fields = ['page_title']
    list_display_links = ('page_title',)

class imprintAdmin(admin.ModelAdmin):
    list_display = ('id', 'page_title','detail_html')
    search_fields = ['page_title']
    list_display_links = ('page_title',)
    
    

admin.site.register(Home, HomeAdmin)
admin.site.register(contact, contactAdmin)
admin.site.register(AGB, AGBAdmin)
admin.site.register(data_protection, data_protectionAdmin)
admin.site.register(imprint,imprintAdmin)