import unittest
import sys
import io
import responses

from photo_album import display_photos, run_program


class TestPhotoAlbum(unittest.TestCase):
    def test_album_id_must_be_integer(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        sys.argv[1] = 'abc'
        run_program()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), 'Album ID must be an integer\n')

    def test_album_id_must_be_greater_than_0(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        display_photos(0)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), 'Album ID must be within 1 and 100\n')

    def test_album_id_must_be_less_than_100(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        display_photos(101)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), 'Album ID must be within 1 and 100\n')

    @responses.activate
    def test_album_id_for_id_of_3(self):
        responses.add(
            responses.GET, 'https://jsonplaceholder.typicode.com/photos?albumId=3',
            json=[
              {
                "albumId": 3,
                "id": 101,
                "title": "incidunt alias vel enim",
                "url": "https://via.placeholder.com/600/e743b",
                "thumbnailUrl": "https://via.placeholder.com/150/e743b"
              }
            ],
            status=200
        )

        captured_output = io.StringIO()
        sys.stdout = captured_output
        display_photos(3)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), '[101] incidunt alias vel enim\n')
        self.assertEqual(len(responses.calls), 1)


    @responses.activate
    def test_bad_response(self):
        responses.add(
            responses.GET, 'https://jsonplaceholder.typicode.com/photos?albumId=3',
            status=520
        )

        captured_output = io.StringIO()
        sys.stdout = captured_output
        display_photos(3)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), 'Bad response, try again.\n')


if __name__ == '__main__':
    unittest.main()
    
