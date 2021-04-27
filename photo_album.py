#!/usr/bin/python

import sys
import requests

def run_program():
    if sys.argv[1].isdigit():
        album_id = int(sys.argv[1])
        display_photos(album_id)
    else:
        print('Album ID must be an integer')

def display_photos(album_id):
    if album_id < 1 or album_id > 100:
        print('Album ID must be within 1 and 100')
    else:
        response = requests.get(f"https://jsonplaceholder.typicode.com/photos?albumId={album_id}")

        if response.status_code == 200:
            for photo in response.json():
                print(f"{[photo.get('id')]} {photo.get('title')}")
        else:
            print("Bad response, try again.")
