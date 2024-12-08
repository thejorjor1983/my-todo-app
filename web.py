import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todor = st.session_state["new_todo"]
    todos.append(todor)
    functions.write_todos(todos)


st.title("My Minimalistic Grocery List")
st.subheader("Never forget food again!")
st.write("This app is to help you with the grocery buying process")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new grocery item...",
              on_change=add_todo, key='new_todo')