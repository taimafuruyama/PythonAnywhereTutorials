# Turning a Python script into a website
# https://blog.pythonanywhere.com/169/
# https://www.pythonanywhere.com/user/tafuruyama/files/home/tafuruyama/mysite/processing.py?edit
# /home/tafuruyama/mysite/processing.py

import statistics

def process_data(input_data):
    result = ""
    for line in input_data.splitlines():
        if line != "":
            numbers = [float(n.strip()) for n in line.split(",")]
            result += str(sum(numbers))
        result += "\n"
    return result
