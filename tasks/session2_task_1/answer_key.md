# Session 2 Task 1 — Answer Key

**Task ID:** session2_task_1  
**Maximum Score:** 600 points (550 seeded + 50 bonus)

---

## Seeded Bugs (5 total)

### Bug 1: Loose Equality Operator
- **Location:** Line 10
- **Severity:** High
- **Description:** Uses `==` instead of `===` for email comparison
- **Problem:** Allows type coercion, which can cause unexpected matches
- **Impact:** Could accidentally match non-string values that coerce to the admin email
- **Correct Fix:** `if (formData.email === "admin@example.com")`
- **Points:** 25 (find) + 25 (fix) = 50

### Bug 2: Null/Undefined Guard Missing
- **Location:** Line 14
- **Severity:** Critical
- **Description:** No null/undefined check before accessing `.length`
- **Problem:** If `formData.password` is null or undefined, accessing `.length` throws a TypeError
- **Impact:** Runtime crash if password field is missing
- **Correct Fix:** `if (!formData.password || formData.password.length < 8)`
- **Points:** 75 (find) + 75 (fix) = 150

### Bug 3: Regex Missing Case-Insensitive Flag
- **Location:** Line 18
- **Severity:** High
- **Description:** Email regex pattern lacks the `i` flag for case-insensitive matching
- **Problem:** Pattern matches only lowercase emails; rejects valid emails with uppercase letters
- **Impact:** Valid emails like "John@Example.com" are rejected
- **Correct Fix:** `/^[a-z0-9+_.-]+@[a-z0-9.-]+\.[a-z]{2,}$/i` (add `i` at end)
- **Points:** 50 (find) + 50 (fix) = 100

### Bug 4: Array Method Confusion (.includes vs .some)
- **Location:** Line 22
- **Severity:** High
- **Description:** Uses `.includes()` with an array argument; should use `.some()` or regex
- **Problem:** `.includes()` checks if the string includes the array object itself, not the characters in the array
- **Impact:** Always returns false; special character warning never triggers
- **Correct Fix Option A:** `formData.password.split('').some(char => ["!","@","#","$","%"].includes(char))`
- **Correct Fix Option B:** `/[!@#$%]/.test(formData.password)`
- **Points:** 50 (find) + 50 (fix) = 100

### Bug 5: Swapped Age Logic
- **Location:** Line 26
- **Severity:** Critical
- **Description:** Age check logic is backwards; uses `> 18` when it should use `< 18`
- **Problem:** Rejects users 18 and older; allows minors
- **Impact:** Adult users are blocked; minors pass validation
- **Correct Fix:** `if (formData.age < 18)` (change `>` to `<`)
- **Points:** 75 (find) + 75 (fix) = 150

---

## Bonus Points (up to 50 total)

### Bonus 1: Semantic Issue (up to +25)
**Award if participant flags:**
- Timestamp ambiguity: `new Date().getTime()` returns milliseconds, not seconds
- If backend expects seconds, this will cause timestamp calculation errors
- Suggestion to use `Math.floor(Date.now() / 1000)` or document the millisecond assumption

### Bonus 2: Test Case Design (up to +25)
**Award if participant proposes:**
- Test cases for null/undefined password
- Test case for uppercase email
- Test case for password without special characters
- Test case for boundary condition (age exactly 18)
- Any systematic approach to catching the bugs

---

## Scoring Summary

| Bug | Find | Fix | Total |
|-----|------|-----|-------|
| 1 (==) | 25 | 25 | 50 |
| 2 (null guard) | 75 | 75 | 150 |
| 3 (regex flag) | 50 | 50 | 100 |
| 4 (.includes) | 50 | 50 | 100 |
| 5 (age logic) | 75 | 75 | 150 |
| **Subtotal** | | | **550** |
| Bonus (semantic + test cases) | | | **+50** |
| **Maximum** | | | **600** |

---

**Answer Key Prepared:** Claude Haiku 4.5  
**Date:** Day 405, May 11, 2026
