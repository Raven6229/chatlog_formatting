print("running parser")

my_script = "script"

try:
    in_script = open(my_script+".txt", "rt")
    print("Script found! Parasing...")
except:
    print("script not found: " + my_script)
out_script = open(my_script+"_out.txt", "wt")
out_script.write("")

def parse_script():
    # script must have two blank lines at the very end
    message = []
    script_new = []
    last_speaker = ""
    for line in in_script:
        speaker_end = line.find(":") # finds the end of the speaker by searching for :

        if speaker_end != -1: # runs if there is a :

            is_message = True
            for i in range(2): # checks if the code is a timebreak 
                if line[0:2] == "[" + str(i): # checks if the found line is a time stamp
                    print()
                    print("FOUND TIMESTAMP: " + line) 
                    is_message = False

            if is_message:
                speaker = line[0:speaker_end] # finds the speaker
                if speaker != last_speaker: # checks if it's a new speaker talking
                    message.append(speaker) # appends speaker
                    last_speaker = speaker # sets last speaker to avoid repeatedly labeling the speaker

                text = line[speaker_end + 1:] # adds message content
                text = text.replace("\n", "")
                message.append(text) # adds the newest message to the script

            else:
                line = line.replace("\n", "")
                timebreak_array = line.split("-")
                message = ["timestamp", timebreak_array[0]]
                if len(timebreak_array) > 1:
                    message.append(timebreak_array[1])
                last_speaker = ""
                script_new.append(message)
                message = []
                
        else: # why is this in an else statement
            if len(message) != 0: # checks if the message is empty. if not, add to script and empty
                script_new.append(message) 
            message = [] # but this is resetting the message

        
    return script_new


def format_script(pass_script):
    final_script = ""
    for s in pass_script:
        if s[0] != "timestamp":
            final_script += format_speaker(s)
        else:
            final_script += format_header(s[1:])
    out_script.write(final_script)


def format_speaker(msgs):

    # what in the cinnamon fresh fuck
    cmds = {
        "p_start": "<p>",
        "speaker_start": "<div class = \"speaker\">",

        "speaker_name_start": "<span class = \"",
        "speaker_name_start_close": "\">",
        "speaker_name_end": "</span>",

        "msg_start": "<div class = \"msg\">",
        "msg_end": "</div>",

        "speaker_end": "</div>",
        "p_end": "</p>",

    }

    

    msg = cmds["p_start"]+"\n"
    msg += cmds["speaker_start"]+"\n"

    speaker = msgs[0]

    speaker_code_name = speaker.lower()

    # comment this out when no longer needed to make wash blue
    if speaker == "Wash":
        speaker_code_name = "church"

    # makes lopez 2.0 use lopez formatting
    if speaker == "Lopez 2.0":
        speaker_code_name = "lopez"

    speaker_line = cmds["speaker_name_start"] + speaker_code_name + cmds["speaker_name_start_close"]
    speaker_line += speaker
    speaker_line += cmds["speaker_name_end"]

    msg += speaker_line+"\n"

    msgs = msgs[1:]

    for m in msgs:
        m = m.strip()
        msg += cmds["msg_start"]
        msg += m
        msg += cmds["msg_end"] + "\n"

    msg += cmds["speaker_end"] + "\n"
    msg += cmds["p_end"] + "\n\n"

    return msg

def format_header(header):
    # WASH'S WILL HAVE TO BE CHANGED TO GRAY HELMET.
    # CAN ADD YOUR OWN IMAGES HERE MANUALLY
    # BACKSLASHES ARE WEIRD, PAY CLOSE ATTENTION TO WHAT I DO HERE
    prof_icons = {
        "caboose" : "<img src=\"https://i.imgur.com/sktSAep.png\" alt=\"caboose\">",
		"wash" :	"<img src=\"https://i.imgur.com/s68cw9I.png\" alt=\"wash-blue\">",
        "washington" : "<img src=\"https://i.imgur.com/s68cw9I.png\" alt=\"wash-blue\">",
		"tucker" :	"<img src=\"https://i.imgur.com/zaOREey.png\" alt=\"tucker\">",
		"sarge" :	"<img src=\"https://i.imgur.com/ANc5oDR.png\" alt=\"sarge\">",
		"simmons" :	"<img src=\"https://i.imgur.com/gxY6pLJ.png\" alt=\"simmons\">",
		"grif" :	"<img src=\"https://i.imgur.com/JHQYumV.png\" alt=\"grif\">",
        "carolina" :    "<img src=\"https://i.imgur.com/xnaK8OT.png\" alt=\"carolina\">",
        "church" :   "<img src=\"https://i.imgur.com/66GMfaI.png\" alt=\"church\">",
        "epsilon" : "<img src=\"https://i.imgur.com/66GMfaI.png\" alt=\"church\">",
        "doc" :   "<img src=\"https://i.imgur.com/MXj9Kgg.png\" alt=\"doc\">",
        "dufresne" : "<img src=\"https://i.imgur.com/MXj9Kgg.png\" alt=\"doc\">",
        "donut" :   "<img src=\"https://i.imgur.com/NCvaKOl.png\" alt=\"donut\">"
    }

    msg = "<div class=\"skype-head\"><hr/>"

    if len(header) > 1: # if there are icons included, god help you
        
        if len(header[1]) > 2:
            header[1] = header[1][1:-1]
            speakers = header[1].split(" ")
            for speaker in speakers:
                try:
                    msg+=prof_icons[speaker.lower()]
                except:
                    pass
            msg+="<hr/>"
    
    msg += header[0] + "</div>"
    print(msg)
    return msg



#<div class="skype-head">
			#<hr/>
			#<p>[10:52]</p>
		#</div>
    



format_script(parse_script())

