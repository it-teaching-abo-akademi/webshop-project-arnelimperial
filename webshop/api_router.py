from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path, include

from users.api.views import UserViewSet, UserCountView

from merchandises.api.views import MerchandiseViewset, MerchandiseCountView, MerchandiseOwnedByUserView

from carts.api.views import CartViewset, CartOwnedByUserView, UserCartViewSet

from purchases.api.views import PurchaseViewset, PurchasesByUserView, BuyerPurchasesViewSet, ItemBySellersViewSet


from initial.api.views import InitialViewset

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r"users", UserViewSet, basename='users')
router.register(r"user-counts", UserCountView, basename='user-counts')
router.register(r"merchandises", MerchandiseViewset, basename="merchandises")
router.register(r"merchandise-counts", MerchandiseCountView, basename='merchandise-counts')
router.register(r"merchandise-owned", MerchandiseOwnedByUserView, basename='merchandise-owned')
router.register(r"carts", CartViewset, basename='carts')
router.register(r"users-cart", CartOwnedByUserView, basename='users-cart')
router.register(r"customers-cart", UserCartViewSet, basename='customers-cart')
router.register(r"purchases", PurchaseViewset, basename='purchases')
router.register(r"purchases-buyer", BuyerPurchasesViewSet, basename='purchases-buyer')
router.register(r"purchases-sellers", ItemBySellersViewSet, basename='purchases-seller')




router.register("initial", InitialViewset, basename='initials')



app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
  
]

