from data.manager import DataManager
class ConsoleUi:
    def __init__(self):
        self.dm = DataManager.get_instance()
    def start_ui(self):
        self.dm.validate_data()

        while True:
           print('Personal Finance Management')
           print('1. Add Goal ')
           print('2. View Goals ') 
           print('3. Import Data ') 
           print('4. Export Data')  
           print('5. Exit')

           choice=input('Enter you choice(1-5):')

           if choice=='1':
                self.add_goal()
           elif choice=='2':
                self.view_goals()
           elif choice=='3':
                self.import_data()
           elif choice=='4':
                self.export_data()

           elif choice=='5':
               print('Exit')
               break
           else:
               print('Invalid choice.Enter number between (1-5)')
 
    def add_goal(self):
        try:
            name = input("Enter goal name: ")
            amount = float(input("Enter target amount: "))
            deadline = input("Enter deadline (e.g., 2025-12-31): ")
            goal = {"name": name, "amount": amount, "deadline": deadline}
            self.dm.add_goal(goal)
            self.dm.save_to_file()
            print("Goal added successfully.")
        except ValueError:
            print("Invalid input. Amount must be a number.")

    def view_goals(self):
        goals=self.dm.get_all_data().get('goals',[])
        if not goals:
            print("No goals found.")
        else:
            print("\nYour Goals:")
            for i, goal in enumerate(goals, 1):
                print(f"{i}. {goal['name']} - ${goal['amount']} by {goal['deadline']}")

    def import_data(self):
        path=input('Enter the import file path:')
        self.dm.import_data(path)

    def export_data(self):
        path=input('Enter the export file path:')
        self.dm.export_data(path)