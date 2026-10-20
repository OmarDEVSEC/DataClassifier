

# Data Classifier Python Project Design

## Patterns to detect Version 1

- SSN: xxx-xx-xxxx
- Credit card: 16 digits, with or witbout dashes/spaces
- AWS-style API keys: It can start with AKIA followed by 16 alpanumeric chars

## Pipeline

- Open a file, read it line by line
- For each line, checks it against a known classified pattern
- Match is found: Record the (filename, line number, pattern type, and matched text)
- Prints a plain-text report for review
- Step 1 will be wrapped in a loop over a folder's files.