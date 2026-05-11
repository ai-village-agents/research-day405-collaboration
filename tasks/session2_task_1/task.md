# Session 2, Task 1: validateUserInput function

**Task Family:** JavaScript bug inspection and correction  
**Task ID:** session2_task_1  
**Difficulty:** Medium (5 seeded issues)  
**Time Estimate:** 15–20 minutes per condition  

---

## Background

You are reviewing a JavaScript utility function `validateUserInput()` that validates and transforms user input for a web form. The function has 5 intentional bugs (seeded for research purposes).

---

## Code Under Review

```javascript
// validateUserInput.js
// Validates and transforms user input from a web form

function validateUserInput(formData) {
  const errors = [];
  const warnings = [];
  
  // Bug 1: String comparison with wrong operator
  if (formData.email == "admin@example.com") {
    errors.push("Admin email cannot be used");
  }
  
  // Bug 2: Length check on undefined
  if (formData.password.length < 8) {
    errors.push("Password must be at least 8 characters");
  }
  
  // Bug 3: Regex missing flag
  const emailRegex = /^[a-z0-9+_.-]+@[a-z0-9.-]+\.[a-z]{2,}$/;
  if (!emailRegex.test(formData.email)) {
    errors.push("Invalid email format");
  }
  
  // Bug 4: Wrong array method
  const hasSpecialChar = formData.password.includes(["!","@","#","$","%"]);
  if (!hasSpecialChar) {
    warnings.push("Password should include special characters");
  }
  
  // Bug 5: Logic error - swapped condition
  if (formData.age > 18) {
    errors.push("User must be 18 or older");
  }
  
  return {
    isValid: errors.length === 0,
    errors: errors,
    warnings: warnings,
    timestamp: new Date().getTime()
  };
}

module.exports = validateUserInput;
```

---

## Instructions

### Your Task
1. **Identify all seeded bugs** in the code above.
2. **Propose fixes** for each bug.
3. **Rate severity** (Critical / High / Medium / Low).
4. **Optionally:** identify any semantic issues, edge cases, or test cases that would catch these bugs.

### Output Format
Provide your analysis in the following structure:

```
# Bug Analysis

## Bug 1: [Bug Name]
- **Location:** [Line number]
- **Severity:** [Critical / High / Medium / Low]
- **Problem:** [What is wrong?]
- **Impact:** [What breaks?]
- **Fix:** [Proposed correction]

...

## Additional Observations
[Any bonus insights, edge cases, test ideas, or semantic issues]
```

---

## Answer Key (For Scoring Only)

Do not read this section during the analysis.

### Bug 1: Loose equality operator
- **Location:** Line 10
- **Severity:** High
- **Problem:** Uses `==` instead of `===`
- **Fix:** Change to `===`

### Bug 2: Null/undefined check missing
- **Location:** Line 14
- **Severity:** Critical
- **Problem:** No guard against `formData.password` being null/undefined
- **Fix:** Add guard: `if (!formData.password || formData.password.length < 8)`

### Bug 3: Regex missing case-insensitive flag
- **Location:** Line 18
- **Severity:** High
- **Problem:** Regex only matches lowercase; missing `i` flag
- **Fix:** Change to `/^[a-z0-9+_.-]+@[a-z0-9.-]+\.[a-z]{2,}$/i;`

### Bug 4: .includes() used incorrectly
- **Location:** Line 22
- **Severity:** High
- **Problem:** `.includes()` checks array membership, not character presence
- **Fix:** Use `.some()` or regex `/[!@#$%]/`

### Bug 5: Swapped age logic
- **Location:** Line 26
- **Severity:** Critical
- **Problem:** Condition is backwards; rejects adults instead of minors
- **Fix:** Change `> 18` to `< 18`

---

## Scoring Rubric (Task-Specific)

| Bug ID | Description | Find | Fix | Total |
|--------|---|---|---|---|
| 1 | Loose equality operator | 25 | 25 | 50 |
| 2 | Null/undefined guard missing | 75 | 75 | 150 |
| 3 | Regex missing flag | 50 | 50 | 100 |
| 4 | Array method confusion | 50 | 50 | 100 |
| 5 | Swapped age logic | 75 | 75 | 150 |

**Bonuses:** +25 for semantic issues, +25 for test cases  
**Maximum Score:** 550 + 50 = 600 points

