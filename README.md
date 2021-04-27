# Photo Album
Create a console application that displays photo ids and titles in an album. The photos are available in this online web
service (https://jsonplaceholder.typicode.com/photos).
 Photos are filtered with a query string. This will return photos within albumId=3
(https://jsonplaceholder.typicode.com/photos?albumId=3)

## Requirements
Python >= 3.0.0

[`requirements.txt`](https://github.com/shifali-malhotra/photo-album/blob/main/requirements.txt)

## How to Build and Run Program
- Create a virtual environment for the project `python3 -m venv env`
  - `env` is the environment name
  - enter your virtual environment by running `source bin/activate` while within the generated `env` directory
  - pull this repository into the `env` directory
- Run `pip install -r requirements.txt`
- Run `python run.py << album_id >>`
  - `<< album_id >>` should be any album number between 1 and 100

## How to Run Tests
`python -m unittest test.py`

## Error Handling
- When given album id less than 0, prints out 'Album ID must be within 1 and 100'.
- When given album id greater than 100, prints out 'Album ID must be within 1 and 100'.
- When given a non-integer value for album id, prints out 'Album ID must be an integer'.
- When a bad response code is returned (i.e. 520), prints out 'Bad response, try again.'
