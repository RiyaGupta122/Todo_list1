import streamlit as st

def main():
    st.title("✅ To-Do List Checker")
    
    # Initialize session state for tasks if it doesn't exist
    if 'tasks' not in st.session_state:
        st.session_state.tasks = []
    if 'completed' not in st.session_state:
        st.session_state.completed = []

    # Input for new task
    new_task = st.text_input("Add a new task:")
    if st.button("Add Task") and new_task:
        st.session_state.tasks.append(new_task)
        st.success(f"Added task: {new_task}")

    # Display pending tasks
    st.subheader("Pending Tasks")
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([4,1])
        with col1:
            st.write(f"- {task}")
        with col2:
            if st.button("Complete", key=f"complete_{i}"):
                st.session_state.completed.append(task)
                st.session_state.tasks.pop(i)
                st.rerun()

    # Display completed tasks
    if st.session_state.completed:
        st.subheader("Completed Tasks")
        for task in st.session_state.completed:
            st.write(f"✅ {task}")

if __name__ == "__main__":
    main()
