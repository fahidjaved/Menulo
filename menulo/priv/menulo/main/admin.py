from django.contrib import admin
from .models import categories, Restaurant, dish, topic, sub_categories, review, size, price, Image, Slider





class SliderInline(admin.TabularInline):
    model = Slider
    list_display = ('id', 'name', 'imge','promos_img', 'restaurants', 'thumbnail')
    fields = ('name', 'promo','imge' )
    readonly_fields = ('imge',)
    raw_id_fields = ('promo',)
    


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'imagename', 'imge', )
    search_fields = ['img', ]
    list_display_links = ('name', 'imagename',)


class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'imge', 'restaurants', )
    search_fields = ['img', ]
    list_display_links = ('name',)
    raw_id_fields = ('restaurants', 'promo',)
    readonly_fields = ('thumbail',)


class sizeInline(admin.TabularInline):
    model = size


class priceInline(admin.TabularInline):
    model = price

class sub_categoriesInline(admin.TabularInline):
    model = sub_categories

class categoriesInline(admin.TabularInline):
    model = categories
    inlines = (sub_categoriesInline,)
    
class topicInline(admin.TabularInline):
    model = topic
    inlines = (categoriesInline,)

class dishInline(admin.TabularInline):
    model = dish
    inlines = (sub_categoriesInline,)





class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'absolute_url', 'img',
                    'allergene',
                    'zusatzstoffe', 'shisha_law', 'dish_access', 'shisha_price', 'shisha_sort', 'slider')
    search_fields = ['name']
    list_display_links = ('name',)
    raw_id_fields = ('user', 'logo',)
    inlines = [
        SliderInline,
        
    ]


class reviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user_review', 'restaurants')
    search_fields = ['name', 'user_review', 'restaurants']

    def restaurants(self, obj):
        return obj.Restaurant.name
    restaurants.admin_order_field = 'name'  # Allows column order sorting
    list_display_links = ('name',)


class topicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'restaurants', 'order_num')
    raw_id_fields = ('restaurants',)
    search_fields = ['name', 'restaurants__name']
    list_display_links = ('name',)
    


class categoriesAdmin(admin.ModelAdmin):
    # list_display = ('id','name','menu')
    model = categories
    list_display = ['id', 'name', 'menu', 'restaurant', 'order_num']

    def restaurant(self, obj):
        return obj.menu.restaurants.name
    restaurant.admin_order_field = 'name'  # Allows column order sorting
    raw_id_fields = ('menu',)
    search_fields = ['name', 'menu__name', 'menu__restaurants__name']
    list_display_links = ('name',)
    


class sizeAdmin(admin.ModelAdmin):
    # list_display = ('id','name','menu')
    model = size
    list_display = ['id', 'size', 'price', 'dish_id',
                    'sub_category', 'category', 'restaurant']

    def category(self, obj):
        return obj.dish_id.sub_category.category.name
    category.admin_order_field = 'name'  # Allows column order sorting

    def sub_category(self, obj):
        return obj.dish_id.sub_category.name
    sub_category.admin_order_field = 'name'  # Allows column order sorting

    def restaurant(self, obj):
        return obj.dish_id.sub_category.category.menu.restaurants.name
    restaurant.admin_order_field = 'name'  # Allows column order sorting

    raw_id_fields = ('dish_id',)
    search_fields = ['size', 'dish_id__title',
                     'dish_id__sub_category__category__menu__restaurants__name']
    list_display_links = ('size',)


class priceAdmin(admin.ModelAdmin):
    # list_display = ('id','name','menu')
    model = price
    list_display = ['id', 'price', 'cat_id', 'restaurant']

    def cat(self, obj):
        return obj.cat_id.name
    cat.admin_order_field = 'name'  # Allows column order sorting

    def restaurant(self, obj):
        return obj.cat_id.category.menu.restaurants.name
    restaurant.admin_order_field = 'name'  # Allows column order sorting
    raw_id_fields = ('cat_id',)
    search_fields = ['price', ]
    list_display_links = ('price',)


class dishAdmin(admin.ModelAdmin):
    model = dish
    list_display = ('id', 'img', 'number_AZ', 'title',
                    'description', 'price', 'sub_category', 'restaurant', 'order_num')
    list_per_page = 15
    raw_id_fields = ('restaurant', 'sub_category', 'image')
    search_fields = [
        'title', 'sub_category__category__menu__restaurants__name', 'sub_category__name']
    list_display_links = ('title',)

    def restaurant(self, obj):
        return obj.restaurant.name
    restaurant.admin_order_field = 'name'  # Allows column order sorting

    inlines = [
        sizeInline,
    ]


class sub_categoriesAdmin(admin.ModelAdmin):
    # list_display = ('id','name','category')
    model = sub_categories
    list_display = ['id', 'name', 'intro', 'category',
                    'menu', 'restaurant', 'order_num']

    def restaurant(self, obj):
        return obj.category.menu.restaurants.name
    restaurant.admin_order_field = 'name'  # Allows column order sorting

    def menu(self, obj):
        return obj.category.menu.name
    menu.admin_order_field = 'name'  # Allows column order sorting
    raw_id_fields = ('category',)
    search_fields = ['name', 'category__name',
                     'category__menu__name', 'category__menu__restaurants__name']
    list_display_links = ('name',)
    inlines = [
        priceInline,
    ]


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(topic, topicAdmin)
admin.site.register(categories, categoriesAdmin)
admin.site.register(sub_categories, sub_categoriesAdmin)
admin.site.register(dish, dishAdmin)
admin.site.register(review, reviewAdmin)
admin.site.register(size, sizeAdmin)
admin.site.register(price, priceAdmin)
admin.site.register(Image, ImageAdmin)
# admin.site.register(Slider,SliderAdmin)
# Register your models here.
