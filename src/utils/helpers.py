def build_prompt(profile: dict) -> str:
    return f"""
Role: {profile.get('role')}
Target Certification: {profile.get('target_certification')}
Current Skills: {profile.get('current_skills')}
Available Study Hours: {profile.get('available_study_hours_per_week')} hours/week
Workload: {profile.get('workload_signals')}
Career Goal: {profile.get('career_goal')}
Team Goal: {profile.get('team_goal')}
"""
