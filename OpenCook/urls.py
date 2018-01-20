from django.contrib import admin
from django.conf.urls import url

from mainapp.views import get_index, get_signup, post_signup, post_logout, post_login
from recipe.views import get_recipes_api, get_create_recipe, post_create_recipe, get_recipe


urlpatterns = [
    url('admin/', admin.site.urls),
    url('signup$', get_signup),
    url('signup/post$', post_signup),
    url('login/post$', post_login),
    url('logout/post$', post_logout),
    url('api/recipes$', get_recipes_api),
    url('recipes/(\d+)$', get_recipe),
    url('recipes/create$', get_create_recipe),
    url('recipes/create/post$', post_create_recipe),
    url('', get_index)
]

