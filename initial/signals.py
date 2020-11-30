from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta, datetime
from .models import Initial
# from django.core.mail import send_mail, send_mass_mail, EmailMessage, EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags
from django.conf import settings
from django.contrib.auth import get_user_model
from merchandises.models import Merchandise
from django.contrib.auth.hashers import make_password

User = get_user_model()

@receiver(post_save, sender=Initial)
def delete_users_on_create(sender, instance=None, created=False, **kwargs):
    if created:
        users = User.objects.filter(is_staff=False)
        users.delete()

@receiver(post_save, sender=Initial)
def generate_users_on_create(sender, instance=None, created=True, **kwargs):

    users_count = User.objects.filter(is_staff=False).count()
    

    if users_count == 0:
        
        User.objects.bulk_create([
            User(
                username='testuser1',
                email='testuser1@shop.aa',
                password=make_password('pass1'),
                is_active=True,
            ),
             User(
                username='testuser2',
                email='testuser2@shop.aa',
                password=make_password('pass2'),
                is_active=True,
            ),
             User(
                username='testuser3',
                email='testuser3@shop.aa',
                password=make_password('pass3'),
                is_active=True,
            ),
             User(
                username='testuser4',
                email='testuser4@shop.aa',
                password=make_password('pass4'),
                is_active=True,
            ),
             User(
                username='testuser5',
                email='testuser5@shop.aa',
                password=make_password('pass5'),
                is_active=True,
            ),
             User(
                username='testuser6',
                email='testuser6@shop.aa',
                password=make_password('pass6'),
                is_active=True,
            ),

        ])
   

