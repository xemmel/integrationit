# AI-103 – Language, Vision & Information Extraction Cheat Sheet

## Azure Language
Specialized NLP service for analyzing text.

Can detect **sentiment**, extract **key phrases** and **named entities**, detect language, summarize text, etc.

Use when you need a well-defined NLP operation rather than general LLM reasoning.

---

## Generative AI / LLM
General-purpose language models can perform:

- Summarization
- Classification
- Information extraction
- Sentiment analysis
- Structured output

More flexible than Azure Language, but results are generative rather than a specialized API.

---

## Speech-to-Text Models
Generative models that convert **audio → text**.

Useful for transcription of recordings, meetings, conversations, etc.

---

## Text-to-Speech Models
Generate **spoken audio from text**.

Useful when an AI application needs to respond with speech.

---

## Azure Speech
Specialized Azure service for speech processing.

Supports:

- Speech-to-text
- Text-to-speech
- Voices
- Speech translation

Often used through the **Speech SDK**.

---

## Azure Speech MCP
Exposes Azure Speech functionality through an **MCP server**.

Allows an AI agent to use speech functionality as tools.

---

## Voice Live
Service/API for **real-time voice conversations with AI**.

Designed for low-latency conversational applications where users speak naturally with an AI agent.

---

## Azure Translator
Specialized service for translating **text between languages**.

Use when the primary requirement is reliable language translation.

---

## Speech Translation
Translates spoken language.

Example:

**Danish speech → English translation**

---

# Vision

## Multimodal / Vision Models
Generative AI models that can accept **images as input**.

They can:

- Describe images
- Answer questions about images
- Reason about visual information
- Extract information from images

Normally no custom image-model training is required.

---

## Image Generation Models
Generate new images from text prompts.

Example:

**Input:**  
`A red car driving through Copenhagen at night`

**Output:**  
A generated image.

---

## Sora
Generative **video model**.

Can generate video from text and/or visual input.

---

# Information Extraction

## Azure Content Understanding
Service for extracting **structured information from complex multimodal content**.

Works with:

- Documents
- Images
- Audio
- Video

You define the information/schema you want and an **analyzer** extracts structured results.

Useful for turning unstructured business content into data that applications and AI systems can use.

---

## Azure Document Intelligence
Specialized **document-processing service**.

Can extract:

- Text
- Layout
- Tables
- Key/value pairs
- Structured fields

Provides **prebuilt models** for common document types and supports **custom document models**.

Think:

**Invoices, receipts, forms, contracts and other business documents.**

---

## OCR – Optical Character Recognition
Extracts **text from images or scanned documents**.

Turns pixels containing written or printed text into machine-readable text.

OCR is commonly part of larger document and content-processing solutions.

---

# Azure AI Search

## Azure AI Search
Azure's **search, indexing and retrieval service**.

Used for:

- Traditional search
- Knowledge mining
- RAG

Can index large collections of documents and retrieve relevant information for users or AI models.

---

## AI Search Index
The searchable data structure containing documents and fields.

Applications query the **index** instead of searching the original data source directly.

---

## AI Search Indexer
Automatically retrieves content from supported data sources and populates or updates an **AI Search index**.

---

## AI Search Skillset
An **enrichment pipeline** executed during indexing.

Can perform operations such as:

- OCR
- Entity extraction
- Language detection
- Image analysis
- Chunking
- Custom processing

Turns raw source content into richer searchable information.

---

## AI Search Knowledge Store
Stores enriched information produced by an AI Search enrichment pipeline **outside the search index**.

Useful when enriched data needs to be consumed by other applications or analytics processes.

---

## Vector Search
Search using **embeddings** rather than exact words.

Finds content that is **semantically similar** to the query.

Very important for **RAG**.

---

## Hybrid Search
Combines:

**Keyword/full-text search + Vector search**

Often produces better retrieval results than using either technique alone.

---

## Semantic Ranking
Uses semantic understanding to improve the **ordering of search results**.

It reranks retrieved results so the most relevant results appear first.

---

# Quick Reference

| Service / Technology | Think |
|---|---|
| **Azure Language** | Analyze text |
| **Azure Speech** | Understand/generate speech |
| **Azure Translator** | Translate languages |
| **Voice Live** | Real-time voice conversation |
| **Multimodal models** | Understand images |
| **Image generation** | Create images |
| **Sora** | Create video |
| **Document Intelligence** | Extract text/layout/fields from documents |
| **Content Understanding** | Extract structured information from multimodal content |
| **Azure AI Search** | Index, enrich, search and retrieve information |
| **Vector Search** | Semantic retrieval using embeddings |
| **Hybrid Search** | Keyword + vector retrieval |
| **Semantic Ranking** | Improve ranking of retrieved results |