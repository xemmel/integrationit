import os
from pathlib import Path


def get_file_content(fileName: str) -> str:
    fullName = Path("file_outputs") / fileName
    return fullName.read_text(encoding="utf-8")

def list_files() -> list[str]:
    folder = Path("file_outputs")
    return [file.name for file in folder.iterdir() if file.is_file()]

def save_file(fileName: str, content: str) -> str:
    fullName = Path("file_outputs") / fileName
    fullName.write_text(content, encoding="utf-8")
    return f"File saved {fullName}"

common_file_tools = [
    {
        "type" : "function",
        "name" : "get_file_content",
        "description" : """
        Get file content 
        -------------
        returns the content as a string
        """,
        "parameters" : {
            "type" : "object",
            "properties" : {
                "fileName" : {
                    "type" : "string",
                    "description" : """
                    The filename of the file to get the content from
                    """
                }
            },
            "required" : [ "fileName" ],
            "additionalProperties" : False
        }
    },
        {
        "type" : "function",
        "name" : "list_files",
        "description" : """
        List all files available
        -------------
        returns a list[str] of filenames
        """,
        "parameters" : {
            "type" : "object",
            "properties" : {},
            "required" : [ ],
            "additionalProperties" : False
        }
    },
    {
        "type" : "function",
        "name" : "save_file",
        "description" : "Save content to a file.",
        "parameters" : {
            "type" : "object",
            "properties" : {
                "fileName" : {
                    "type" : "string",
                    "description" : """
                        The filename of the file to be created
                        ------------
                        returns a string with the filename Created
                    """
                },
                "content" : {
                    "type" : "string",
                    "description" : """
                        The content of the file to be created
                    """
                }
            },
            "required" : [ "fileName", "content" ],
            "additionalProperties" : False
        }
    }
]

