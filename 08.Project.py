#Create a python solution that reads the US Constitution, prompts for a search term, then displays the relevant sections.
#The text of the US Constitution can be found at https://brucebauer.info/constitution.txt. Click on the link, select all of the text, and paste it into your Codespace with a name of "constitution.txt".
#Open the file constitution.txt and read each line into a list. Be sure to strip out the linefeed character.
const=open ("constitution.txt", "r")
line=const.readline()
#Prompt for a search term (exit the program when the search term is blank)
#Search for the search term in each line. When the search term is found:
#Loop backwards from the current line to find the beginning of the section. Look for a blank line.
#Loop forwards from the current lint to find the end of the section. Look for a blank line.
#Print the section of text that contains the serach term along with the line number.
#Skip to the end of the section. Don't print the section twice if the search term is found twice.
#Prompt for another search term