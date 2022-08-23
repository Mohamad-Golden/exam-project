# Urls must start and end with slash

from views import exam, home


urlpatterns = {
    '/':home,
    '/exam/':exam
}