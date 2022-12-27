# Process Monitor using Python:
 
## Basic Setup:
* Create a venv using the command `python3 -m vevn env_name`
* Install the dependencies using the command `pip install -r requirements.txt`
* Create two folders `logs` & `complete` in the same directory where the file `monitor.py` exists.
* In the `auto_email.py` replace with the required recipient

## Running the Script:
* Run the script `run.py` or any other process to get a PID to monitor.
* Run the `monitor.py` script which will take three input `PID`, `Memory Constraint in MB`, `CPU usage in %`
* Exit with the help of `Ctrl+C`
* To plot the data, run the `plot.ipynb` & give the PID in the function call for the function `plot(PID)`
