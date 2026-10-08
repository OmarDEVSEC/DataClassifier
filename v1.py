
# Function 1 the start of the pipeline
# Opens a file, reads it line by line


classifer_dictionary = {
    "ssn": "\d{3}-\d{2}-\d{4}",
    "AWSKey": "AKIA\w{16}",
    "DOB": "\d{2}-\d{2}-\d{4}",
    "CCard": "\d{16}"
    }

#Completed the first iteration of the line scanner, matches found for

def line_scanner(text,linenumber):
    match_found = 0
    for char in text:
        if char[3] == '-' and char[6] == '-':
           match_found += 1
        

