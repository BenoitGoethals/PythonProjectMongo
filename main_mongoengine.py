from mongoengine import connect, NotUniqueError
from dotenv import find_dotenv, load_dotenv
import os
import pprint

from posts import PostMetatag, Posts, PostCategory
from user import User

load_dotenv(find_dotenv())
password = os.getenv("MONGODB_PWD")
connection_string = f"mongodb+srv://benoitgoethals:{password}@cluster0.ds9qs.mongodb.net/"
connect(db='test_user', host=connection_string)

User.drop_collection()
Posts.drop_collection()


try:
    user = User(email='test@email.com')
    user.first_name = 'Paris'
    user.last_name = 'Nakita Kejser'
    user.save()
except NotUniqueError as e:
    print('E-mail allready found')


# Static params field updater
user = User.objects(email='test@email.com')
user.update(first_name='New Paris', last_name='Nakita Kejser')

# Dynamic params field updater
user2 = User.objects(email='test2@email.com')
fields = {
    'first_name': 'Secound Test',
    'last_name': 'Frist Last Name'
}
user2.update(**fields)
userss = User.objects()
for u in userss:
    print(u)


post_metatag = PostMetatag()
post_metatag.title = 'Test meta title'
post_metatag.description = 'meta test description'

post = Posts()
post.title = 'Hello world'
post.url = 'hello-world'
post.content = 'World is nice! :)'
post.metatag = post_metatag
post.status = 'pending'

post_category = PostCategory()
post_category.title = 'category title 1'
post_category.id = '5ea3f1a86f1ab83cc46c8cfc'
post.categorys.append(post_category)

post_category = PostCategory()
post_category.title = 'category title 2'
post_category.id = '5ea3f1e0c43137a34d5dd291'
post.categorys.append(post_category)

post.authors.append('5ea3f21351f65442e5e7383e')
post.authors.append('5ea3f219d65038bc607f70f5')
post.authors.append('5ea3f21e7515c00ee4abaec8')

post.save()
try:
    post = Posts.objects.get(pk="5ea3f264290e1c5733baa7b7")

    cat_inx = 1

    post_category = PostCategory()
    post_category.id = '5ea3f6cd34d222091bdae306'
    post_category.title = 'new push category title here'

    update_dict = {
        'set__metatag__title': 'new title changed',  # $set.metatag.title
        f'set__categorys__{cat_inx}__title': 'new category title',  # $set.categorys.0.title
        'push__authors': '5ea3f641e5e3bdda84df7269',  # $push.authors
    }
    post.update(**update_dict)

    update_dict = {
        'push__categorys': post_category,  # $push.categorys
    }
    post.update(**update_dict)

    post.authors.pop(2)


    post.save()
except Exception as e:
    print('Post not found')
