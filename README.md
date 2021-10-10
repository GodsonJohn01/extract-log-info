# extract-log-info
This project intends to extract the required data from a log file using python

Steps to set up the project locally:

1. Clone the Repository `https://github.com/GodsonJohn01/extract-log-info.git`.
   Now, get into the repository `cd extract-log-info`

1. Install and activate virtualenv: 
    `pip install virtualenv` (ignore if already installed)
    `virtualenv venv`
    `source venv/bin/activate`

3. Install the requirements using `pip install -r requirements.txt`

4. Now, Run the main file  `python3 extract_log.py`.
   Congrats! You can see the output in the file `output.txt` if everything is right.

5. To run the test cases, simply run the command `pytest`
   It will automatically run the test file `test_extract_log.py` since it starts with keyword `test_`

6. To check the code coverage, `pytest --cov=.`


<hr>

### Notes
Issue in running the project?

Install all the specified requirements properly and try again. Thanks!
