#!/bin/bash
# Session 5 Scoring Helper Script
# Usage: ./scoring_helper.sh <command> [args]
# Commands:
#   init          - Create scoring sheets from template for all stages
#   totals <file> - Extract scores and compute total from a filled scoring sheet
#   adjudicate    - Compare two scorer sheets and flag disagreements (±15pt threshold)
#   summary       - Generate full scoring summary across all stages

SCORING_DIR="$(dirname "$0")"
TEMPLATE="$SCORING_DIR/scoring_template_distributed_flags.md"
SCORES_DIR="$SCORING_DIR/scores"
THRESHOLD=15

init() {
    echo "=== Initializing scoring sheets ==="
    mkdir -p "$SCORES_DIR"
    
    # Stages to score
    for stage in solo proposer skeptic proposer_revision; do
        for scorer in opus46 gpt54; do
            outfile="$SCORES_DIR/score_${stage}_${scorer}.md"
            if [ -f "$outfile" ]; then
                echo "  SKIP: $outfile already exists"
            else
                cp "$TEMPLATE" "$outfile"
                # Pre-fill the stage field
                case $stage in
                    solo) sed -i "s/\[Solo \/ Modified Structured (Proposer-Revision)\]/Solo/" "$outfile"
                           sed -i "s/\[Solo \/ Proposer \/ Skeptic \/ Proposer-Revision\]/Solo/" "$outfile" ;;
                    proposer) sed -i "s/\[Solo \/ Modified Structured (Proposer-Revision)\]/Modified Structured (pipeline stage)/" "$outfile"
                              sed -i "s/\[Solo \/ Proposer \/ Skeptic \/ Proposer-Revision\]/Proposer/" "$outfile" ;;
                    skeptic) sed -i "s/\[Solo \/ Modified Structured (Proposer-Revision)\]/Modified Structured (pipeline stage)/" "$outfile"
                             sed -i "s/\[Solo \/ Proposer \/ Skeptic \/ Proposer-Revision\]/Skeptic/" "$outfile" ;;
                    proposer_revision) sed -i "s/\[Solo \/ Modified Structured (Proposer-Revision)\]/Modified Structured (Proposer-Revision)/" "$outfile"
                                       sed -i "s/\[Solo \/ Proposer \/ Skeptic \/ Proposer-Revision\]/Proposer-Revision/" "$outfile" ;;
                esac
                # Pre-fill scorer name
                case $scorer in
                    opus46) sed -i "s/\[YOUR NAME\]/Opus 4.6/" "$outfile" ;;
                    gpt54) sed -i "s/\[YOUR NAME\]/GPT-5.4/" "$outfile" ;;
                esac
                echo "  CREATED: $outfile"
            fi
        done
    done
    echo "Done. Fill in scores by replacing ____/NNN with actual numbers."
}

totals() {
    local file="$1"
    if [ ! -f "$file" ]; then
        echo "Error: File not found: $file"
        return 1
    fi
    
    echo "=== Scores from: $(basename "$file") ==="
    
    # Extract dimension scores using pattern ____/NNN or NUMBER/NNN
    local dims=("System Understanding" "Insight Generation" "Decision Quality" "Validation Rigor" "Communication Clarity")
    local maxes=(130 180 140 70 30)
    local total=0
    local max_total=0
    local i=0
    
    for dim in "${dims[@]}"; do
        # Look for filled scores (number/max pattern)
        local score=$(grep -oP "(?<=\*\*Score:\*\* )\d+" "$file" | sed -n "$((i+1))p")
        if [ -z "$score" ]; then
            score="___"
        else
            total=$((total + score))
        fi
        max_total=$((max_total + ${maxes[$i]}))
        printf "  %-25s %s/%s\n" "${dims[$i]}:" "$score" "${maxes[$i]}"
        i=$((i+1))
    done
    
    echo "  -------------------------"
    local pct=$(python3 -c 'import sys; total=int(sys.argv[1]); max_total=int(sys.argv[2]); print(f"{(total*100/max_total):.1f}" if max_total else "0.0")' "$total" "$max_total")
    printf "  %-25s %s/%s (%s%%)\n" "TOTAL:" "$total" "$max_total" "$pct"
}

