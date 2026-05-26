---
name: agentic-invoice-skill
description: >-
  Generate branded invoice and billing-document PDFs for agentic development services, including deposits, milestones, retainers, change orders, pass-through expenses, credits, receipts, refunds, and closeout billing. Use when the user wants structured billing documents from verified contract, SOW, milestone, and payment facts.
version: 1.0.3
metadata:
  openclaw:
    skillKey: agentic-invoice-skill
    homepage: https://github.com/CompleteTech-LLC/agentic-invoice-skill
    requires:
      bins:
        - python3
    install:
      - kind: uv
        package: reportlab==4.5.1
      - kind: uv
        package: pyyaml==6.0.3
      - kind: uv
        package: pypdfium2==5.8.0
      - kind: uv
        package: pillow==12.2.0
---

# Agentic Invoice Skill

## At a Glance

| What it creates | Best for | Output |
|---|---|---|
| Invoices and billing documents | Deposits, milestones, retainers, support, change orders, credits, receipts, refunds, and closeout | Branded PDF, Markdown, optional PNG preview |

This skill turns verified billing events, line items, contract references, credits, payment terms, and approval facts into clean CompleteTech-style invoice artifacts. It is local-only: it creates documents and does not issue invoices, collect payment, or call accounting systems.

## Included Billing Documents

- Pro forma, deposit, pilot, discovery, milestone, prototype, final balance, and time-and-materials invoices.
- Retainer, recurring support, overage, expansion, training, advisory, and pass-through invoices.
- Credit memos, refund memos, corrected invoices, void notices, installment requests, and paid-in-full receipts.

## Purpose

Create practical invoice documents for agentic development services end to end: upfront deposits, scoped pilots, discovery, implementation, evaluation, change orders, retainers, support, expenses, credits, late fees, refunds, and closeout.

## System Boundary

This skill owns billing document drafting and invoice-event selection. Use `agentic-proposal-skill` for pricing rationale or commercial scope before approval, `agentic-contract-skill` for agreement terms, `agentic-delivery-skill` for milestone evidence, `agentic-email-skill` for the message that sends an invoice, and an accounting system or human reviewer for final tax, payment, ledger, and collection decisions.

## Core Workflow

1. Identify the invoice event: estimate, deposit, milestone, monthly retainer, time and materials, change order, expense, final invoice, credit, late fee, refund, or renewal.
2. Gather required facts: provider, client, invoice number, issue date, due date, terms, currency, contract or SOW reference, project name, billing period, line items, taxes, discounts, credits, previous payments, payment instructions, and notes.
3. Use `references/invoice-positioning.md` for service language and risk boundaries.
4. Use `references/use-case-decision-table.md` to choose the right invoice type.
5. Use `references/invoice-lifecycle.md` for end-to-end billing flow and gates.
6. Use `references/invoice-catalog.md` for the near-exhaustive invoice template library.
7. Draft clearly and conservatively. Do not invent tax IDs, banking details, tax rates, contract terms, or legal/accounting claims.

## Invoice Selection Guide

Choose by billing event:

- Before signed agreement or purchase order: use `pro-forma-invoice` or `deposit-request-invoice`.
- Fixed-scope pilot deposit: use `pilot-deposit-invoice`.
- Workflow assessment only: use `discovery-assessment-invoice`.
- Contract signing deposit: use `contract-deposit-invoice`.
- Milestone reached: use `milestone-invoice`.
- Prototype delivered: use `prototype-delivery-invoice`.
- Evaluation or test-set work delivered: use `evaluation-work-invoice`.
- Documentation and handoff complete: use `handoff-invoice`.
- Final balance due: use `final-balance-invoice`.
- Hourly work: use `time-and-materials-invoice`.
- Monthly support or managed monitoring: use `monthly-retainer-invoice`.
- Recurring agent operations support: use `recurring-support-invoice`.
- Additional scope after agreement: use `change-order-invoice`.
- Rush work: use `rush-fee-invoice`.
- Added integration or tool connector: use `integration-add-on-invoice`.
- API, model, hosting, storage, or third-party pass-through charges: use `usage-pass-through-invoice`.
- Travel, printing, procurement, or reimbursable costs: use `expense-reimbursement-invoice`.
- Support hours exceeded: use `support-overage-invoice`.
- Late payment fee or finance charge: use `late-fee-invoice`.
- Payment plan installment: use `installment-invoice`.
- Partial payment received: use `partial-payment-receipt-invoice`.
- Client prepayment or credit balance: use `prepayment-credit-invoice`.
- Discount or courtesy reduction: use `discount-adjustment-invoice`.
- Correcting a prior invoice: use `corrected-invoice`.
- Cancelled project with earned work: use `termination-invoice`.
- Refund owed: use `refund-memo`.
- Credit owed against future work: use `credit-memo`.
- Retainer renewal: use `retainer-renewal-invoice`.
- Expansion to a second workflow: use `expansion-workflow-invoice`.
- Training or enablement: use `training-invoice`.
- Advisory-only work: use `advisory-invoice`.
- Acceptance holdback release: use `holdback-release-invoice`.
- Tax-only adjustment: use `tax-only-invoice`.
- Voiding a prior invoice: use `voided-invoice-notice`.
- Confirming full payment: use `paid-in-full-receipt`.

