
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


def line_scanner2(text):
   ssn_found = 0
   for i in range(0,len(text) - 10):     #Non hardcoded numbers, adapts easily and doesnt break if condition is not met
      chunk = text[i:i+11]               #Grabs and 11-character slice of text, starting at indext i.
      if chunk[3] == '-' and chunk[6] == '-':
                  if (chunk[0:3] + chunk[4:6] + chunk[7:11]).isdigit():
                   ssn_found += 1
   dob_found = 0
   for i in range(0,len(text) - 9):
      chunk = text[i:i+10]
      month_str = chunk[0:2]
      day_str = chunk[3:5]
      year_str = chunk[6:10]

      if (chunk[2] == '-' or chunk[2] == '/') and (chunk[5] == '-' or chunk[5] == '/'):
          if month_str.isdigit() and day_str.isdigit() and year_str.isdigit():
              month = int(month_str)
              day = int(day_str)
              if 1 <= month <= 12 and 1 <= day <= 31:
               dob_found += 1

   awskey_found = 0

   for i in range(0,len(text) - 19):
       chunk = text[i:i+20]
       if (chunk[0:4] == "AKIA" and chunk[4:20].isalnum()): 
           awskey_found += 1


   cnum_found = 0
   for i in range(0,len(text) - 15):
       chunk = text[i:i+16]
       if chunk[0:17].isdigit():
           cnum_found += 1
   
   return f"Amount of SSNs: {ssn_found}\n" f"Amount of DOBs: {dob_found}\n" f"Amount of Keys: {awskey_found}\n" 



print(line_scanner2(text="06/07/1981,07/08/1981,08/09/1981,09/10/1981,489-36-8350,690-05-5315,12-20-6833,AKIAIOSFODNN7EXAMPLE"))

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
        if (chunk[2]== '-' or chunk[2] == '/' and chunk[5] == '2' or chunk[5] == '/'):
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
        if chunk[0:4] == "AKIA" and chunk[5:20].isalnum():
            awskey_found1 += 1
    return awskey_found1


def ccnum_scanner1(text):
    cnum_found1 = 0
    for i in range(0,len(text) - 15):
        chunk = text[i:i+16]
        if chunk[0:17].isdigit():
            cnum_found1 += 1
    return cnum_found1


"""Second iteration: Each info type now has its own function, following single responbility practice
"""

def call_scanner(text):
    ssn_count = ssn_scanner(text)
    dob_count = dob_scanner(text)
    awskey_count = awskey_scanner(text)
    cardnumber_count = ccnum_scanner1(text)

    return f"Amount of SSNs: {ssn_count}\nAmount of DOBs: {dob_count}\nAmount of AWS Keys: {awskey_count}\nAmount of Card Numbers: {cardnumber_count}"
print(call_scanner("4929381332664295, AKIAIOSFODNN7EXAMPLE,10/23/2023, 672-22-3334"))