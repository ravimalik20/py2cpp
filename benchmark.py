#!/usr/bin/python

import sys
from datetime import datetime
import os

input_files = sys.argv[1:]

ROUNDS = 50

RUN_FILE = "run.py"

# rounds, input_data
def stat(file_name, rounds):
	rounds_data = []

	translate_command = "python %s %s temp.cpp"%(RUN_FILE, file_name)
	os.system(translate_command)

	compile_command = "g++ temp.cpp"
	os.system(compile_command)

	for i in range(rounds):
		data = []

		python_stat_command = "python %s"%file_name
		begin = datetime.now()
		os.system(python_stat_command)
		end = datetime.now()
		elapsed_time = end - begin
		data.append(elapsed_time.microseconds)

		cpp_stat_command = "./a.out"
		begin = datetime.now()
		os.system(cpp_stat_command)
		end = datetime.now()
		elapsed_time = end - begin
		data.append(elapsed_time.microseconds)

		rounds_data.append(data)

	return rounds_data

def prepareCSV(data):
	csv_string = ""

	for rounds_data in data:
		file_name = rounds_data[0]

		for i in range(len(rounds_data[1])):
			single_round = rounds_data[1][i]

			python_time = single_round[0]
			cpp_time = single_round[1]

			temp = "%s,%s,%s,%s\n"%(file_name, i, python_time, cpp_time)
			csv_string = csv_string + temp

	return csv_string

def exportCSV(csv_string):
	if (len(csv_string) > 0):
		f = open(str(datetime.now())+".csv", "w")

		# Write header on the CSV file
		f.write("Filename,Round,Time Python,Time Cpp\n")
		# Write CSV data to file
		f.write(csv_string);

		f.close();

def cleanup():
	os.system("rm -f temp.cpp")
	os.system("rm -f a.out");

def main():
	input_files = sys.argv[1:]

	data = []

	for file_name in input_files:
		rounds_data = stat(file_name, ROUNDS)
		data.append([file_name, rounds_data])

	csv_string = prepareCSV(data)
	exportCSV(csv_string)

	cleanup()

if __name__ == "__main__":
	main()
