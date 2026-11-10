from uuid import uuid4

def create_file(file_name: str, content: str):
    print(f"Creating file: {file_name}")
    with open(file_name, "w") as f:
        f.write(content)
    return f"File: {file_name} created"

def create_support_case(employee_id: str):
    support_case_id = str(uuid4())
    print(f"Creating support case: {support_case_id} for emp: {employee_id}")
    return f"Support case {support_case_id} created"

def update_support_case(support_case_id: str,content: str):
    print(f"Updating support case: {support_case_id}. Content_: {content}")
    return f"Support case {support_case_id} updated"

create_file_tool = {
    "type" : "function",
    "name" : "create_file",
    "description" : """
    A method for creating files locally
    ----------
    outputs: File {file_name} created
""",
   "parameters" : {
       "type" : "object",
       "properties" : {
           "file_name" : {
               "type" : "string",
               "description" : "The name of the file"
           },
           "content" : {
               "type" : "string",
               "description" : "The file content to be inserted into the created file"
           }
       },
       "required" : [ "file_name", "content" ]
   }
}

create_support_case_tool = {
    "type" : "function",
    "name" : "create_support_case",
    "description" : """
    A method for creating a new support case
    ----------
    outputs: The unique id for the newly created case
""",
   "parameters" : {
       "type" : "object",
       "properties" : {
           "employee_id" : {
               "type" : "string",
               "description" : "The id of the employee making the support case, MUST be [0-9]{4}. The employees are idiots so give them a proper sample of what an id looks like if they dont supply it. The example must be 5454"
           }
       },
       "required" : [ "employee_id" ]
   }
}

update_support_case_tool = {
    "type" : "function",
    "name" : "update_support_case",
    "description" : """
    Updates an existing support case with information
    ----------
    outputs: support case {support_case_id} updated
""",
   "parameters" : {
       "type" : "object",
       "properties" : {
           "support_case_id" : {
               "type" : "string",
               "description" : "The id of the support case"
           },
           "content" : {
               "type" : "string",
               "description" : "The text of what the support issue is about"
           }
       },
       "required" : [ "support_case_id", "content" ]
   }
}