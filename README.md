# Photo Album
Create a console application that displays photo ids and titles in an album. The photos are available in this online web
service (https://jsonplaceholder.typicode.com/photos).
 Photos are filtered with a query string. This will return photos within albumId=3
(https://jsonplaceholder.typicode.com/photos?albumId=3)

## Requirements
Python >= 3.0.0

[`requirements.txt`](https://github.com/shifali-malhotra/photo-album/blob/main/requirements.txt) Contains the latest version of the packages

## How to Build and Run Program
- Run `pip install -r requirements.txt`
- Run `python photo_album.py <<albumId>>`
  - `albumId` should be any album number between 1 and 100

## How to Run Tests
`python -m unittest test.py`
