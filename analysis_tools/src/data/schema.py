"""
Data schema module for AI Village coordination research.
Matches GPT-5.4's minimal schema and extends it for comprehensive analysis.
"""

from dataclasses import dataclass, asdict, field
from typing import List, Dict, Optional, Union, Any
from enum import Enum
import json
from datetime import datetime
from pathlib import Path


class CoordinationMode(str, Enum):
    """Coordination modes observed in AI Village."""
    SOLO = "solo"
    UNSTRUCTURED = "unstructured_discussion"
    STRUCTURED = "structured_cross_check"
    COMPETITIVE = "competitive"
    COLLABORATIVE = "collaborative"
    PARALLEL = "parallel_individual"
    SEMI_STRUCTURED = "semi_structured"


class TaskType(str, Enum):
    """Task type categories."""
    CREATIVE = "creative"
    TECHNICAL = "technical"
    RESEARCH = "research"
    SOCIAL_OUTREACH = "social_outreach"
    INFRASTRUCTURE = "infrastructure"
    GAME_DEV = "game_development"
    FUNDRAISING = "fundraising"
    BENCHMARK = "benchmark"


class OutcomeStatus(str, Enum):
    """Outcome status categories."""
    COMPLETED = "completed"
    PARTIAL = "partial"
    FAILED = "failed"
    ABANDONED = "abandoned"


@dataclass
class HistoricalGoal:
    """Historical data schema for village goals."""
    # Core identifiers
    id: int
    name: str
    start_day: int
    end_day: int
    duration_days: int
    
    # Coordination characteristics
    coordination_mode: str
    team_size: int
    agents: List[str]
    task_type: str
    
    # Structure indicators
    explicit_roles: bool
    validator_present: bool
    human_guidance_level: str  # "high", "medium", "low"
    
    # Performance metrics
    outcome: str
    outcome_vs_target: str
    success_level: int  # 1-5 scale
    
    # Error handling
    error_recovery_speed: str  # "fast", "medium", "slow"
    error_correction_count: Optional[int] = None
    
    # Timing and efficiency
    role_emergence_time: Optional[str] = None  # e.g., "8 days", "<4 minutes"
    notable_events: List[str] = field(default_factory=list)
    coordination_notes: List[str] = field(default_factory=list)
    
    # Derived metrics
    validator_effect: Optional[float] = None
    structure_score: Optional[float] = None  # 0-1 scale
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization."""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'HistoricalGoal':
        """Create instance from dictionary."""
        return cls(**data)


@dataclass
class ExperimentRun:
    """Experimental data schema for controlled experiments."""
    # Core identifiers
    run_id: str
    condition: CoordinationMode
    task_id: str  # e.g., "pilot_task_b"
    participants: List[str]
    start_time: str
    end_time: str
    duration_minutes: float
    
    # Performance metrics (from rubric)
    bugs_found_count: int
    bugs_total_count: int
    bugs_found_percentage: float
    fixes_correct_count: int
    fixes_total_count: int
    fixes_correct_percentage: float
    
    # Quality metrics
    edge_cases_identified: int
    test_cases_suggested: int
    novelty_rating: Optional[float] = None  # 1-5 scale
    insight_rating: Optional[float] = None  # 1-5 scale
    
    # Error handling
    errors_caught_pre_finalization: Optional[int] = None
    errors_escaped_finalization: Optional[int] = None
    
    # Communication metrics (if available)
    message_count: Optional[int] = None
    validation_checkpoints: Optional[int] = None
    
    # Derived metrics
    total_score: float
    max_score: float
    score_percentage: float
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization."""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ExperimentRun':
        """Create instance from dictionary."""
        return cls(**data)


class DataLoader:
    """Loader for historical and experimental data."""
    
    def __init__(self, data_dir: Union[str, Path] = "../data"):
        self.data_dir = Path(data_dir)
        
    def load_historical_goals(self, filename: str = "historical/village_goal_timeline.json") -> List[HistoricalGoal]:
        """Load historical goal data."""
        filepath = self.data_dir / filename
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        goals = []
        for goal_data in data.get("goals", []):
            # Convert to HistoricalGoal dataclass
            goal = HistoricalGoal.from_dict(goal_data)
            goals.append(goal)
        
        return goals
    
    def load_experimental_runs(self) -> List[ExperimentRun]:
        """Load experimental run data from various sources."""
        # This would be implemented based on actual experimental data structure
        runs = []
        
        # Example placeholder - would load from actual experiment files
        return runs


class DataValidator:
    """Validator for data consistency and completeness."""
    
    @staticmethod
    def validate_historical_goals(goals: List[HistoricalGoal]) -> Dict[str, Any]:
        """Validate historical goal data."""
        validation = {
            "total_goals": len(goals),
            "missing_fields": [],
            "inconsistent_data": [],
            "coverage_stats": {}
        }
        
        required_fields = ["id", "name", "coordination_mode", "team_size", "outcome"]
        
        for goal in goals:
            for field in required_fields:
                value = getattr(goal, field, None)
                if value is None or (isinstance(value, str) and value.strip() == ""):
                    validation["missing_fields"].append(f"Goal {goal.id}: missing {field}")
        
        return validation


# Export main classes
__all__ = [
    "CoordinationMode",
    "TaskType",
    "OutcomeStatus",
    "HistoricalGoal",
    "ExperimentRun",
    "DataLoader",
    "DataValidator"
]
