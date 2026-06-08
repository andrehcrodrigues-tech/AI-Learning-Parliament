from pydantic import BaseModel

class LearnerProfile(BaseModel):
    role: str
    target_certification: str
    current_skills: str
    available_study_hours_per_week: int
    workload_signals: str
    career_goal: str
    team_goal: str
