Program by Raven6229
https://www.tumblr.com/blog/raven6229
https://www.tumblr.com/blog/sabotourist
feel free to use, just give credit and @ me on tumblr when you do (so that i can see what you make!)

this program requires something that can run a python script. i use visual studio code with python installed, personally

ScriptConversion.py is the code that converts a plain text file to HTML code that can be copy-pasted directly into ao3

note: custom formatting such as italics and bolds will be lost. 
    I like to mark them with an * asterisk and then find those spots and just italicize them manually in ao3 after

the code looks for a file called "script.txt" (no quotation marks, case sensitive) and then outputs "script_out.txt" which will be copy-paste friendly
i recommend turning it into an html file and checking it in your browser first before moving it to ao3, because ao3 makes it very annoying to edit after if there are mistakes

i included four files:
an example input, an example output, a blank html doc you can copy-paste into to test the code before uploading, and an example html

skin.css is what you'll want to edit if you want to add your own colors and usernames. follow the format used there. 
the name of the class must match the name being used in the txt file (not case sensitive)
the code is very prone to breaking if there are mistakes. make sure the text file has three blank lines at the end
Wash specifically is a special case, where the code manually uses epsilon's color. if you want to use his color, you can edit the python file around line 97.
    this is also how you make names that don't match the skin.css class name (like having wash use the epsilon color)

timestamps, as i've done them, must be formatted very specifically to have the code replace them properly with the right images, and to recognize that it is a timestamps
    follow my example closely on that

imgur links to my helmets are already included. you can replace those with your own images or choose not to include them entirely

dm me on tumblr with any questions, and i'll be happy to troubleshoot! odds are good you'll find some weird bugs here and there since i only ever meant for me to use this