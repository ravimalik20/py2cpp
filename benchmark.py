import sys
from datetime import datetime
import os

input_files = sys.argv[1:]

ROUNDS = 50

RUN_FILE = "run.py"

# rounds, input_data
def stat(file_name, rounds):
	rounds_data = []

	for i in range(rounds):
		data = []

		translate_command = "python %s %s temp.cpp"%(RUN_FILE, file_name)
		os.system(translate_command)

		compile_command = "g++ temp.cpp"
		os.system(compile_command)

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
		for single_round in rounds_data[1]:
			python_time = single_round[0]
			cpp_time = single_round[1]

			temp = "%s,%s,%s\n"%(file_name, python_time, cpp_time)
			csv_string = csv_string + temp

	return csv_string

def exportCSV(csv_string):
	f = open(str(datetime.now())+".csv", "w")
	f.write(csv_string);

	f.close();

def main():
	input_files = sys.argv[1:]

	data = []

	for file_name in input_files:
		rounds_data = stat(file_name, ROUNDS)
		data.append([file_name, rounds_data])

	csv_string = prepareCSV(data)
	exportCSV(csv_string)

if __name__ == "__main__":
	main()
