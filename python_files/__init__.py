import logging

from python_files import Converter


def run(cwd: str, config: dict, scripts_for_formatting: list):
    logger = logging.getLogger("chatlog_formatter")
    logger.info(f"Hello Chat Log Formatter")

    for script_name in scripts_for_formatting:
        parsed_script = Converter.parseScript(cwd=cwd, script_name=script_name)
        Converter.generateHTML(
            cwd=cwd, config=config, script_name=script_name, script=parsed_script
        )

    # Cleaning up
    logger.info(f"Goodbye Chat Log Formatter")
