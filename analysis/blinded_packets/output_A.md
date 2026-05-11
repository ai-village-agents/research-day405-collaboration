# Output A

## Task family
Seeded bug inspection.

## Final output

### Summary
- **Total Bugs Found:** 6/6
- **Critical:** 3
- **Medium:** 2
- **Low:** 1

### Detailed Findings

#### Bug 1: Assignment Instead of Comparison
- **Location:** Line 11
- **Severity:** Critical
- **Description:** `sight.name.length = 0` uses assignment operator `=` instead of comparison `===`
- **Impact:** Always assigns 0 to length property, then evaluates as falsy. Name validation is broken.
- **Proposed Fix:** `if (!sight.name || sight.name.length === 0)`

#### Bug 2: Off-by-One Array Bounds Error
- **Location:** Line 18
- **Severity:** Critical
- **Description:** Loop condition `i <= sight.position.length` iterates past array bounds
- **Impact:** Accesses `position[3]` which is undefined, causing false "not a number" errors
- **Proposed Fix:** `for (let i = 0; i < sight.position.length; i++)`

#### Bug 3: Suboptimal Data Structure
- **Location:** Line 47
- **Severity:** Low (efficiency)
- **Description:** Uses plain object `{}` for tracking seen names instead of `Set`
- **Impact:** Technically works but less idiomatic. O(1) either way but Set is cleaner.
- **Proposed Fix:** `const seenNames = new Set();` with `seenNames.has()` / `seenNames.add()`

#### Bug 4: Case-Sensitive Duplicate Detection
- **Location:** Line 51
- **Severity:** Medium
- **Description:** Duplicate name check is case-sensitive
- **Impact:** "Alpha" and "alpha" treated as different names, allowing semantic duplicates
- **Proposed Fix:** Normalize: `seenNames[sight.name.toLowerCase()]`

#### Bug 5: Array Printed Instead of Count
- **Location:** Line 62
- **Severity:** Medium
- **Description:** `console.log` prints `results.duplicates` (array) not its length
- **Impact:** Output shows "[name1, name2]" instead of "2" - confusing summary
- **Proposed Fix:** `console.log(\`  Duplicates: ${results.duplicates.length}\`);`

#### Bug 6: Logic Error in Bounds Check
- **Location:** Line 72
- **Severity:** Critical
- **Description:** Uses `&&` (AND) between min/max comparisons: `x < minX && x > maxX`
- **Impact:** Condition is mathematically impossible - no value can be both < min AND > max. Function always returns true (in bounds).
- **Proposed Fix:** `if (x < minX || x > maxX || y < minY || y > maxY || z < minZ || z > maxZ)`

### Additional observations
1. **Null/undefined sight:** No guard against null input.
2. **Non-finite coordinates:** `NaN` / `Infinity` could pass a typeof check.
3. **Empty input array:** Could yield misleading output.
4. **Missing bounds properties:** Bounds helper assumes all properties exist.
5. **Description field not validated:** No check for existence or length.

### Suggested test cases
- Valid sight
- Empty name
- Boundary-length position array
- Case-insensitive duplicate pair
- Out-of-bounds position
- `NaN` in position array
