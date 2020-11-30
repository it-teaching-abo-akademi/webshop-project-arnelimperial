from rest_framework import permissions
from merchandises.models import Merchandise
from carts.models import Cart
from django.contrib.auth import get_user_model

User = get_user_model()

class IsNotVendor(permissions.BasePermission):
    
   def has_permission(self, request, view):
    #    other = User.objects.get(pk=request.user.id)
    #    invalid_customer = Cart.objects.filter(customer=request.user.id).exists()

       if view.action == 'create' and not request.user:
           return True
       if view.action == 'list' and request.user.is_staff:
           return True
       if view.action == 'create' and request.user.is_staff:
           return True
       if view.action == 'destroy' and not request.user:
           return True
       else:
           return False

# def has_object_permission(self, request, view, obj):
#     print('enter has_object_permission')
#     # only allow the owner to make changes
#     user = self.get_user_for_obj(obj)
#     print(f'user: {user.username}')
#     if request.user.is_staff:
#         print('has_object_permission true: staff')
#         return True
#     elif view.action == 'create':
#         print('has_object_permission true: create')
#         return True
#     elif user == request.user:
#         print('has_object_permission true: owner')
#         return True # in practice, an editor will have a profile
#     else:
#         print('has_object_permission false')
#         return False

# def get_user_for_obj(self, obj):
#     model = type(obj)
#     if model is models.UserProfile:
#         return obj.user
#     else:
#         return obj.owner.user
