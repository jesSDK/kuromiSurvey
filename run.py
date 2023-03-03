import gspread
from google.oauth2.service_account import Credentials

SCOPE = [ 
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ] #scope for our APIs

CREDS = Credentials.from_service_account_file('creds.json') #Define our credentials
SCOPED_CREDS = CREDS.with_scopes(SCOPE) #Define our scope, with credentials
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS) #Pass scope and credentials to our client
SHEET = GSPREAD_CLIENT.open('KuromiSurvey') #Open our sheet with the client

def enter_survey_results():
    """
    Allows user to enter in the latest survery results
    """
    while True: #Loop until we get valid data
        print("Please enter the survey results, seperated by a coma, for each age range from 16 to 24")
        print("e.g: 6,7,2,4,6,9,1,9")
        data_str = input("Please enter the results: \n")

        results = data_str.split(',')
        if validate_results(results):
            break
    return results

def validate_results(results):
    """
    Validates the results to ensure numerical and within the range we are expecting 0-10
    """
    try:
        [int(value) for value in results]
        if len(results) != 8:
            raise ValueError (f"Expected 8 results, got {len(results)}")
        for value in results:
            if (int(value) > 10 or int(value) < 0):
                raise ValueError(f"Expected a result between 0-10, got {value}")
    except ValueError as e:
        print (f"Error: {e}")
        return False #return false if data is invalid
    return True 

def main():
    """
    Runs all our functions for the program 
    """
    enter_survey_results()
main()