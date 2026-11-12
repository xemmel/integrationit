from fastapi import FastAPI

app = FastAPI()


@app.get("/version",description="Gives you the current version of the openapi")
def get_version():
    return { "version" : "1.10" }

@app.get("/funnyquote",description="Gives you a funny quote. Answer is in JSON ")
def get_version():
    return { "answer" : "This is funny.....Kitten...." }


@app.get("/customers",description="List all customers in json { ""name"" : ""customer1"", ""priority"" : 1 }")
def get_version() -> dict:
    return [
        {
        "name" : "Contoso",
        "priority" : 2
        },
        {
        "name" : "IBM",
        "priority" : 5
        },
    ]

