import os
from mssql_python import connect

def query_sql(query: str) -> list[dict[str, object]]:
    print(f"Sql command to execute: {query}")
    conn = connect(os.environ["SQL_CONNECTION_STRING"])

    cursor = conn.cursor()
    cursor.execute(query)

    if cursor.description:
        columns = [col[0] for col in cursor.description]

        rows = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

        conn.close()
        return rows

    conn.commit()
    conn.close()
    return []


local_function_tools = [
    {
        "type" : "function",
        "name" : "query_sql",
        "description" : """
            executes sql commands and return result set (if any) with python: list[dict[str,object]]
            -------------------------
            ONLY selects
            -------------------------
            This is an Azure SQL Database (MS Sql Server)
        """,
        "parameters" : {
            "type" : "object",
            "properties" : {
                "query" : {
                    "type" : "string",
                    "description" : "The sql command to execute"
                }
            },
            "required" : [ "query" ],
            "additionalProperties" : False
        }
    }
]