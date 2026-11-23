# Invoice Review

A hybrid invoice and receipt documents review application built with **Azure AI Document Intelligence, Azure OpenAI, FastAPI**.

## Overview

Automates document extraction, validates financial information against company policies, and supports human-led invoice and receipt approvals.

## Key Features

- Upload PDF and image documents (up to 4 MB).
- Automatically classify invoices and receipts.
- Extract supplier, customer, dates, purchase orders, totals, and line items.
- Apply deterministic invoice and receipt policies.
- Detect duplicate documents.
- Edit extracted information and approve or reject documents.

## Architecture

1. **Document Upload:** The reviewer uploads an invoice or receipt through the React interface.
2. **Document Extraction:** Azure AI Document Intelligence extracts structured information and confidence scores.
3. **AI Assistance:** Azure OpenAI supports document classification, missing-field extraction.
4. **Validation:** Python-based deterministic rules validate VAT numbers, financial totals, duplicates, and company policies.
5. **Human Review:** The reviewer examines extracted information and validation results before making the final decision.
6. **Persistence:** FastAPI stores review records and history in SQLite.

