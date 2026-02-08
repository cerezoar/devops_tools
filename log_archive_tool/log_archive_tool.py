# /// script
# dependencies = []
# ///


# Requirements:
# Run in the command line and accepts the log directory as an input.
# Store the logs and store them in different directory.
# The tool should compress the file in tar.gz format.
# The tool assumes the all the files in the log directory are log files/

import tarfile
import os
from datetime import datetime

def create_output_filename(base_name="system_logs", datetime_str):
	pass

def compress(source_dir_file="/var/log/devops_logs", output_filename):
	pass


if __name__ == "__main__":
	pass
	# Current date and time
	current_date = datetime.now() # get the current date
	dt_filename_suffix = current_date.strftime("%Y-%m-%d_%H-%M-%S") # convert datetime to string format
	
	# Get the log file location / directory
	log_file_path = input("Enter the logs directory:")
	# Compress the directory and move to home location
	with tarfile.open(output_filename, "w:gz") as tar:
		tar.add()

