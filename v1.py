
# Function 1 the start of the pipeline
# Opens a file, reads it line by line


# Put in the r "raw" prefix before the regex, becuase python is flagging it, It will be used in the 
# Future.

classifer_dictionary = {
    "ssn": r"\d{3}-\d{2}-\d{4}",
    "AWSKey": r"AKIA\w{16}",
    "DOB": r"\d{2}-\d{2}-\d{4}",
    "CCard": r"\d{16}"
    }

#Completed the first iteration of the line scanner, matches found for dictionaries
"""Version 1 of the line scanner can only detect two digit dates of days and months."""



"""Splitting up the line scanner into different functions for the purpose of single responsibility"""

def ssn_scanner(text):
    ssn1_found = 0
    for i in range(0, len(text) - 10):
        chunk = text[i:i+11]
        if chunk[3] == '-' and chunk[6] == '-':
            if (chunk[0:3] + chunk[4:6] + chunk[7:11]).isdigit():
               ssn1_found += 1
    return ssn1_found



def dob_scanner(text):
    dob1_found = 0
    for i in range(0,len(text) - 9):
        chunk = text[i:i+10]
        month_str1 = chunk[0:2]
        day_str1 = chunk[3:5]
        year_str1 = chunk[6:10]
        if (chunk[2]== '-' or chunk[2] == '/') and (chunk[5] == '-' or chunk[5] == '/'):
            if month_str1.isdigit() and day_str1.isdigit() and year_str1.isdigit():
                month = int(month_str1)
                day = int(day_str1)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    dob1_found += 1
    return dob1_found


def awskey_scanner(text):
    awskey_found1 = 0
    for i in range(0,len(text) - 19):
        chunk = text[i:i+20]
        if chunk[0:4] == "AKIA" and chunk[4:20].isalnum():
            awskey_found1 += 1
    return awskey_found1


def ccnum_scanner1(text):
    cnum_found1 = 0
    for i in range(0,len(text) - 15):
        chunk = text[i:i+16]
        if chunk[0:16].isdigit():
            cnum_found1 += 1
    return cnum_found1


"""Second iteration: Each info type now has its own function, following single responbility practice
"""

#Calling each function
def call_scanner(text):
    ssn_count = ssn_scanner(text)
    dob_count = dob_scanner(text)
    awskey_count = awskey_scanner(text)
    cardnumber_count = ccnum_scanner1(text)

    return (ssn_count, dob_count, awskey_count, cardnumber_count)
print(call_scanner("4929381332664295, AKIAIOSFODNN7EXAMPLE,10/23/2023, 672-22-3334"))

def file_scan(file_name):
    #Scans the file line by line and will return a summary of sensitive data found
    #Produces a running total of sensitive info type found
    total_ssn = 0
    total_dob = 0
    total_awskey = 0
    total_cardnum = 0

    #'with' closes the file automatically, even if an error occurs
    with open(file_name) as f:
        #Reads one line at a time, large files don't load fully into memory
        for line in f:
          #call_scanner returns a tuple: ssn, dob, awskey, cardnum
          runscan = call_scanner(line)
          total_ssn += runscan[0]
          total_dob += runscan[1]
          total_awskey += runscan[2]
          total_cardnum += runscan[3]
        return f"Sensitive data found in: {file_name}\n Sensitive Content by Category: SSN:{total_ssn}, DOB:{total_dob}, AWS Key:{total_awskey}, Card Numbers:{total_cardnum}" 

