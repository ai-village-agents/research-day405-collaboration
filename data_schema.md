# Historical + Experimental Data Schema

## Table 1: tasks
- task_id: unique ID
- task_family: source_summary | code_inspection | hypothesis_generation
- task_title: short human-readable title
- source_packet_path: path or URL for source materials
- answer_key_path: path or URL for answer key / adjudication notes
- seeded_error_count: integer (0 if not applicable)
- planted_discrepancy_count: integer (0 if not applicable)
- objective_claim_opportunities: integer
- notes: free text

## Table 2: runs
- run_id: unique ID
- task_id: foreign key to tasks
- condition: solo | unstructured | structured_cross_check
- start_ts: ISO timestamp
- end_ts: ISO timestamp
- duration_min: numeric
- completed: yes | no
- exclusion_flag: yes | no
- exclusion_reason: free text
- final_output_path: path to final answer
- transcript_path: path to transcript/log
- deidentified_output_path: path to blinded output

## Table 3: participants
- run_id: foreign key to runs
- agent_name: model/agent identifier
- role: proposer | skeptic | synthesizer | verifier | finisher | soloist | discussant | judge | tiebreak_judge | study_lead
- order_in_run: integer
- notes: free text

## Table 4: process_features
- run_id: foreign key to runs
- explicit_roles_present: 0/1
- checklist_present: 0/1
- validator_or_external_check_present: 0/1
- citations_or_evidence_links_present: 0/1
- revisions_before_final: integer
- errors_flagged_pre_final: integer
- errors_corrected_pre_final: integer
- unsupported_claims_noted_pre_final: integer
- conflict_or_disagreement_event: 0/1
- handoff_count: integer

## Table 5: judge_scores
- run_id: foreign key to runs
- judge_id: identifier
- accuracy_score: 0-4
- unsupported_claims_score: 0-4
- error_detection_score: 0-4
- novelty_score: 0-4
- clarity_score: 0-4
- time_score: 0-4
- evidence_notes: free text

## Table 6: historical_cases
For retrospective village-history extraction where exact run-level info may be partial.

- case_id: unique ID
- day_range: e.g. 395-404
- project_name: short label
- task_type: technical | creative | outreach | hybrid
- apparent_team_size: integer or range
- coordination_mode: solo | free_form | structured_roles | swarm | mixed
- explicit_roles_present: 0/1/unknown
- validator_or_checklist_present: 0/1/unknown
- observable_error_correction_event_count: integer or approximate
- outcome_status: success | partial | failed | mixed
- timing_signal: available | partial | unavailable
- notes: free text

## Minimum fields for historical extraction
If time is tight, capture at least:
1. case_id
2. day_range
3. project_name
4. task_type
5. apparent_team_size
6. coordination_mode
7. explicit_roles_present
8. validator_or_checklist_present
9. observable_error_correction_event_count
10. outcome_status
11. timing_signal
12. notes
