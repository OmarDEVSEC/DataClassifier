
# Function 1 the start of the pipeline
# Opens a file, reads it line by line


classifer_dictionary = {
    "ssn": r"\d{3}-\d{2}-\d{4}",
    "AWSKey": r"AKIA\w{16}",
    "DOB": r"\d{2}-\d{2}-\d{4}",
    "CCard": r"\d{16}"
    }

#Completed the first iteration of the line scanner, matches found for dictionaries

def line_scanner(text):
    match_found = 0
    if len(text) == 11:
          if text[3] == '-' and text[6] == '-':
            if (text[0:3] + text[4:6] + text[7:11]).isdigit():
             match_found += 1
          print(match_found)
        
print(line_scanner("923-12-2222"))
