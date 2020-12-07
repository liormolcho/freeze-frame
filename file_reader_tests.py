from file_reader import FileReader
import unittest

class TestFileReaderMethods(unittest.TestCase):

	def test_not_a_url(self):
		NOT_A_URL = "i'm not a url at all"
		with self.assertRaises(ValueError):
			FileReader(NOT_A_URL)

	def test_faulty_url(self):
		FAULTY_URL2 = "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_still_not_a_valid_url.mp4"
		with self.assertRaises(ValueError):
			FileReader(FAULTY_URL2)

	def test_valid_url(self):
		URL_1 = "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_a.mp4"
		fr = FileReader(URL_1)
		self.assertEqual(fr.duration, 29.06)
		self.assertEqual(fr.video_map['longest_valid_period'], 4.5045)
		self.assertEqual(fr.video_map['valid_video_percentage'], 0.47)
		self.assertEqual(fr.video_map['valid_periods'], [[0.0, 4.5045], [10.4271, 12.012], [14.2476, 18.018], [25.392, 29.06]])

	def test_valid_url2(self):
		URL_2 = "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_b.mp4"
		fr = FileReader(URL_2)
		self.assertEqual(fr.duration, 29.06)
		self.assertEqual(fr.video_map['longest_valid_period'], 4.5045)
		self.assertEqual(fr.video_map['valid_video_percentage'], 0.45)
		self.assertEqual(fr.video_map['valid_periods'], [[0.0, 4.5045], [10.6106, 12.0787], [14.4311, 18.018], [25.5755, 29.06]])

	def test_valid_url3(self):
		URL_3 = "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_c.mp4"
		fr = FileReader(URL_3)
		self.assertEqual(fr.duration, 26.76)
		self.assertEqual(fr.video_map['longest_valid_period'], 4.5045)
		self.assertEqual(fr.video_map['valid_video_percentage'], 0.51)
		self.assertEqual(fr.video_map['valid_periods'], [[0.0, 4.5045], [8.3083, 9.97663], [12.1288, 16.016], [23.2733, 26.76]])

if __name__ == '__main__':
    unittest.main()