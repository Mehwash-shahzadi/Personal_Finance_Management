import streamlit as st
from data.manager import DataManager


dm = DataManager.get_instance()
dm.validate_data()

st.title('Personal Finance Management')

menu=st.sidebar.selectbox('Menu',['Add Goal','View Goals','Import Data','Export Data','Exit'])

if menu=='Add Goal':
    st.subheader('Add a new Goal')
    name=st.text_input('Enter the Goal name')
    amount=st.number_input('Enter the Amount',min_value=1)
    deadline=st.date_input('Deadline')

    if st.button('Add Goal'):
        goal = {"name": name, "amount": amount, "deadline": str(deadline)}
        dm.add_goal(goal)
        dm.save_to_file()
        st.success("Goal added successfully!")
elif menu == "View Goals":
    st.subheader("Your Goals")
    goals = dm.get_all_data().get("goals", [])
    
    if not goals:
        st.warning("No goals found.")
    else:
        for i, goal in enumerate(goals, 1):
            st.write(f"{i}. {goal['name']} - ${goal['amount']} by {goal['deadline']}")
elif menu == "Import Data":
    st.subheader("Import Data")
    path = st.text_input("Enter import file path")
    if st.button("Import"):
        dm.import_data(path)
        st.success("Data imported successfully.")

elif menu == "Export Data":
    st.subheader("Export Data")
    path = st.text_input("Enter export file path")
    if st.button("Export"):
        dm.export_data(path)
        st.success("Data exported successfully.")

elif menu == "Exit":
    st.info("You can now close the tab to exit.")





    