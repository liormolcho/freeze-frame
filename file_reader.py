import os
import subprocess
import re

'''
ffmpeg -i 'https://storage.googleapis.com/hiring_process_data/freeze_frame_input
_a.mp4' -vf "freezedetect=n=-60dB:d=0.5,metadata=mode=print:file=freeze.txt" -map 0:v:0 -f null -
'''




class fileReader(object):

	def __init__(self, url, id):
		self.url = url
		self.file_name = str(id) +".txt"
		self.id = id 
		self.duration = self.read_and_filter()
		self.video_map = self.create_map_from_file()

	def read_and_filter(self):
		process  = subprocess.Popen(['ffmpeg', '-i', self.url, '-vf', "freezedetect=n=0.003,metadata=mode=print:file="+ self.file_name, '-map', '0:v:0', '-f', 'null', '-'], stderr=subprocess.PIPE)
		out = process.communicate()
		matches = re.search(r"Duration:\s{1}(?P<hours>\d+?):(?P<minutes>\d+?):(?P<seconds>\d+\.\d+?),", str(out), re.DOTALL).groupdict()
		t_hour = matches['hours']
		t_min  = matches['minutes']
		t_sec  = matches['seconds']

		t_hour_sec = int(t_hour) * 3600
		t_min_sec = int(t_min) * 60
		t_s_sec   = float(t_sec)

		total_sec = t_hour_sec + t_min_sec + t_s_sec

		return total_sec

	def create_map_from_file(self):
		f = open(self.file_name, "r")
		file_map = {}
		current_start = 0.00
		current_end = 0.00
		longest_valid_period = 0
		valid_periods = []
		sum_valid = 0
		for line in f:
			if 'lavfi.freezedetect.freeze_start' in line:
				current_start = float(line.split("=")[1])
				if current_start - current_end > longest_valid_period:
					longest_valid_period = current_start - current_end
				valid_periods.append([current_end, current_start])
				sum_valid += current_start - current_end
			if 'lavfi.freezedetect.freeze_end' in line:
				current_end = float(line.split("=")[1])
		if current_end < self.duration:
			valid_periods.append([current_end, self.duration])
		last_valid = self.duration - current_end
		sum_valid += last_valid
		longest_valid_period = longest_valid_period if longest_valid_period >= last_valid else last_valid
		file_map["longest_valid_period"] = longest_valid_period
		file_map["valid_video_percentage"] = sum_valid/self.duration
		file_map["valid_periods"] = valid_periods
		f.close()
		os.remove(self.file_name) 
		return file_map