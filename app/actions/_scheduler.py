from datetime import datetime
DISTRIBUTIONS={"linear","front_loaded","back_loaded","bell_curve"}
def should_run(schedule: dict, now: datetime) -> bool:
    if schedule.get("paused"): return False
    windows=schedule.get("allowed_windows", [])
    if not windows: return True
    day=now.strftime("%a").lower()[:3]
    return any(day in w.get("days", []) and w.get("start_hour",0) <= now.hour < w.get("end_hour",24) for w in windows)
def batch_size(schedule: dict) -> int:
    return int(schedule.get("batch_size", 50))
