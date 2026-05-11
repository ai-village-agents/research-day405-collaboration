#!/usr/bin/env python3
"""
Visualization tools for multi-agent coordination research results.
Generates figures for blogpost and paper.
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from typing import List, Dict, Tuple

# Set publication-quality defaults
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = 'sans-serif'

def plot_pilot_comparison(results: Dict[str, Dict[str, float]], output_path: str = 'pilot_comparison.png'):
    """
    Create box/bar plot comparing Solo, Unstructured, Structured conditions.
    
    Args:
        results: Dict with condition names as keys, containing 'score' and 'max_score'
        output_path: Where to save the figure
    """
    conditions = list(results.keys())
    percentages = [results[c]['score'] / results[c]['max_score'] * 100 for c in conditions]
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    bars = ax.bar(conditions, percentages, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    
    # Add value labels on bars
    for bar, pct in zip(bars, percentages):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{pct:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    ax.set_ylabel('Score (%)', fontsize=12)
    ax.set_xlabel('Coordination Condition', fontsize=12)
    ax.set_title('Pilot Experiment: Bug-Finding Accuracy by Coordination Mode', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_ylim(0, 110)
    ax.axhline(y=100, color='gray', linestyle='--', alpha=0.5, label='Perfect Score')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_path}")
    return fig

def plot_historical_coordination_modes(data: List[Tuple[str, float, int]], 
                                       output_path: str = 'historical_modes.png'):
    """
    Create bar chart showing average outcome by coordination mode from historical data.
    
    Args:
        data: List of (mode_name, avg_outcome, count) tuples
        output_path: Where to save the figure
    """
    modes, outcomes, counts = zip(*sorted(data, key=lambda x: x[1], reverse=True))
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = ['#2ECC71' if out >= 2.5 else '#F39C12' if out >= 2.0 else '#E74C3C' 
              for out in outcomes]
    bars = ax.barh(modes, outcomes, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    
    # Add count labels
    for bar, count, outcome in zip(bars, counts, outcomes):
        width = bar.get_width()
        ax.text(width + 0.05, bar.get_y() + bar.get_height()/2.,
                f'n={count}', ha='left', va='center', fontsize=9)
    
    ax.set_xlabel('Average Outcome Quality (0-3 scale)', fontsize=12)
    ax.set_ylabel('Coordination Mode', fontsize=12)
    ax.set_title('Historical Analysis: Outcome Quality by Coordination Mode (22 Goals)', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(0, 3.3)
    
    # Add reference lines
    ax.axvline(x=2.0, color='gray', linestyle='--', alpha=0.3, label='Acceptable')
    ax.axvline(x=2.5, color='green', linestyle='--', alpha=0.3, label='Good')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_path}")
    return fig

def plot_validator_impact(with_validator: Dict, without_validator: Dict,
                         output_path: str = 'validator_impact.png'):
    """
    Create grouped bar chart showing validator impact on error recovery and outcomes.
    
    Args:
        with_validator: Dict with 'fast_recovery_pct', 'avg_outcome', 'count'
        without_validator: Same structure
        output_path: Where to save the figure
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Fast recovery comparison
    categories = ['With\nValidator', 'Without\nValidator']
    recovery = [with_validator['fast_recovery_pct'], without_validator['fast_recovery_pct']]
    
    bars1 = ax1.bar(categories, recovery, color=['#2ECC71', '#E74C3C'], 
                   alpha=0.8, edgecolor='black', linewidth=1.5)
    
    for bar, val in zip(bars1, recovery):
        ax1.text(bar.get_x() + bar.get_width()/2., val + 2,
                f'{val:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    ax1.set_ylabel('Fast Error Recovery (%)', fontsize=11)
    ax1.set_title('Error Recovery Speed', fontsize=12, fontweight='bold')
    ax1.set_ylim(0, 60)
    
    # Outcome quality comparison
    outcomes = [with_validator['avg_outcome'], without_validator['avg_outcome']]
    counts = [with_validator['count'], without_validator['count']]
    
    bars2 = ax2.bar(categories, outcomes, color=['#2ECC71', '#E74C3C'], 
                   alpha=0.8, edgecolor='black', linewidth=1.5)
    
    for bar, val, n in zip(bars2, outcomes, counts):
        ax2.text(bar.get_x() + bar.get_width()/2., val + 0.05,
                f'{val:.2f}\n(n={n})', ha='center', va='bottom', fontweight='bold')
    
    ax2.set_ylabel('Average Outcome Quality (0-3)', fontsize=11)
    ax2.set_title('Overall Outcome Quality', fontsize=12, fontweight='bold')
    ax2.set_ylim(0, 3)
    ax2.axhline(y=2.5, color='gray', linestyle='--', alpha=0.5)
    
    fig.suptitle('Historical Validator Impact Analysis (22 Goals, 405 Days)', 
                fontsize=14, fontweight='bold', y=1.02)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_path}")
    return fig

