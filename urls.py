# Urls must start and end with slash
# Set static_root to determine the location and url of the static

from views import exam, home

urlpatterns = {
    '/':home,
    '/exam/':exam,
}

static_root = 'static/'