from file_reader import FileReader
import json
import sys

class FreezeBatch(object):
	def __init__(self, arr_urls):
		self.file_readers = [FileReader(url) for url in arr_urls]
		self.videos_maps = [reader.video_map for reader in self.file_readers]
		self.freeze_frame_synced = self.are_synced()
		self.output = {}
		self.output["all_videos_freeze_frame_synced"] = self.freeze_frame_synced
		self.output["videos"] = self.videos_maps

	def are_synced(self):
		valid_periods = [period for period in self.videos_maps[0]['valid_periods']]
		num_periods = len(valid_periods)
		for video in self.videos_maps[1:]:
			video_valid_periods = [period for period in video['valid_periods']]
			if len(video_valid_periods) != num_periods:
				return False
			for i in range(len(video_valid_periods)):
				if abs(video_valid_periods[i][0] - valid_periods[i][0]) > 0.5 or abs(video_valid_periods[i][1] - valid_periods[i][1]) > 0.5:
					return False
		return True

	def get_output(self):
		return json.dumps(self.output)

def freeze_filter(url_list):
	fb = FreezeBatch(url_list)
	return fb.get_output()

if __name__ == '__main__':
     urls = sys.argv[1:]
     print(freeze_filter(urls))
