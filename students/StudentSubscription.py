from datetime import datetime


class StudentSubscription:
    def __init__(self, student_data: dict, subscription_levels: dict):
        self.student_data = student_data
        self.subscription_levels = subscription_levels

    def update_subscription(self, new_subscription: str):
        old_sub = self.student_data["SUBSCRIPTION"]
        student_features = self.student_data["ENABLED_FEATURES"]
        free_features = {key: False for (
            key, value) in student_features.items() if new_subscription == "free"}
        if (old_sub == new_subscription):
            raise ValueError(
                "The new subscription is the same, there's not an upgrade or downgrade")
        elif (self.subscription_levels[old_sub] < self.subscription_levels[new_subscription]):
            self.student_data["SUBSCRIPTION"] = new_subscription
            self.student_data["UPGRADE_DATE"] = str(datetime.now())
        else:
            self.student_data["SUBSCRIPTION"] = new_subscription
            self.student_data["DOWNGRADE_DATE"] = str(datetime.now())
            if new_subscription == "free":
                self.student_data["ENABLED_FEATURES"] = free_features
