This file explain how to use data_collection.py
===============================================


Script 'data_collection.py' is an interactive Python script that will ask following questions:

1. How many commands do you want to run? > expectes integer value
2. How many times do you want this to be collected? > expectes integer value
3. Interval in seconds? > expects integer value

After that it will start collecting output of commands from point 1 for number of times from point 2 and the interval is seconds from point 3.

At the moment it expects output value to be passed as parameter, so to start:

# python data_collection.py output_file

Script can also be made executable with:

# chmod +x data_collection.py

and run:

# ./data_collection.py output_file