def plot_role_emergence_timeline(data: List[Tuple[int, float]], 
                                 output_path: str = 'role_emergence.png'):
    """
    Create line plot showing role emergence speed over village history (H4).
    
    Args:
        data: List of (village_day, days_to_role_emergence) tuples
        output_path: Where to save the figure
    """
    days, emergence_time = zip(*sorted(data))
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(days, emergence_time, marker='o', linewidth=2.5, markersize=8,
           color='#3498DB', markerfacecolor='white', markeredgewidth=2)
    
    # Add trend line
    z = np.polyfit(days, emergence_time, 2)
    p = np.poly1d(z)
    x_smooth = np.linspace(min(days), max(days), 100)
    ax.plot(x_smooth, p(x_smooth), '--', color='red', linewidth=2, alpha=0.7, label='Trend')
    
    ax.set_xlabel('Village Day', fontsize=12)
    ax.set_ylabel('Days Until Explicit Roles Emerge', fontsize=12)
    ax.set_title('Role Emergence Speed Over Time (H4: Coordination Efficiency Improvement)', 
                fontsize=14, fontweight='bold', pad=20)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_path}")
    return fig

def plot_rubric_radar(scores: Dict[str, Dict[str, float]], 
                     output_path: str = 'rubric_radar.png'):
    """
    Create radar chart showing blinded rubric scores across 6 dimensions.
    
    Args:
        scores: Dict with condition names as keys, containing dimension scores (0-4)
        output_path: Where to save the figure
    """
    dimensions = ['Completeness', 'Correctness', 'Clarity', 'Insight', 
                  'Efficiency', 'Robustness']
    num_vars = len(dimensions)
    
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # Complete the circle
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
    
    colors = {'Solo': '#FF6B6B', 'Unstructured': '#4ECDC4', 'Structured': '#45B7D1'}
    
    for condition, color in colors.items():
        if condition in scores:
            values = [scores[condition].get(dim, 0) for dim in dimensions]
            values += values[:1]  # Complete the circle
            
            ax.plot(angles, values, 'o-', linewidth=2, label=condition, 
                   color=color, markersize=8)
            ax.fill(angles, values, alpha=0.15, color=color)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(dimensions, size=11)
    ax.set_ylim(0, 4)
    ax.set_yticks([1, 2, 3, 4])
    ax.set_yticklabels(['1', '2', '3', '4'], size=9)
    ax.set_title('Blinded Rubric Scores by Coordination Mode', 
                fontsize=14, fontweight='bold', pad=30)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=11)
    ax.grid(True)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_path}")
    return fig

# Example usage with placeholder data
if __name__ == "__main__":
    print("Multi-Agent Coordination Research - Visualization Tools")
    print("=" * 60)
    
    # Example: Pilot comparison (will be updated with real data)
    pilot_results = {
        'Solo': {'score': 450, 'max_score': 525},
        'Unstructured': {'score': 600, 'max_score': 650},
        'Structured': {'score': 525, 'max_score': 525}
    }
    # plot_pilot_comparison(pilot_results)
    
    # Example: Historical coordination modes
    historical_data = [
        ('Competitive/Individual', 3.00, 4),
        ('Structured/Semi-Structured', 2.60, 5),
        ('Parallel Individual', 2.60, 5),
        ('Unstructured', 2.00, 2),
        ('Collaborative (No Structure)', 1.80, 5)
    ]
    plot_historical_coordination_modes(historical_data)
    
    # Example: Validator impact
    validator_data = {
        'with': {'fast_recovery_pct': 50.0, 'avg_outcome': 2.60, 'count': 6},
        'without': {'fast_recovery_pct': 0.0, 'avg_outcome': 2.38, 'count': 16}
    }
    plot_validator_impact(validator_data['with'], validator_data['without'])
    
    print("\nVisualization complete! Ready to generate final plots with real data.")
