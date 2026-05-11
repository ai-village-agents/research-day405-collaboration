# Pilot Task: JavaScript Code Review

## Overview
Review the following JavaScript code for bugs. The code contains **6 seeded bugs** of varying severity.

## Time Limit
45 minutes

## Deliverable Format
For each bug found, provide:
1. **Line number** (or approximate location)
2. **Bug description** (what's wrong)
3. **Severity** (Critical/High/Medium/Low)
4. **Fix suggestion** (how to correct it)

---

## Code to Review

```javascript
// cosmic-sight-validator.js
// Validates cosmic sight entries before insertion into the universe

const fs = require('fs');

function validateCosmicSight(sight) {
    const errors = [];
    
    // Check required fields
    if (!sight.name || sight.name.length = 0) {  // BUG 1: Assignment instead of comparison
        errors.push('Name is required');
    }
    
    // Validate position array
    if (!Array.isArray(sight.position) || sight.position.length !== 3) {
        errors.push('Position must be an array of 3 coordinates');
    } else {
        // Check each coordinate is a number
        for (let i = 0; i <= sight.position.length; i++) {  // BUG 2: Off-by-one (should be <)
            if (typeof sight.position[i] !== 'number') {
                errors.push(`Position[${i}] must be a number`);
            }
        }
    }
    
    // Validate color hex code
    if (sight.color) {
        const hexPattern = /^#[0-9A-Fa-f]{6}$/;
        if (!hexPattern.test(sight.color)) {
            errors.push('Color must be a valid hex code');
        }
    }
    
    // Validate size
    if (sight.size !== undefined) {
        if (sight.size < 0 || sight.size > 100) {
            errors.push('Size must be between 0 and 100');
        }
    }
    
    return errors;
}

async function validateBatch(filePath) {
    const content = fs.readFileSync(filePath, 'utf8');
    const sights = JSON.parse(content);
    
    const results = {
        valid: [],
        invalid: [],
        duplicates: []
    };
    
    const seenNames = {};  // BUG 3: Should be new Set() for O(1) lookup, but this is just inefficient not a bug
    
    for (const sight of sights) {
        const errors = validateCosmicSight(sight);
        
        // Check for duplicate names
        if (seenNames[sight.name]) {  // BUG 4: This works but doesn't handle case sensitivity
            results.duplicates.push(sight.name);
        }
        seenNames[sight.name] = true;
        
        if (errors.length === 0) {
            results.valid.push(sight);
        } else {
            results.invalid.push({ sight, errors });
        }
    }
    
    // Generate summary report
    console.log(`Validation Complete:`);
    console.log(`  Valid: ${results.valid.length}`);
    console.log(`  Invalid: ${results.invalid.length}`);
    console.log(`  Duplicates: ${results.duplicates}`);  // BUG 5: Should be .length for count
    
    return results;
}

function checkPositionBounds(sight, bounds) {
    const [x, y, z] = sight.position;
    const { minX, maxX, minY, maxY, minZ, maxZ } = bounds;
    
    // BUG 6: Logic error - should be OR conditions, not AND for out-of-bounds check
    if (x < minX && x > maxX || y < minY && y > maxY || z < minZ && z > maxZ) {
        return false;
    }
    return true;
}

module.exports = { validateCosmicSight, validateBatch, checkPositionBounds };
```

---

## Scoring Rubric (Max 600 points)

| Bug | Severity | Points for Finding | Points for Correct Fix |
|-----|----------|-------------------|----------------------|
| Bug 1 | Critical | 50 | 50 |
| Bug 2 | Critical | 50 | 50 |
| Bug 3 | Low (efficiency) | 25 | 25 |
| Bug 4 | Medium | 50 | 50 |
| Bug 5 | Medium | 50 | 50 |
| Bug 6 | Critical | 50 | 50 |

**Bonus points:**
- +25 for identifying additional edge cases
- +25 for suggesting comprehensive test cases

---

## Answer Key (FOR STUDY LEAD ONLY)

<details>
<summary>Click to reveal answer key</summary>

1. **Line 11:** `sight.name.length = 0` uses assignment `=` instead of comparison `===`
2. **Line 18:** Loop condition `i <= sight.position.length` causes array out-of-bounds (should be `<`)
3. **Line 47:** Object `{}` for name tracking is fine but `new Set()` would be more idiomatic
4. **Line 51:** Case-insensitive duplicate check not handled (`"Alpha"` vs `"alpha"`)
5. **Line 62:** `results.duplicates` prints array, should be `results.duplicates.length`
6. **Line 72:** Logic should be `x < minX || x > maxX || ...` (OR not AND)

</details>
