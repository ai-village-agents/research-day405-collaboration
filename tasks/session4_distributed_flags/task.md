# Session 3: Distributed Feature Flag Regression

## Scenario
The growth team attempted to roll out a phased release of the new "Discover Feed" feature across web and mobile. The rollout relies on a shared feature flag (`discover_feed`) served by the backend `flag_service`, consumed by the React web app, and logged by the analytics pipeline. Mid-deployment, the backend service shipped a new schema version for flag snapshots. The React frontend and the analytics event processor were still running their previous releases when the rollout stalled.

Operations noticed three inconsistent behaviors:
- Some web sessions received the new targeting rules, others stayed on the old defaults even after hard refreshes.
- Mobile traffic (still on the legacy API) sent analytics events indicating the flag was disabled, contradicting backend dashboards.
- A/B test reports showed duplicate `discover_feed` variants because downstream jobs treated some payloads as schema v1 and others as v2.

The incident triggered an incident review. You have the code snapshots from the partial deployment window. The goal is to identify how the backend, frontend, analytics job, and shared schema drifted out of sync and to propose fixes that make the system resilient to version skew.

## Expectations
- Map out how flag payloads should propagate from `flag_service.js` to `FeatureGate.jsx` and `event_processor.py`.
- Diagnose why different clients observed different flag states and why the analytics tables diverged.
- Highlight caching or memoization that turns the bug into a non-deterministic failure.
- Recommend concrete code or design changes to prevent similar regressions (schema validation, cache busting, deployment sequencing, etc.).
- Prepare a depth-weighted evaluation using the provided rubric (see `answer_key.md`).

You do **not** need to implement the fixes—focus on forensic analysis and actionable recommendations grounded in the code.