When several templates fit, choose the invoice closest to the actual commercial trigger. For example, if a prototype was delivered but the contract bills only on milestone acceptance, use `milestone-invoice`, not `prototype-delivery-invoice`.

## Quality Rules

- Use exact client-provided amounts and terms.
- Keep line items specific enough for approval but not cluttered.
- Tie invoices to contract, SOW, change order, or accepted milestone references when available.
- Separate professional services, third-party pass-throughs, expenses, taxes, credits, and late fees.
- Mark drafts as drafts if payment details or tax handling are unknown.
- Do not put legal, tax, or accounting advice on invoices unless the user specifically asks for explanatory notes.
- Never fabricate bank accounts, tax IDs, purchase order numbers, tax rates, or compliance status.

## Resource Guide

- `references/invoice-positioning.md`: load for agentic development service wording, line-item language, and boundaries.
- `references/use-case-decision-table.md`: load when choosing which invoice to use.
- `references/invoice-lifecycle.md`: load for end-to-end invoicing workflows, approval gates, and follow-up steps.
- `references/invoice-catalog.md`: load for the near-exhaustive invoice template library.
- `references/template-index.json`: machine-readable template metadata used by the renderer.
- `scripts/render_invoice.py`: list invoice templates or render a draft with placeholders.

## Runtime Permissions

This skill is a local document-rendering workflow. It reads bundled templates, references, examples, `assets/logo.png`, and user-provided Markdown or invoice variables. It writes only the user-selected `--out`, `--png`, `--markdown-out`, or default `output/` artifact paths. It runs local Python entry points for `scripts/render_invoice.py` and `scripts/render_pdf.py`.

It does not require network access, credential access, persistence, privilege escalation, destructive file operations, or background services.

## Renderer

Use the renderer for repeatable invoice drafts or template discovery:

```bash
python3 scripts/render_invoice.py --list
python3 scripts/render_invoice.py --stage milestone --list
python3 scripts/render_invoice.py --template pilot-deposit-invoice --var client_name=Acme --var invoice_number=INV-1001 --var amount_due=6000
```

If a user needs a polished production invoice, use the rendered draft as a starting point and replace every placeholder with verified facts.

## Rendering to a Branded PDF

Artifacts from this skill are delivered as branded CompleteTech LLC **PDF** documents, not raw Markdown. The renderer emits the PDF (and prints the Markdown) in **one command**, using the same reportlab branding engine as the contract skill:

```bash
pip install -r requirements.txt
python3 scripts/render_invoice.py --template milestone-invoice \
  --out artifact.pdf --png artifact.png \
  --title "Invoice INV-2026-0461" --doc-type "MILESTONE INVOICE" \
  --meta "INVOICE NO.=INV-2026-0461" --meta "DUE=2026-06-23" --no-cover \
  --var client_name="Client Name" --var workflow="support triage"
```

- `--no-pdf` emits Markdown only (the original behavior); `--no-cover` drops the cover page.
- Already drafted the Markdown yourself? Render it directly: `python3 scripts/render_pdf.py --markdown artifact.md --out artifact.pdf --logo assets/logo.png --title "..."`.
- The PDF supports a Markdown subset: `#`/`##`/`###` headings, paragraphs, `-` bullets, tables, `>` callouts, `**bold**`, and `[PAGE_BREAK]`. PDF requires `reportlab==4.5.1`; the optional `--png` preview requires `pypdfium2==5.8.0` and `pillow==12.2.0`. See `assets/examples/` for a rendered example.

## Network Boundary

This skill is local-only. It does not include outbound network helpers, callbacks, or any helper that posts invoice run metadata to an external service.
