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
    url = f'https://graph.facebook.com/v18.0/me?fields=groups%7Bfeed%7Bid%2Cfull_picture%2Clink%2Cdescription%7D%2Cid%2Cname%7D&access_token={access_token}'
    response = requests.get(url)
    data = response.json()
    return data['groups']['data']

# Provide the absolute path to your db.sqlite3 file
db_path = r'C:\Users\Student\Dropbox\My PC (Joey)\Documents\Codes\Git\GLCapstone\gaming-lounge-1\GLbackend\db.sqlite3'

# Connect to the existing SQLite database
conn = sqlite3.connect(db_path)
# ... (rest of the script remains the same)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()


# Use the user access token you obtained
access_token = 'EAAMFfd1gTr8BOZCMqrXX587qpR5jkXr5ZAi7gxnS5uQE19nEoQ2C36AMME7psZBf2Q9Y4NihPTFMzfwkaRXPZChYsIHAQOhgvPNclUfEZAipuD4BnTCMGOHMKteK6roxTuZBt2JSP8zuLVLYTxs8Ysl5VjarMlFC65ZB4Peks0MLduZADQhBA4qHZCx0ZBMJI5KmmJqakwMZCQZBSuTsMN2tYAZDZD'

# Get the group feed
group_feed = get_group_feed(access_token)

# Loop through the data and insert into the existing SQLite database
for group in group_feed:
    group_id = group['id']
    game_title = group['name']
    for post in group['feed']['data']:
        post_id = post.get('id', 'N/A')
        if post_id != 'N/A':
            body = post.get('description', 'No message available')
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