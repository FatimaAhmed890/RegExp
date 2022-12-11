# RegExp

This script is intended to strip out the Domain Name and Top Level Domain from a url provided in a text file and store the result in another text file. 

First we have a utility function called Domain Name:
It's purpose is to compare the given url with the provided pattern of a regular expression.
-In the 1st line of the function we compile a regular expression pattern using re.compile as a string into a regex pattern object in Python.
-In the 2nd line we call the sub() function which stands for substring on the pattern object which returns a string with replaced values, which is stored in a
variable called domain_tld.
-Lastly we just return the variable.

Secondly we have a try/except block in which:
-In the try block
  1- We first open the file in read mode.
  2-Then store all the content line by line using readlines() function in list form inside of read variable.
  3-Now we create a new file and then loop over the each url in 'read' list and call our utility function on each url and store it in a variable, and then finally 
  write the content of that variable inside of the output file.
  4-Then we close the file and print done if execution was successful.
-In except block we throw our exception which in this case is an error message being printed on the screen in case of any error encountered.
