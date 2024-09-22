# chatlog\_formatting

****

Parse an input txt file to create a chatfic for AO3. Designed for RVB fics

Program by Raven6229

https://www.tumblr.com/blog/raven6229

https://www.tumblr.com/blog/sabotourist

Feel free to use, just give credit and @ me on tumblr when you do (so that i can see what you make!)

**Tested on python3.12**

## Setup
Install Python 3.12

Download the program from github as a zip file and un-zip, or git clone the project.

Open Terminal and navigate to where this project was downloaded (Use `cd /{directory_name}` and `ls` to navigate the terminal)

Run the following commands in order
```
python3.12 -m venv /.venv
source .venv/bin/activate
pip install -e .
```
The program can then be ran using the following command
```
bin/run
```

## File Structure
├── bin
|   ├── run                                     # Setup file to run the script
├── config
|   ├── config.json                             # Config file for icons
|   ├── skin.css                                # CSS file for the generated HTML
├── example_files
|   ├── template.html                           # Template html file
├── input
|   ├── example_script.txt                      # Example script to run on
|   ├── test.txt                                # Another example script to run on
|   ├── this_file_will_get_ignored.notatxt      # A non-txt file example that will get ignored
├── output
|   ├── example_script.html                     # Example output from the script
|   ├── test.html                               # Another example output from the script
├── python_files
|   ├── __init__.py                             # File to control the flow of the program
|   ├── Converter.py                            # Handles all the logic for the script

## Python requirements
*Python will require these modules:*

```
No external modules required
```