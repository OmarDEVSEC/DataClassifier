
# Function 1 the start of the pipeline
# Opens a file, reads it line by line


classifer_dictionary = {
    "ssn": "\d{3}-\d{2}-\d{4}",
    "AWSKey": "AKIA\w{16}",
    "DOB": "\d{2}-\d{2}-\d{4}",
    "CCard": "\d{16}"
    }

#Completed the first iteration of the line scanner, matches found for dictionaries

def line_scanner(text):
    match_found = 0
    
    if len(text) == 11 and text[3] == '-' and text[6] == '-':
            match_found += 1
    print(match_found)
        
print(line_scanner("923-12-2222"))
