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


# Set the necessary parameters
CLIENT_ID = '2son5pbomhy29mng0zhzduqriouerl'
CLIENT_SECRET = 'j0djntmdw9mt269ar6ao1b3qfu96h1'
USER_LOGINS = ['kyedae', 'Dendi', 'ninja']  # Replace with the actual streamer's username

# Provide the absolute path to your db.sqlite3 file
db_path = r'C:\Users\Admin\Documents\Glounge\GLbackend\db.sqlite3'

# Connect to the existing SQLite database
conn = sqlite3.connect(db_path)
# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Make a request to get the OAuth token
token_response = requests.post(f'https://id.twitch.tv/oauth2/token'
                               f'?client_id={CLIENT_ID}'
                               f'&client_secret={CLIENT_SECRET}'
                               '&grant_type=client_credentials')

if token_response.status_code == 200:
    access_token = token_response.json()['access_token']
    headers = {
        'Client-ID': CLIENT_ID,
        'Authorization': f'Bearer {access_token}'
    }

    for USER_LOGIN in USER_LOGINS:
        # Get the user ID for the streamer
        user_response = requests.get(f'https://api.twitch.tv/helix/users?login={USER_LOGIN}', headers=headers)

        if user_response.status_code == 200:
            user_data = user_response.json()
            if user_data['data']:
                user_id = user_data['data'][0]['id']
                params = {
                    'user_id': user_id,
                    'first': 5,  # Retrieve the first 5 videos, adjust as needed
                    'sort': 'time'  # Sort the videos by time
                }

                # Make the GET request to the Twitch API with the OAuth token
                response = requests.get('https://api.twitch.tv/helix/videos', headers=headers, params=params)

                # Handle the API response
                if response.status_code == 200:
                    data = response.json()
                    if data['data']:
                        for video in data['data']:
                            
                            video_title = video['title']
                            video_url = f"https://www.twitch.tv/videos/{video['id']}"
                            post_id = video['id']
                            thumbnail_url = video['thumbnail_url']
                            view_count = video['view_count']
                            
                            print(f"Inserted video data for {USER_LOGIN}: {video_title}")
                            user_id = '1cfff9f31d814cb09028c3376871a4bb'
                            user_instance = User.objects.get(id=user_id)

                            # Create a new Post instance
                            new_post = Post.objects.create(
                                body=video_title,
                                created_at=formatted_datetime,
                                created_by_id=user_instance.id,
                                is_private=False,
                                game_title_id=9,
                                post_url=video_url,
                                outside_id=post_id
                            )
                            
                            User.objects.filter(id=user_id).update(posts_count=F('posts_count') + 1)
                            
                            
                            new_attachment = PostAttachment.objects.create(
                                image_url=thumbnail_url,
                                created_by=user_instance
                            )
                            new_post.attachments.add(new_attachment)
                            
                    else:
                        print(f"No videos found for the user {USER_LOGIN}.")
                else:
                    print(f"Error: {response.status_code} - {response.text}")
            else:
                print(f"No user found with the username {USER_LOGIN}.")
        else:
            print(f"Error: {user_response.status_code} - {user_response.text}")