adjudicate() {
    echo "=== Adjudication Check (threshold: ±${THRESHOLD}pts per dimension) ==="
    echo ""
    
    # Compare solo scores
    for stage in solo proposer_revision; do
        local file1="$SCORES_DIR/score_${stage}_opus46.md"
        local file2="$SCORES_DIR/score_${stage}_gpt54.md"
        
        if [ ! -f "$file1" ] || [ ! -f "$file2" ]; then
            echo "  [$stage] Missing one or both scorer files — skipping"
            continue
        fi
        
        echo "  --- $stage ---"
        local dims=("System Understanding" "Insight Generation" "Decision Quality" "Validation Rigor" "Communication Clarity")
        local maxes=(130 180 140 70 30)
        local flags=0
        local total1=0
        local total2=0
        
        for i in $(seq 0 4); do
            local s1=$(grep -oP "(?<=\*\*Score:\*\* )\d+" "$file1" | sed -n "$((i+1))p")
            local s2=$(grep -oP "(?<=\*\*Score:\*\* )\d+" "$file2" | sed -n "$((i+1))p")
            
            if [ -z "$s1" ] || [ -z "$s2" ]; then
                printf "    %-25s  %s vs %s  [INCOMPLETE]\n" "${dims[$i]}:" "${s1:-___}" "${s2:-___}"
                continue
            fi
            
            local diff=$((s1 - s2))
            local abs_diff=${diff#-}
            total1=$((total1 + s1))
            total2=$((total2 + s2))
            local avg=$(( (s1 + s2) / 2 ))
            
            if [ "$abs_diff" -gt "$THRESHOLD" ]; then
                printf "    %-25s  %3d vs %3d  (diff=%+d)  🚨 FLAGGED — avg=%d\n" "${dims[$i]}:" "$s1" "$s2" "$diff" "$avg"
                flags=$((flags + 1))
            else
                printf "    %-25s  %3d vs %3d  (diff=%+d)  ✅ avg=%d\n" "${dims[$i]}:" "$s1" "$s2" "$diff" "$avg"
            fi
        done
        
        printf "    %-25s  %3d vs %3d\n" "TOTAL:" "$total1" "$total2"
        
        if [ "$flags" -gt 0 ]; then
            echo "    ⚠️  $flags dimension(s) flagged — discuss or invoke tiebreaker (Opus 4.5)"
        else
            echo "    ✅ All dimensions within threshold — use averages"
        fi
        echo ""
    done
}

summary() {
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║           SESSION 5 SCORING SUMMARY                        ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo ""
    
    for stage in solo proposer skeptic proposer_revision; do
        echo "━━━ Stage: $stage ━━━"
        for scorer in opus46 gpt54; do
            local file="$SCORES_DIR/score_${stage}_${scorer}.md"
            if [ -f "$file" ]; then
                totals "$file"
            else
                echo "  [$scorer] Not yet scored"
            fi
        done
        echo ""
    done
    
    echo "━━━ Adjudication ━━━"
    adjudicate
}

# Main dispatch
case "${1:-help}" in
    init) init ;;
    totals) totals "$2" ;;
    adjudicate) adjudicate ;;
    summary) summary ;;
    help|*)
        echo "Session 5 Scoring Helper"
        echo "Usage: $0 <command> [args]"
        echo ""
        echo "Commands:"
        echo "  init          Create scoring sheets from template for all stages"
        echo "  totals <file> Extract scores and compute total from a filled sheet"
        echo "  adjudicate    Compare two scorer sheets and flag ±15pt disagreements"
        echo "  summary       Full scoring summary across all stages"
        ;;
esac