@receiver(post_save, sender=Initial)
def generate_default_users_items(sender, instance, created, **kwargs):

    users_count = User.objects.filter(is_staff=False).count()
    items = Merchandise.objects.all().count()
    user1 = User.objects.get(email='testuser1@shop.aa')
    user2 = User.objects.get(email='testuser2@shop.aa')
    user3 = User.objects.get(email='testuser3@shop.aa')

    u1 =  User.objects.all().filter(email='testuser1@shop.aa')

    if u1.exists():
        user1 = User.objects.get(email='testuser1@shop.aa')
        user_a = User.objects.get(id=user1.id)

        item1 = Merchandise.objects.create(
             title='Classic T-shirt',
             description='Standard T-shirt for everyday use',
             price='20,45',
             merchant=user_a
        )
        item2 = Merchandise.objects.create(
            title='Essential T-shirt',
            description='Just your everyday smooth, comfy tee',
            price='18,04',
            merchant=user_a
        )
        item3 = Merchandise.objects.create(
            title='Vintage T-shirt',
            description='Thick cotton vintage style',
            price='22,89',
            merchant=user_a
        )
        item4 = Merchandise.objects.create(
            title='Colored T-shirt',
            description='Everyday staple tee',
            price='17,55',
            merchant=user_a
        )
        item5 = Merchandise.objects.create(
            title='Dolor T-shirt',
            description='Rugged style tee',
            price='30,22',
            merchant=user_a
        )
        item6 = Merchandise.objects.create(
            title='Handmade sneaker',
            description='Vegetable-tanned, chromium-free, leathers',
            price='43,45',
            merchant=user_a
        )
        item7 = Merchandise.objects.create(
            title='Blue Leather Boots',
            description='Well, the way they make shows is, they make one show',
            price='256,88',
            merchant=user_a
        )
        item8 = Merchandise.objects.create(
            title='Kent Pattern',
            description='Comfortable canvas sneakers',
            price='70,77',
            merchant=user_a
        )
        item9 = Merchandise.objects.create(
            title='Men Boots',
            description='Casual ankle hight boots',
            price='315,24',
            merchant=user_a
        )
        item10 = Merchandise.objects.create(
            title='Black Dress Shoes',
            description='50-80% Handmade shoes for men',
            price='322,55',
            merchant=user_a
        )
    ########
    u2 =  User.objects.all().filter(email='testuser2@shop.aa')
    
    if u2.exists():
        user2 = User.objects.get(email='testuser2@shop.aa')
        user_b = User.objects.get(id=user2.id)
        
        item11 = Merchandise.objects.create(
            title='Dungaree Pinafore Dress',
            description='The pinafore looks perfect worn over a polo',
            price='49,64',
            merchant=user_b
        )
        item12 = Merchandise.objects.create(
            title='Bandana Dress',
            description='Hand-sewn in Bhutan',
            price='80,99',
            merchant=user_b
        )
        item13 = Merchandise.objects.create(
            title='Cotton Midi Dress',
            description='Tied waistband slim silhouette',
            price='75,74',
            merchant=user_b
        )
        item14 = Merchandise.objects.create(
            title='Turtleneck Sweater',
            description='Gray Sweatshirt Dress',
            price='78,90',
            merchant=user_b
        )
        item15 = Merchandise.objects.create(
            title= 'Oxford Leather',
            description='Shoes made with zakar fabric',
            price='86,32',
            merchant=user_b
        )
        item16 = Merchandise.objects.create(
            title='Leather sandals',
            description='Natural color Greek gladiator sandals',
            price='50,11',
            merchant=user_b
        ),
        item17 = Merchandise.objects.create(
            title='Breathable Running Shoes ',
            description='Lightweight Outdoor Beach Pool Exercise sneakers',
            price='40,00',
            merchant=user_b
        )
        item18 = Merchandise.objects.create(
            title=' Cognac Leather',
            description="Tan Leather Women's Oxford Shoes",
            price='120,33',
            merchant=user_b
        )
        item19 = Merchandise.objects.create(
            title='Knitted Slipper Boots',
            description='Indoor knitted slippers, House Shoes',
            price='30,23',
            merchant=user_b
        )
        item20 = Merchandise.objects.create(
            title="Women's Shirt",
            description='A unique and soft deep V-neck cut tee',
            price="19,26",
            merchant=user_b
        )
    ########
    u3 =  User.objects.all().filter(email='testuser3@shop.aa')

    if u3.exists():
        user3 = User.objects.get(email='testuser3@shop.aa')
        user_c = User.objects.get(id=user3.id)
        
        item21 = Merchandise.objects.create(
            title='Mens Foldable Earflap Cap',
            description='A classic winter cap made of high quality wool',
            price='30,99',
            merchant=user_c
        )
        item22 = Merchandise.objects.create(
            title='Seaman Mens Hat',
            description='Cap Stevedore Longshoreman Cloth',
            price='63,21',
            merchant=user_c
        )
        item23 = Merchandise.objects.create(
            title='Cotton Watch Cap',
            description='Navy blue Beanie hat unisex one size fits all',
            price='44,02',
            merchant=user_c
        )
        item24 = Merchandise.objects.create(
            title='Patrol Baseball Cap',
            description='Tweed Pure Wool Earflap Winter Cap',
            price='52,52',
            merchant=user_c
        )
        item25 = Merchandise.objects.create(
            title='Ranger Jockey Duty Cap',
            description='A warm and comfortable patrol cap',
            price='56,88',
            merchant=user_c
        )
        item26 = Merchandise.objects.create(
            title='Vintage Cotton Hat',
            description='Washed out, vintage look cap',
            price='35,77',
            merchant=user_c
        )
        item27 = Merchandise.objects.create(
            title='FULL-GRAIN LEATHER Shoes',
            description='Made of high-quality chromium free leathers',
            price='88,77',
            merchant=user_c
        )
        item28 = Merchandise.objects.create(
            title='Graphic Designer Shirt',
            description='Unisex t-shirt for everyday use',
            price='19,88',
            merchant=user_c
        )
        item29 = Merchandise.objects.create(
            title='Nantucket Baseball Hat',
            description="Easy-to-use adjustable strap, 100% cotton",
            price='33,04',
            merchant=user_c
        )
        item30 = Merchandise.objects.create(
            title='Porsche Hat',
            description='Distressed Outlaw Porsche 1963 Hat',
            price='34,77',
            merchant=user_c
        )
    

       
