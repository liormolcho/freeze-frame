# freeze frame
 
the program downloads a set of video files from a given set of urls, runs a filter to find freeze frames, and returns the resulting json to be consumed by other api's.

when calculating the full length of the video, we get the full length from ffmpeg output.

the returned json will include:
		all_videos_freeze_frame_synced - keeps if all the videos are sunced freeze-wise
		videos: - list of data from each video
				longest_valid_period - the longest time without a freeze
				valid_video_percentage - sum of valid periods devided by the full length of the video. rounded to two decimal points
				valid_periods - list of times between freeze episodes. including between the last freeze and the end of the video.

# requirments
you need python on your machine.
you need ffmpeg on your machine.
i assumed the machine is a nix machine

# how to run
two ways to run.
command line:
python ./freeze_batch.py url1 url2 ....

through python:
from freeze_batch import freeze_filter
freeze_filter([URL1, URL2...])

# run tests:
to run tests from command line:
from freeze-frame folder:
python -m unittest discover