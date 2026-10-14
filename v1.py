
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



# def line_scanner(text):
#     ssn_found = 0
#     dob_found = 0
#     if len(text) == 11:
#           if text[3] == '-' and text[6] == '-':
#             if (text[0:3] + text[4:6] + text[7:11]).isdigit():
#              ssn_found += 1
    
#     if len(text) == 10:
#        if (text[2] == '/' or text[2] == '-') and (text[5] == '/' or text[5] == '-'):
#           if (text[0:2]+ text[3:5]+ text[6:10]).isdigit():
#              dob_found += 1 
    
#     return f"Amount of SSNs: {ssn_found}\n Amount of DOBs: {dob_found}" 

# print(line_scanner(text = "923-12-2222, 09/23/2007"))



#Modified second intteration of the line scanner, scanning any text in a file and returning what is needed to be matched

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
      if (chunk[2] == '-' or chunk[2] == '/') and (chunk[5] == '-' or chunk[5] == '/'):
          if(chunk[0:2]+chunk[3:5]+chunk[6:10]).isdigit():
              print(chunk)
              dob_found += 1 
   return f"Amount of SSNs: {ssn_found}\n" f"Amount of DOBs: {dob_found}"

    

print(line_scanner2(text = "09/23/2007, 003-45-2134"))

#