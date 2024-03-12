# tracker.py

class FitnessTracker:
    def __init__(self, user):
        self.user = user
        self.activities = []

    def add_activity(self, activity):
        self.activities.append(activity)

    def get_activities(self):
        return self.activities

    # Add more methods as needed
