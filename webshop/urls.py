from django.contrib import admin
from django.urls import path, include, re_path
from core.views import client_view
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseRedirect
from django.views import defaults as default_views
from rest_framework.authtoken.views import obtain_auth_token
from users.admin import admin_log




urlpatterns = [
    #path(settings.ADMIN_URL, admin.site.urls),
    path(settings.ADMIN_URL_OTP, admin_log.urls),
    path("accounts/", include("allauth.urls")),
    path("users/", include('users.urls', namespace='users')),
    path("merchandises/", include('merchandises.urls', namespace='merchandises')),
    path("carts/", include('carts.urls', namespace='carts')),
    path("purchases/", include('purchases.urls', namespace='purchases')),
    path("initial/", include('initial.urls', namespace='initial')),


    path('favicon.ico', lambda x: HttpResponseRedirect(settings.STATIC_URL + 'favicon.ico')),
     

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("webshop.api_router")),

    # DRF auth token
    path("auth-token/", obtain_auth_token),
     # Login via browsable api
    path("api-auth/", include("rest_framework.urls")),
    # Login via REST
    path("api/rest-auth/", include("rest_auth.urls")),
    # Registration via REST
    path("api/rest-auth/registration/", include("rest_auth.registration.urls")),
]


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]


# URL patterns for frontend 
urlpatterns += [
    #path("", include('core.urls', namespace='core')),
    # Catch all routes and redirect to index.html
    re_path(r"^.*$", view=client_view, name="client-app"),
]