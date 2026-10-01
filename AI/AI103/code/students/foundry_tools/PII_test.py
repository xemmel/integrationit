import os
import argparse

from azure.identity import DefaultAzureCredential
from azure.ai.textanalytics import TextAnalyticsClient

parser = argparse.ArgumentParser()
parser.add_argument("--text", required=True)
args = parser.parse_args()

client = TextAnalyticsClient(
    endpoint=os.environ["FOUNDRY_TOOLS_ENDPOINT"],
    credential=DefaultAzureCredential()
)

result = client.recognize_pii_entities(
    [args.text],
    language="en"
)[0]

print("Redacted:")
print(result.redacted_text)

print("\nDetected PII:")
for entity in result.entities:
    print(
        f"{entity.text} -> {entity.category} "
        f"({entity.confidence_score:.2f})"
    )