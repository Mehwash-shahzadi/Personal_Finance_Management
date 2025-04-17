class NotificationManager:
    def __init__(self):
        self.notification=[]

    def add_notification(self,notification):
        self.notification.append(notification)

    def send_all(self):
        for notification in self.notification:
            print(notification.send())

    def clear_notification(self):
        self.notification = []



class BudgetAlert:
    def __init__(self,category,budget_limit,current_spending):
        self.category=category
        self.budget_limit=budget_limit
        self.current_spending=current_spending

    def check_alert(self):
        return self.current_spending >= 0.9 * self.budget_limit

    def send(self):
        if self.check_alert():
            return f" Budget Alert: You're close to your {self.category} budget limit!"
        else:
            return f" You're within your {self.category} budget."


class GoalReminder:
    def __init__(self,goal_name,target_amount,current_progress):
        self.goal_name=goal_name
        self.target_amount=target_amount
        self.current_progress=current_progress

    def checkprogress(self):
        return self.current_progress>=self.target_amount
    
    def send(self):
        if self.checkprogress():
            return f" Goal Reached: You've achieved your goal - {self.goal_name}!"
        else:
            percent = (self.current_progress / self.target_amount) * 100
            return f" Reminder: You're {round(percent)}% towards your {self.goal_name} goal."
        

class ScheduledNotification:
    def __init__(self, message, frequency, scheduled_day):
        self.message = message
        self.frequency = frequency
        self.scheduled_day = scheduled_day  

    def should_send(self, today):
        return self.scheduled_day.lower() == today.lower()

    def send(self):
        return f" Scheduled Notification: {self.message}"
