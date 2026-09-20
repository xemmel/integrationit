import uuid
import requests

url = "https://thenewappapphello-frontapp.kindpebble-8ed0ec78.germanywestcentral.azurecontainerapps.io/documents"


def create_support_case(employee_id: str) -> str:
    case_id = str(uuid.uuid4())
    response = requests.post(
            url,
            data=f"Support case: {case_id} created for user: {employee_id}",
            headers={"Content-Type": "text/plain"}
        )
    print(f"Creating support case with id: {case_id}")
    return case_id

def insert_support_case_text(case_id: str, text: str) -> str:

    response = requests.post(
    url,
    data=f"Support case: {case_id}\n{text}",
    headers={"Content-Type": "text/plain"}
)

    print(f"Adding text to support case: {case_id}")
    print(text)
    return "text inserted"

def close_support_case(case_id: str) -> str:
    return f"case: {case_id} closed"

common_supportcase_tools = [
    {
        "type" : "function",
        "name" : "create_support_case",
        "description": """
            Creates a new empty support case for the employee.

            IMPORTANT: This function creates an EMPTY support case.
            It does NOT store the user's problem description.

            If the user supplied a problem description, after this function
            returns a case_id you MUST call insert_support_case_text using:
            - the returned case_id
            - the user's original problem description exactly as supplied

            The support case creation task is NOT complete until the problem
            description has been inserted.
        """,
        "parameters" : {
            "type" : "object",
            "properties" : {
                "employee_id" : {
                    "type" : "string",
                    "description" : """
                    The employee id of the employee with a support case.
                    -----------
                    format: [0-9]{4}
                    -----------
                    The employee MUST supply the id themself
                    -----------
                    returns: a uuid4 unique id for the newly created support case
                    """
                }
            },
            "required" : [ "employee_id" ],
            "additionalProperties" : False
        }
    },
    {
        "type" : "function",
        "name" : "insert_support_case_text",
        "description" : """
            Inserts/Append text into an existing support case
        """,
        "parameters" : {
            "type" : "object",
            "properties" : {
                "case_id" : {
                    "type" : "string",
                    "description" : """
                       the unique support case id
                    """
                },
                "text" : {
                    "type" : "string",
                    "description" : """
                    The content of the text needed to be added to the support case
                    ---------------
                    Do not correct if misspelled
                    """
                }
            },
            "required" : [ "case_id", "text" ],
            "additionalProperties" : False
             
        }
    }
]