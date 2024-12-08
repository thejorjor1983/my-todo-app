import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todor = st.session_state["new_todo"]
    todos.append(todor)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ""


st.title("My Grocery List")
st.subheader("Never forget food again!")
st.write("Start your grocery list by entering an item below")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new grocery item...",
              on_change=add_todo, key='new_todo')