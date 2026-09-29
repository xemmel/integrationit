import uuid

def create_support_case(emp_id: str) -> str:
    case_id = str(uuid.uuid4())
    print(f"-- create_support_case executed with case_id: {case_id} for emp_id: {emp_id}")    
    return case_id

def update_support_case(case_id: str, content: str) -> str:
    print(f"-- update_support_case executed with case_id: {case_id} content: '{content}'")
    return "updated"

support_tools = [
       {
                "type" : "function",
                "name" : "create_support_case",
                "description" : """
                    Creates a support case for an employee
                    -------------------
                    Outputs: the newly created support case unique id
                """,
                "parameters" : {
                    "type" : "object",
                    "properties" : {
                        "emp_id" : {
                                "type" : "string",
                                "description" : "The employee id. Format: [0-9]{4}"
                            }
                    },
                    "required" : [ "emp_id" ],
                    "additionalProperties" : False
                }
            },
            {
                        "type" : "function",
                        "name" : "update_support_case",
                        "description" : """
                            Update an existing support case for an employee
                            -------------------
                            Outputs: updated as string
                        """,
                        "parameters" : {
                            "type" : "object",
                            "properties" : {
                                "case_id" : {
                                        "type" : "string",
                                        "description" : "The support case id"
                                    },
                                "content" : {
                                        "type" : "string",
                                        "description" : "The content to be appended to the support text"
                                    }
                            },
                            "required" : [ "case_id", "content" ],
                            "additionalProperties" : False
                        }
                    }
]