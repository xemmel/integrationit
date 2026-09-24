FROM python:3.14-slim

WORKDIR /app

COPY mcp_requirements.txt .
RUN pip install --no-cache-dir -r mcp_requirements.txt

COPY mcp_server.py .

EXPOSE 8000

CMD [ "python", "mcp_server.py" ]
