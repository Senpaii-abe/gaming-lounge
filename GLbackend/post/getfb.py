import json
import requests
import sqlite3
from datetime import datetime
import os
import django
import sys
from django.db.models import F

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GLbackend.settings")
django.setup()

from post.models import Post, PostAttachment
from account.models import User
# Get the current date and time
current_datetime = datetime.now()

# Format the datetime as a string (you can adjust the format as needed)
formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

def get_group_feed(access_token):
    url = f'https://graph.facebook.com/v18.0/me?fields=groups%7Bname%2Cid%2Cfeed%7Bid%2Cmessage%2Cfull_picture%2Clink%7D%7D&access_token={access_token}'
    response = requests.get(url)
    data = response.json()
    return data['groups']['data']

# Provide the absolute path to your db.sqlite3 file
db_path = r'C:\Users\Admin\Documents\Glounge\GLbackend\db.sqlite3'

# Connect to the existing SQLite database
conn = sqlite3.connect(db_path)
# ... (rest of the script remains the same)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()


# Use the user access token you obtained
access_token = 'EAAMFfd1gTr8BO54uqkZBz29DVGzzVLaBAJNDs1wz1ZBN4HOBKDGctHFbzDcEfSLTQCLNkNr3OxDlpH4IfAdE4b6rDbvZA7ZAbMD11oDnT70Szuw3UgyESaB6q3pDbYVEQwcOj6dWGRpkPPkplQsoZB7FZB1ZCixHyuW5sbecQBbbVX3JoWF82NWwjmGSikJoaQGOi2QWuDSz9SqRbZAGD3c4ZCPQ68RWN2Q4eU2X9NcARUXNqlgfNu9Pxf8QPjqfTmAZDZD'

# Get the group feed
group_feed = get_group_feed(access_token)

# Loop through the data and insert into the existing SQLite database
for group in group_feed:
    group_id = group['id']
    game_title = group['name']
    for post in group['feed']['data']:
        post_id = post.get('id', 'N/A')
        if post_id != 'N/A':
            body = post.get('message', 'No message available')
            link = post.get('link', 'No link available')
            full_picture = post.get('full_picture', 'No picture available')
            
            user_id = '675a5aad3287452bba57b5aec4f60cc8'
            user_instance = User.objects.get(id=user_id)

            # Create a new Post instance
            new_post = Post.objects.create(
                body=body,
                created_at=formatted_datetime,
                created_by_id=user_instance.id,
                is_private=False,
                game_title_id=14,
                post_url=link,
                outside_id=post_id
            )
                            
            User.objects.filter(id=user_id).update(posts_count=F('posts_count') + 1)
                            
                            
            new_attachment = PostAttachment.objects.create(
                image_url=full_picture,
                created_by=user_instance
            )
            new_post.attachments.add(new_attachment)



#to list all the libraries installed-- "pip list"
#to deactivate environment -- "deactivate"
#to activate environment -- activate "name of environment"
#when changing directory -- cd D:\For coding\Glounge\GLbackend\account
#when running a file -- python "filename"