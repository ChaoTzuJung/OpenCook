from django.contrib import admin
from django.conf.urls import url, include

from mainapp.views import get_index, get_signup, post_signup, post_logout, post_login, get_shop
from recipe.views import get_recipes_api, get_create_recipe, post_create_recipe, get_recipe


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup$', get_signup),
    url(r'^signup/post$', post_signup),
    url(r'^login/post$', post_login),
    url(r'^logout/post$', post_logout),
    url(r'^api/recipes$', get_recipes_api),
    url(r'^recipes/(\d+)$', get_recipe),
    url(r'^recipes/create$', get_create_recipe),
    url(r'^recipes/create/post$', post_create_recipe),
    url(r'^shop$', get_shop),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', get_index),
]
