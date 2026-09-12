import streamlit as st

# Check if session_state is empty and initialize if necessary
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Sidebar navigation
page = st.sidebar.selectbox("Trang", ["Trang Lập kế hoạch", "Trang Thực hiện"])

if page == "Trang Lập kế hoạch":
    st.title("Trang Lập kế hoạch")
    # Input field for new task
    new_task = st.text_input("Nhập công việc mới:")
    
    # Button to add task to the list
    if st.button("Thêm công việc"):
        if new_task:
            st.session_state.tasks.append(new_task)
            st.success("Công việc đã được thêm vào danh sách!")
    
    # Display the list of tasks
    st.header("Danh sách công việc")
    for task in st.session_state.tasks:
        st.write(task)

elif page == "Trang Thực hiện":
    st.title("Trang Thực hiện")
    # Display the list of tasks with checkboxes
    st.header("Danh sách công việc")
    for i, task in enumerate(st.session_state.tasks):
        st.checkbox(task, key=i)