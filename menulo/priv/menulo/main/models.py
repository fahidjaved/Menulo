from django.db import models
from django.shortcuts import reverse
from autoslug import AutoSlugField
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.conf import settings

import os


class Image(models.Model):
    img = models.ImageField(upload_to="recipies/", blank=True)
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "9. Gallery"
        verbose_name = "Image"

    def imagename(self):
        return os.path.basename(self.img.name)

    def imge(self):
        if self.img:
            return mark_safe('<img src="%s" width="80" height="80" />' % (self.img.url))

    imge.short_description = 'Image'


class Restaurant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    slug = AutoSlugField(populate_from='name', always_update=True, blank=True)
    logo = models.ForeignKey(
        Image, on_delete=models.SET_NULL, blank=True, null=True, related_name="logo_image")
    allergene = models.TextField(blank=True)
    zusatzstoffe = models.TextField(blank=True)
    shisha_law = models.TextField(blank=True, verbose_name='Shisha Law')
    dish_access = models.BooleanField(default=False, verbose_name='Dish Price')
    shisha_price = models.BooleanField(default=False, verbose_name='Shisha Price')
    shisha_sort = models.BooleanField(default=False, verbose_name='Shisha Sorts')
    Guests = models.BooleanField(default=False, verbose_name='Gästeliste')
    slider = models.BooleanField(default=False, verbose_name='Promo Slider')

    class Meta:
        verbose_name_plural = "1. Restaurants"
        verbose_name = "Restaurant"

    def __str__(self):
        return self.name

    def absolute_url(self):
        return mark_safe('<a href="%s" target="_blank">Preview</a>' % ('/' + self.slug)
                         )

    absolute_url.short_description = 'Preview'

    def img(self):
        if self.logo:
            return mark_safe('<img src="%s" width="50" height="50" />' % (self.logo.img.url))

    img.short_description = 'logo'

    def promof_img(self):
        if self.promof:
            return mark_safe('<img src="%s" width="50" height="50" />' % (self.promof.img.url))

    promof_img.short_description = 'Promo 1st'

    def promos_img(self):
        if self.promos:
            return mark_safe('<img src="%s" width="50" height="50" />' % (self.promos.img.url))

    promos_img.short_description = 'Promo 2nd'

    def promot_img(self):
        if self.promot:
            return mark_safe('<img src="%s" width="50" height="50" />' % (self.promot.img.url))

    promot_img.short_description = 'Promo 3rd'


class Slider(models.Model):
    restaurants = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="promo_restaurants")
    promo = models.ForeignKey(
        Image, on_delete=models.SET_NULL, blank=True, null=True, related_name="slider_image",
        verbose_name='Promo Image')
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "10. Promo Slider"
        verbose_name = "Promo Slider"

    def thumbnail(self):
        return u'<img src="%s" width="50" height="50" />' % (self.promo.url)

    thumbnail.short_description = 'Thumbnail'

    def imagename(self):
        return os.path.basename(self.img.name)

    def imge(self):
        if self.promo:
            return mark_safe('<img src="%s" width="80" height="80" />' % (self.promo.img.url))

    imge.short_description = 'Promo Slider'


class review(models.Model):
    restaurants = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="review_restaurants", verbose_name='Restaurant')
    name = models.CharField(max_length=100, blank=True)
    user_review = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name_plural = "8. Feedbacks"
        verbose_name = "Feedback"


class GuestRegister(models.Model):
    vorname = models.CharField(max_length=128)
    nachname = models.CharField(max_length=128)
    tel_email = models.CharField(max_length=256, null=True, blank=True)
    road = models.CharField(max_length=256, null=True, blank=True)
    zip_code = models.CharField(max_length=16, null=True, blank=True)
    location = models.CharField(max_length=256, null=True, blank=True)
    restaurants = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, verbose_name='Restaurant')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class topic(models.Model):
    restaurants = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="topic_restaurants", verbose_name='Restaurant')
    name = models.CharField(max_length=100, blank=True)
    order_num = models.IntegerField(default=0, verbose_name='Order Nr')

    class Meta:
        verbose_name_plural = "2. Topics"
        verbose_name = "Topics"

    def __str__(self):
        return self.name


class categories(models.Model):
    menu = models.ForeignKey(
        topic, on_delete=models.CASCADE, related_name="catoegory_topics", verbose_name='Topic')
    name = models.CharField(max_length=100, blank=True)
    order_num = models.IntegerField(default=0, verbose_name='Order Nr')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "3. Categories"
        verbose_name = "Categories"


class sub_categories(models.Model):
    category = models.ForeignKey(
        categories, on_delete=models.CASCADE, related_name="sub_cat_categories")
    name = models.CharField(max_length=100, blank=True)
    intro = models.TextField(max_length=900, blank=True)
    order_num = models.IntegerField(default=0, verbose_name='Order Nr')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "4. Sub Categories"
        verbose_name = "Sub Categories"

    def intro_as_list(self):
        return self.intro.split('<br>')


class dish(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="dish_Restaurant", verbose_name='Restaurant')
    sub_category = models.ForeignKey(
        sub_categories, on_delete=models.CASCADE, related_name="dish_sub_categories", verbose_name='Sub Category')
    image = models.ForeignKey(
        Image, on_delete=models.SET_NULL, blank=True, null=True, related_name="dish_image")
    title = models.CharField(max_length=100, blank=True, verbose_name='Dish')
    description = models.CharField(max_length=500, blank=True)
    price = models.CharField(max_length=500, blank=True, null=True)
    number_AZ = models.CharField(max_length=100, blank=True, verbose_name='Nr. A|Z')
    slug = AutoSlugField(populate_from='title', unique_with=('title'), always_update=True, blank=True)
    order_num = models.IntegerField(default=0, verbose_name='Order Nr')

    class Meta:
        verbose_name_plural = "5. Dishes"
        verbose_name = "Dishes"

    def __str__(self):
        return self.title

    def absolute_url(self):
        return reverse("product", kwargs={
            'slug': self.slug
        })

    def img(self):
        if self.image:
            return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.img.url))

    img.short_description = 'Image'


class size(models.Model):
    dish_id = models.ForeignKey(
        dish, on_delete=models.SET_NULL, blank=True, null=True, related_name="size_dishs", verbose_name='Dish')
    size = models.CharField(max_length=100, blank=True)
    price = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.size

    class Meta:
        verbose_name_plural = "6. Sizes and Prices"
        verbose_name = "Size"


class price(models.Model):
    cat_id = models.ForeignKey(
        sub_categories, on_delete=models.SET_NULL, blank=True, null=True, related_name="price_cat",
        verbose_name='Price')
    price = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.price

    class Meta:
        verbose_name_plural = "7. Prices"
        verbose_name = "Price"
