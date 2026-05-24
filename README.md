# Agentic Invoice Skill

A CompleteTech LLC Codex skill for creating invoice drafts and billing documents for agentic development engagements.

## What It Does

- Selects the right invoice by billing event.
- Drafts invoices, pro formas, deposits, milestone invoices, change-order invoices, retainers, pass-through invoices, credit memos, refund memos, receipts, and closeout billing.
- Keeps line items aligned with practical agentic development work: workflow discovery, pilot implementation, evaluation, approval gates, monitoring, documentation, handoff, support, and expansion.
- Includes a near-exhaustive invoice catalog for the full billing lifecycle.

## Contents

- `SKILL.md` - operating instructions and invoice-selection guide.
- `references/invoice-catalog.md` - 36 reusable invoice and billing-document templates.
- `references/use-case-decision-table.md` - quick guide for choosing the right invoice.
- `references/invoice-lifecycle.md` - end-to-end billing workflow and approval gates.
- `references/invoice-positioning.md` - CompleteTech LLC invoice language and guardrails.
- `scripts/render_invoice.py` - deterministic template listing and rendering helper.

## Quick Start

```bash
python3 scripts/render_invoice.py --list
python3 scripts/render_invoice.py \
  --template pilot-deposit-invoice \
  --var invoice_number=INV-1001 \
  --var issue_date=2026-05-24 \
  --var due_date=2026-06-08 \
  --var contract_id=ADSA-DEMO-0001 \
  --var workflow="support triage" \
  --var amount_due="USD 6,000"
```

Rendered templates are drafts. Replace placeholders with verified client, contract, tax, payment, and accounting details before use.

## Brand Notes

Use clear, specific, auditable line items. Separate professional services, pass-through costs, expenses, taxes, credits, and late fees. Do not invent tax IDs, banking details, tax rates, purchase orders, contract terms, or legal/accounting conclusions.
