#
# Day 19
#
# Change:
#    - First version
#

import streamlit as st
import functions

#
# Functions
#

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    print(todo)                            # Debug message
    todos.append(todo)
    functions.write_todos(todos)


#
# Main program
#

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):      # Enumerate populates the index variable for todos
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]              # Delete the todo from session state
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")


# Debug messages
print("Executed py script.")

st.session_state          # This will show in the web browser
                          # It only shows the state of widgets that have a key.