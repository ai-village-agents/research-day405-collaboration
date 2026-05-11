#!/usr/bin/env python3
"""
Visualization script for pilot experiment results.
Generates comparison charts for Solo vs Unstructured vs Structured conditions.
"""

import matplotlib.pyplot as plt
import numpy as np

def create_pilot_comparison_chart(data, output_path='pilot_comparison.png'):
    """
    Create a bar chart comparing pilot conditions.
    
    Args:
        data: dict with keys 'solo', 'unstructured', 'structured'
              each containing {'score': float, 'max': float, 'bugs_found': int, 'bugs_total': int}
    """
    conditions = ['Solo', 'Unstructured', 'Structured']
    
    # Calculate percentages
    percentages = []
    for cond in ['solo', 'unstructured', 'structured']:
        if cond in data and data[cond]['score'] is not None:
            pct = (data[cond]['score'] / data[cond]['max']) * 100
            percentages.append(pct)
        else:
            percentages.append(0)  # Pending
    
    # Create figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Chart 1: Score percentages
    colors = ['#ff6b6b' if p == 0 else '#4ecdc4' if p == 100 else '#45b7d1' for p in percentages]
    bars = ax1.bar(conditions, percentages, color=colors, edgecolor='black')
    ax1.set_ylabel('Score (%)', fontsize=12)
    ax1.set_title('Pilot Experiment: Score by Condition', fontsize=14)
    ax1.set_ylim(0, 110)
    ax1.axhline(y=100, color='green', linestyle='--', alpha=0.5, label='Perfect score')
    
    # Add value labels
    for bar, pct in zip(bars, percentages):
        if pct > 0:
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                    f'{pct:.1f}%', ha='center', fontsize=11, fontweight='bold')
        else:
            ax1.text(bar.get_x() + bar.get_width()/2, 5,
                    'PENDING', ha='center', fontsize=10, color='red')
    
    # Chart 2: Bugs found
    bugs_found = []
    bugs_total = []
    for cond in ['solo', 'unstructured', 'structured']:
        if cond in data and data[cond]['bugs_found'] is not None:
            bugs_found.append(data[cond]['bugs_found'])
            bugs_total.append(data[cond]['bugs_total'])
        else:
            bugs_found.append(0)
            bugs_total.append(0)
    
    x = np.arange(len(conditions))
    width = 0.35
    
    bars1 = ax2.bar(x - width/2, bugs_found, width, label='Bugs Found', color='#4ecdc4')
    bars2 = ax2.bar(x + width/2, bugs_total, width, label='Total Bugs', color='#95a5a6')
    
    ax2.set_ylabel('Count', fontsize=12)
    ax2.set_title('Bugs Found vs Total Seeded Bugs', fontsize=14)
    ax2.set_xticks(x)
    ax2.set_xticklabels(conditions)
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    
    return output_path


# Example usage with current data
if __name__ == '__main__':
    # Current pilot data (update as results come in)
    pilot_data = {
        'solo': {
            'score': None,  # PENDING - awaiting GPT-5.1
            'max': 525,
            'bugs_found': None,
            'bugs_total': 5,
            'task': 'pilot_task_b'
        },
        'unstructured': {
            'score': 600,
            'max': 650,
            'bugs_found': 6,
            'bugs_total': 6,
            'task': 'pilot_task.md'  # Different task!
        },
        'structured': {
            'score': 525,
            'max': 525,
            'bugs_found': 5,
            'bugs_total': 5,
            'task': 'pilot_task_b'
        }
    }
    
    output = create_pilot_comparison_chart(pilot_data)
    print(f"Chart saved to: {output}")
    print("\nNote: Solo condition still pending. Cross-task comparison caveat applies.")
