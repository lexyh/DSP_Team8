## Author

**Team 8**

Hayden Puckeridge
Anna Ly
Suellen Fletcher
Alexis Henderson


## Description
This app is built to allow a user to point to a data file , load that file and automate some basic data exploration tasks:
1. load the file
2. display a summary of the file content
3. select columns to change to datetime format
4. display summary information such as: empty and null values, stastistical values for numeric columns, date summary for date columns and frequency of values for text columns.  

Note: currently files suitable to read in are limited to files in comma delimited format.

## Available Commands

In the project directory, you can run:

### `streamlit run streamlit_app.py`,

If you are using Pipenv, then you can run:

### `pipenv streamlit streamlit_app.py`

## Built With

- Python (3.8+)

## Package Dependencies
 - Streamlit
 - DataClass 
 - Pandas
 - Plotly
 
## Structure

    ├── README.md          <- Markdown file outlining the program and how to use.
    ├── docker-compose     <- Describe file
    ├── Dockerfile         <- Describe file
    ├── requirements       <- Describe file

    app
      ├── streamlit_app.py    <- Python file that reads in the files from 'src' and                                            initialises the program


    src
      ├── __init__ .py        <- Describe file
      ├── data.py             <- Python file that evaluates the content of the loaded csv file
      ├── datetime.py         <- Python file that defines a DateTime Column object and specifies  methods for that object. These methods are called in the streamlit_app.py file.
      ├── text.py             <- Python file that defines a TextColumn object and specifies methods for that object. These methods are called in the streamlit_app.py file.
      ├── numeric.py          <- Python file that defines a NumericColumn object and specifies methods for that object. These methods are called in the streamlit_app.py file.
      
      test
         ├── test_data.py    <- Python file that runs unit tests against the object defined in the data.py module.
         ├── test_datetime.py    <- Python file that runs unit tests against the object defined in the datetime.py module.
         ├── test_numeric.py    <- Python file that runs unit tests against the object defined in the numeric.py module.
         ├── test_text.py    <- Python file that runs unit tests against the object defined in the text.py module.



## TO SET UP IN DOCKER ##
Steps to set up and launch the program as a docker container are outlined below. 
This should allow users to run the program from the command line.
1. Download program files from the GitHub Repository https://github.com/lexyh/DSP_Team8.git  
2. Save the application files to a location on your local computer. 
3. download and install docker:
    - desktop, or
    - engine and compose separately
4. Open command line prompt 
5. In CMD type: cd the-application-path/DSP_Team8
6. In CMD type: docker-compose up -d
7. Open your web browser and navigate to: http://localhost: 8501 or localhost: 8501  

## ALTERNATIVELY RUN FROM COMMAND LINE ##
To run from command line instead: 
Navigate to the program location via the command line and type: streamlit run streamlit_app.py

Comments:
HP 27/10/21
to run tests:
python3 -m unittest src/test/test_datetime.py
must be run from this directory


