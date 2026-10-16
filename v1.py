
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

   
   return f"Amount of SSNs: {ssn_found}\n" f"Amount of DOBs: {dob_found}"



print(line_scanner2(text="06/07/1981,07/08/1981,08/09/1981,09/10/1981,489-36-8350,690-05-5315,12-20-6833"))

"""Version 1 of the line scanner can only detect two digit dates of days and months."""

