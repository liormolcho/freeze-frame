from freeze_batch import FreezeBatch, freeze_filter
import unittest

class TestFreezeBatchMethods(unittest.TestCase):

	def test_with_one_url_is_equal(self):
		URL_1 = "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_a.mp4"
		fb = FreezeBatch([URL_1])
		self.assertTrue(fb.freeze_frame_synced)
		self.assertEqual(len(fb.file_readers), 1)
		self.assertEqual(fb.get_output(), '{"all_videos_freeze_frame_synced": true, "videos": [{"longest_valid_period": 4.5045, "valid_video_percentage": 0.47, "valid_periods": [[0.0, 4.5045], [10.4271, 12.012], [14.2476, 18.018], [25.392, 29.06]]}]}')

	def test_with_two_synced_urls_is_synced(self):
		URL_1 = "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_a.mp4"
		URL_2 = "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_b.mp4"
		fb = FreezeBatch([URL_1, URL_2])
		self.assertTrue(fb.freeze_frame_synced)
		self.assertEqual(len(fb.file_readers), 2)
		self.assertEqual(fb.get_output(), '{"all_videos_freeze_frame_synced": true, "videos": [{"longest_valid_period": 4.5045, "valid_video_percentage": 0.47, "valid_periods": [[0.0, 4.5045], [10.4271, 12.012], [14.2476, 18.018], [25.392, 29.06]]}, {"longest_valid_period": 4.5045, "valid_video_percentage": 0.45, "valid_periods": [[0.0, 4.5045], [10.6106, 12.0787], [14.4311, 18.018], [25.5755, 29.06]]}]}')

	def test_freeze_filter_returns_same_output(self):
		URL_1 = "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_a.mp4"
		URL_2 = "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_b.mp4"
		fb = FreezeBatch([URL_1, URL_2])
		self.assertTrue(fb.freeze_frame_synced)
		self.assertEqual(len(fb.file_readers), 2)
		self.assertEqual(fb.get_output(), freeze_filter([URL_1, URL_2]))

	def test_with_two_synced_urls_is_synced_different_order(self):
		URL_1 = "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_a.mp4"
		URL_2 = "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_b.mp4"
		fb = FreezeBatch([URL_2, URL_1])
		self.assertTrue(fb.freeze_frame_synced)
		self.assertEqual(len(fb.file_readers), 2)
		self.assertEqual(fb.get_output(), '{"all_videos_freeze_frame_synced": true, "videos": [{"longest_valid_period": 4.5045, "valid_video_percentage": 0.45, "valid_periods": [[0.0, 4.5045], [10.6106, 12.0787], [14.4311, 18.018], [25.5755, 29.06]]}, {"longest_valid_period": 4.5045, "valid_video_percentage": 0.47, "valid_periods": [[0.0, 4.5045], [10.4271, 12.012], [14.2476, 18.018], [25.392, 29.06]]}]}')

	
	def test_with_two_unsynced_urls_is_not_synced(self):
		URL_1 = "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_a.mp4"
		URL_3 = "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_c.mp4"
		fb = FreezeBatch([URL_1, URL_3])
		self.assertFalse(fb.freeze_frame_synced)
		self.assertEqual(len(fb.file_readers), 2)
		self.assertEqual(fb.get_output(), '{"all_videos_freeze_frame_synced": false, "videos": [{"longest_valid_period": 4.5045, "valid_video_percentage": 0.47, "valid_periods": [[0.0, 4.5045], [10.4271, 12.012], [14.2476, 18.018], [25.392, 29.06]]}, {"longest_valid_period": 4.5045, "valid_video_percentage": 0.51, "valid_periods": [[0.0, 4.5045], [8.3083, 9.97663], [12.1288, 16.016], [23.2733, 26.76]]}]}')

	def test_with_two_unsynced_urls_is_not_synced_different_order(self):
		URL_1 = "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_a.mp4"
		URL_3 = "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_c.mp4"
		fb = FreezeBatch([URL_3, URL_1])
		self.assertFalse(fb.freeze_frame_synced)
		self.assertEqual(len(fb.file_readers), 2)
		self.assertEqual(fb.get_output(), '{"all_videos_freeze_frame_synced": false, "videos": [{"longest_valid_period": 4.5045, "valid_video_percentage": 0.51, "valid_periods": [[0.0, 4.5045], [8.3083, 9.97663], [12.1288, 16.016], [23.2733, 26.76]]}, {"longest_valid_period": 4.5045, "valid_video_percentage": 0.47, "valid_periods": [[0.0, 4.5045], [10.4271, 12.012], [14.2476, 18.018], [25.392, 29.06]]}]}')


	def test_with_two_synced_urls_and_one_not(self):
		URL_1 = "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_a.mp4"
		URL_2 = "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_b.mp4"
		URL_3 = "https://storage.googleapis.com/hiring_process_data/freeze_frame_input_c.mp4"
		fb = FreezeBatch([URL_1, URL_2, URL_3])
		self.assertFalse(fb.freeze_frame_synced)
		self.assertEqual(len(fb.file_readers), 3)
		self.assertEqual(fb.get_output(), '{"all_videos_freeze_frame_synced": false, "videos": [{"longest_valid_period": 4.5045, "valid_video_percentage": 0.47, "valid_periods": [[0.0, 4.5045], [10.4271, 12.012], [14.2476, 18.018], [25.392, 29.06]]}, {"longest_valid_period": 4.5045, "valid_video_percentage": 0.45, "valid_periods": [[0.0, 4.5045], [10.6106, 12.0787], [14.4311, 18.018], [25.5755, 29.06]]}, {"longest_valid_period": 4.5045, "valid_video_percentage": 0.51, "valid_periods": [[0.0, 4.5045], [8.3083, 9.97663], [12.1288, 16.016], [23.2733, 26.76]]}]}')
	
if __name__ == '__main__':
    unittest.main()