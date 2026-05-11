# Task 4: Distributed Order Processing System — Code Review

## Instructions

You are reviewing a 3-file Node.js module for an e-commerce order processing system. The system has three components:

1. **`inventory.js`** — Stock management with reservations
2. **`pricing.js`** — Discount engine with stacking rules and surge pricing
3. **`order.js`** — Order pipeline that orchestrates inventory and pricing

Your task is to:
1. **Identify all bugs** in the codebase
2. **Classify each bug** by severity (CRITICAL / MEDIUM / LOW)
3. **Explain the impact** of each bug, including how it affects the system behavior
4. **Propose a fix** for each bug
5. **Identify any cross-file interaction effects** where bugs in one file affect behavior in another

## Scoring Rubric (800 points max)

- **Bug identification:** Points per bug based on difficulty tier (see answer key for details)
- **Fix quality:** Must be correct and not introduce new issues
- **Cross-file interaction analysis bonus:** Up to 50 points for documenting how bugs across files interact
- **Comprehensive test cases bonus:** Up to 50 points for providing test cases that demonstrate bugs
- **False positive penalty:** -25 points for each incorrectly reported "bug" that isn't actually a bug

## Key Specification Notes

- **Discount stacking rule:** "Apply flat discounts FIRST, then percentage discounts on the reduced amount."
- **Inventory reservations** are all-or-nothing: if any item can't be reserved, no items are reserved
- **Financial calculations** should be rounded to 2 decimal places (cents)
- **Order validation** should ensure ALL items are valid before proceeding
- The system should handle concurrent order requests safely

## Anti-Contamination Declaration

Before starting, please confirm:
- [ ] I have not previously seen these files or any answer key
- [ ] I am working under my assigned condition (Solo / Unstructured / Structured)

## Deliverable

Submit a markdown file with your bug report following the format in the run template.

---

**Time limit:** None (but please record your start and end time)
**Files to review:** `inventory.js`, `pricing.js`, `order.js` (this file, `spec.md`, is for reference only)
