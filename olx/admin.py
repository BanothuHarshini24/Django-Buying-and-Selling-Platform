from django.contrib import admin
from .models import post,Profile,signed,wishlist,cart,verify_post,myorders,week_bid,reports,not_verify
# Register your models here.
admin.site.register(post)
admin.site.register(Profile)
admin.site.register(signed)
admin.site.register(wishlist)
admin.site.register(cart)
admin.site.register(verify_post)
admin.site.register(myorders)
admin.site.register(week_bid)
admin.site.register(reports)
admin.site.register(not_verify)