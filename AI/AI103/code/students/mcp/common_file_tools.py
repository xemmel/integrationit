from pathlib import Path

def create_file(fileName: str, content: str) -> str:
    ## Implement create local file logic
    folder = Path("sandbox")
    folder.mkdir(parents=True, exist_ok=True)
    
    fullName = Path("sandbox") / fileName
    fullName.write_text(content,encoding="utf-8")
    print(f"-- create_file executed with fileName: {fileName}")
    return "success"

file_tools = [
     {
            "type" : "function",
            "name" : "create_file",
            "description" : """
                Creates a local file
                -------------------
                Outputs: status (success/failed)
            """,
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "fileName" : {
                        "type" : "string",
                        "description" : "The name of the file"
                    },
                    "content" : {
                        "type": "string",
                        "description" : "The file content"
                    }
                },
                "required" : [ "fileName", "content"],
                "additionalProperties" : False
            }
        }
]

file_functions = {
    tool["name"]: globals()[tool["name"]]
    for tool in file_tools
}