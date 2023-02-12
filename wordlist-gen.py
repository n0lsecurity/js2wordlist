import re
#open the file

file_js = open("main.js", "r", encoding="utf8")
#read the file

text = file_js.read()
#remove special characters

text = re.sub('[^A-Za-z0-9]+', ' ', text)
#convert the text into a list of words

words = text.split()
#remove duplicates

unique_words = list(set(words))
#save the words to a file

file_txt = open("wordlist-lms.txt", "w")
for word in unique_words:
   file_txt.write(word + "\n")
   
#close the file

file_js.close()
file_txt.close()
