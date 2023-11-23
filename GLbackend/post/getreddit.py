import csv
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

#Get the current date and time
current_datetime = datetime.now()

#Format the datetime as a string (you can adjust the format as needed)
formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

csv_file_path = r'C:\Users\Admin\Documents\Glounge\GLbackend\post\valorant.csv'

#Read data from the CSV file and insert into the Django Post model
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row if it exists

    for row in csv_reader:
        dataname, dataselftext, datasubreddit, dataurl, datathumbnail = row
        if datasubreddit == 'elden ring' or datasubreddit == 'ELDEN RING':
            datasubreddit = 9
        elif datasubreddit == 'genshin impact'or datasubreddit == 'GENSHIN IMPACT':
            datasubreddit = 10
        elif datasubreddit == 'left 4 dead'or datasubreddit == 'LEFT 4 DEAD':
            datasubreddit = 11
        elif datasubreddit == 'minecraft'or datasubreddit == 'MINECRAFT':
            datasubreddit = 12
        elif datasubreddit == 'farlight'or datasubreddit == 'FARLIGHT':
            datasubreddit = 13
        elif datasubreddit == 'valorant'or datasubreddit == 'VALORANT':
            datasubreddit = 14
        elif datasubreddit == 'call of duty'or datasubreddit == 'CALL OF DUTY':
            datasubreddit = 15
        elif datasubreddit == 'counter strike'or datasubreddit == 'COUNTER STRIKE':
            datasubreddit = 16
        elif datasubreddit == 'pubg'or datasubreddit == 'PUBG':
            datasubreddit = 17
        elif datasubreddit == 'football manager'or datasubreddit == 'FOOTBALL MANAGER':
            datasubreddit = 18
        elif datasubreddit == 'rocket league'or datasubreddit == 'ROCKET LEAGUE':
            datasubreddit = 19           
        elif datasubreddit == 'league of legends'or datasubreddit == 'LEAGUE OF LEGENDS':
            datasubreddit = 20
        elif datasubreddit == 'dota 2'or datasubreddit == 'DOTA 2':
            datasubreddit = 21
        elif datasubreddit == 'sims'or datasubreddit == 'SIMS':
            datasubreddit = 22
        elif datasubreddit == 'roblox'or datasubreddit == 'ROBLOX':
            datasubreddit = 23
        elif datasubreddit == 'tekken'or datasubreddit == 'TEKKEN':
            datasubreddit = 24
        elif datasubreddit == 'final fantasy'or datasubreddit == 'FINAL FANTASY':
            datasubreddit = 25
        elif datasubreddit == 'super smash bro'or datasubreddit == 'SUPER SMASH BRO':
            datasubreddit = 26
        elif datasubreddit == 'phamophobia'or datasubreddit == 'PHASMOPHOBIA':
            datasubreddit = 27
        elif datasubreddit == 'diablo 4'or datasubreddit == 'DIABLO 4':
            datasubreddit = 28
        elif datasubreddit == 'gta 5'or datasubreddit == 'GTA 5':
            datasubreddit = 29
        elif datasubreddit == 'monster hunter'or datasubreddit == 'MONSTER HUNTER':
            datasubreddit = 30
        elif datasubreddit == 'mobile legends'or datasubreddit == 'MOBILE LEGENDS':
            datasubreddit = 31
        elif datasubreddit == 'nba'or datasubreddit == 'NBA':
            datasubreddit = 32
        elif datasubreddit == 'forza horizon 5'or datasubreddit == 'FORZA HORIZON 5':
            datasubreddit = 33
        else: 
            datasubreddit = 34
            
        # Assuming you have the user's ID or another way to identify the user
        user_id = '3e9fe50b5c31439f9fb68208a5c3dba9'
        user_instance = User.objects.get(id=user_id)

        # Create a new Post instance
        new_post = Post.objects.create(
            body=dataselftext,
            created_at=formatted_datetime,
            created_by_id=user_instance.id,
            is_private=False,
            game_title_id=datasubreddit,
            post_url=dataurl,
            outside_id=dataname
        )

        # Increment post_count in User model by 1 after creating a new post
        User.objects.filter(id=user_id).update(posts_count=F('posts_count') + 1)

        new_attachment = PostAttachment.objects.create(
            image_url=datathumbnail,
            created_by=user_instance
        )

        # Link this attachment to the specific Post instance
        new_post.attachments.add(new_attachment)
            