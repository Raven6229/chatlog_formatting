import logging
import re

TIMESTAMP_REGEX = r"\[(([0-9]|0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])(:([0-5][0-9]))?([ ]?[AaPp][Mm])?)\](.*)"
MESSAGE_REGEX = r"([A-Za-z0-9]*): (.*)"


def parseScript(cwd: str, script_name: str) -> list:
    """
    Parameters:
        cwd (str): The Current Working Directory (os.getcwd())
        script_name (str): The filename of the script to parse, excluding path and file format
    """
    logger = logging.getLogger("converter.parser")
    logger.info(f"Parsing script '{script_name}'")
    parsed_script = []

    with open(cwd + f"/input/{script_name}.txt", "r") as file:
        current_speaker = None
        for line in file.readlines():
            line = line.strip()

            match_message = re.search(MESSAGE_REGEX, line)
            match_timestamp = re.findall(TIMESTAMP_REGEX, line)

            # Check if the line is a message
            if match_message:
                current_speaker = match_message.group(1)
                message = match_message.group(2)
                parsed_script.append(
                    {"type": "message", "author": current_speaker, "message": message}
                )

                logger.debug(f"{current_speaker}: {message}")

            # Check if the line is a timestamp
            elif match_timestamp:
                # Convert out of tuple list
                for match in match_timestamp:
                    current_timestamp = match[0]
                    timestamp_message = match[-1]

                parsed_script.append(
                    {
                        "type": "timestamp",
                        "timestamp": current_timestamp,
                        "message": timestamp_message,
                    }
                )

                logger.debug(f"Timestamp {current_timestamp}: {timestamp_message}")

            # If the line has content but doesn't have a defined message, default to the current speaker
            elif line != "":
                parsed_script.append(
                    {"type": "message", "author": current_speaker, "message": line}
                )

                logger.debug(f"UNKNOWN AUTHOR: {line}")

    logger.info(f"Script '{script_name}' parsed.")
    return parsed_script


def htmlSetup(cwd: str, title: str) -> str:
    """
    Default header setup stuff
    Parameters:
        cwd (str): The Current Working Directory (os.getcwd())
        title (str): The title of the HTML page
    """
    setup = f"""<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t<title>{title}</title>\n\t<link href="{cwd + '/config/skin.css'}" rel="stylesheet" type="text/css">\n\n</head>\n<body>\n\t<div class="skype">\n"""
    return setup


def htmlEnd() -> str:
    """
    Ending html tags
    """
    end = "\t</div>\n</body>\n</html>"
    return end


def icons(config: dict, authors: set) -> str:
    """
    Generate the icon strings based on the input authors
    Parameters:
        config (dict): Config dict matching author name to an image and alt
        authors (set): Set of authors to draw icons for
    """
    logger = logging.getLogger("converter.icons")
    return_string = '\t\t<hr/><div class="skype-head">'
    for author in authors:
        if config.get("icons", {}).get(author.lower(), {}).get("image", None):
            return_string += f'<img src={config["icons"][author.lower()]["image"]} alt={config["icons"][author.lower()]["alt"]}>'
        else:
            logger.debug(f"No matching icon in config for {author.lower()}")
    return_string += "</div>\n"
    return return_string


def generateHTML(cwd: str, config: dict, script_name: str, script: list[dict]) -> None:
    """
    Generates the HTML file based on the parsed script
    Parameters:
        cwd (str): The Current Working Directory (os.getcwd())
        config (dict): Config file matching author name to an image and alt
        script_name (str): The name of the output script without path or file format
        script (list[dict]): The parsed script in the form of a dictionary.
    """
    logger = logging.getLogger("converter.generate")
    logger.info(f"Generating '{script_name}' Output File")

    timestamp_output = ""
    header_output = []
    script_output = []
    authors = set()
    current_author = ""

    for line in script:
        logger.debug(line)

        # Reset all vars on every new timestamp
        if line.get("type", None) == "timestamp":
            # If there was actually information, append to the headers and add the ending tags
            if len(authors) != 0:
                timestamp_output += f"\t\t\t\t</div>\n\t\t\t</p>\n"
            script_output.append(f"{timestamp_output}")
            header_output.append(authors)
            authors = set()
            timestamp_output = ""
            timestamp_output += (
                f'\t\t<hr/><div class="skype-head">{line.get("timestamp", "")}</div>\n'
            )

        else:
            if current_author != line.get("author", ""):
                current_author = line.get("author", "")
                if len(authors) == 0:
                    timestamp_output += f'\t\t<p>\n\t\t\t<div class="speaker">\n\t\t\t\t<span class = "{current_author.lower()}">{current_author}</span>\n'
                else:
                    timestamp_output += f"\t\t\t</div>\n\t\t</p>\n"
                    timestamp_output += f'\t\t<p>\n\t\t\t<div class="speaker">\n\t\t\t\t<span class = "{current_author.lower()}">{current_author}</span>\n'

                authors.add(current_author)

            timestamp_output += (
                f'\t\t\t\t<div class="msg">{line.get("message", "")}</div>\n'
            )

    # Ensure the final timestamp information still gets put in
    header_output.append(authors)
    script_output.append(f"{timestamp_output}\t\t\t</div>\n\t\t</p>\n")

    with open(cwd + f"/output/{script_name}.html", "w") as f:
        f.write(htmlSetup(cwd=cwd, title=script_name))
        for count in range(len(script_output)):
            if header_output[count]:
                f.write(icons(config=config, authors=header_output[count]))
            f.write(script_output[count])
        f.write(htmlEnd())

    logger.info(f"'{script_name}' Output file generated.")
