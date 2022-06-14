#importing from wikipedia database
import wikipedia as wiki
import ctypes

#get search keyword from user
word = input()
info=wiki.summary(word)

#showing message box
#limit to 400 characters
#"word" is the keyword you entered and displayed in the title of the box
ctypes.windll.user32.MessageBoxW(0,info[:400],word,0)