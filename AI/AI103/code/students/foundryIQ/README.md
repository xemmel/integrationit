## In client/agent

```python

from azure.ai.projects.models import (
    PromptAgentDefinition,
    FileSearchTool
)

file_search = FileSearchTool(
    vector_store_ids=[vector_store.id]
)

```