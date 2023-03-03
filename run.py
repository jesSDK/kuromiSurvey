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
        print("e.g: 1,2,3,4,5,6,7,8,9")
        data_str = input("Please enter the results: \n") #Enter results, new line for heroku bug

        results = data_str.split(',')
        if validate_results(results):
            break #if results are valid break the while loop
    return results

def validate_results(results):
    """
    Validates the results to ensure numerical and within the range we are expecting 0-10
    """
    try:
        [int(value) for value in results]
        if len(results) != 9:
            raise ValueError (f"Expected 9 results, got {len(results)}")
        for value in results:
            if (int(value) > 10 or int(value) < 0): #If value is higher than 10 or less than 0 including negatives numbers
                raise ValueError(f"Expected a result between 0-10, got {value}")
    except ValueError as e:
        print (f"Error: {e}")
        return False #return false if data is invalid
    return True 

def update_spreadsheet(data):
    """
    Updates our spreadsheet with the latest data
    """
    print("Updating survey results...\n")
    sheet_to_update = SHEET.worksheet("survey_results")
    sheet_to_update.append_row(data) #Adds our new data to the spreadsheet
    print("Updated results!")

def calculate_average_result():
    """
    Calculates the average score per age group
    """
    print("Calculating average score per age...")
    sheet = SHEET.worksheet("survey_results")
    results = []
    x = 1
    while x <= sheet.col_count: #iterate for each column in the worksheet
        col_values = sheet.col_values(x)
        values = [int(value) for value in col_values]
        values.pop(0) #Remove first value from each list as it contains our age
        results.append(values)
        total = sum(values)
        average = round(total / len(values)) #Calculate the average
        print(f"Age: {x+15} , average score: {average}/10")
        x+=1
    print("Calculated!")



def main():
    """
    Runs all our functions for the program 
    """
    data = enter_survey_results()
    update_spreadsheet(data)
    calculate_average_result()
main()