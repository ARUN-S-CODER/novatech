import streamlit as st  # importing section
import json             # importing section

def load_notes():
    try: # try block
        with open("notes.json", "r") as file: # opening a file with read mode
            return json.load(file)            # load the file
    except FileNotFoundError:                 # expect block for filenot found exception
        return {}

def save_notes(notes):                       # save note function
    with open("notes.json", "w") as file:    # open the file with write mode
        json.dump(notes, file)               

def add_note(title, content):                # add notes function
    notes = load_notes()                     # call the load function
    notes[title] = content                   # store the content with respective to their title
    save_notes(notes)                        # call the save function
    st.success("Note added successfully!")   # success message.

def list_notes():                            # list note function
    notes = load_notes()
    if notes:                                
        st.write("## Notes:")
        for title in notes:
            st.write("-", title)
    else:
        st.write("No notes found.")

def view_note(title):
    notes = load_notes()
    if title in notes:
        st.write("## Title:", title)
        st.write("## Content:", notes[title])
    else:
        st.error("Note not found.")

def delete_note(title):
    notes = load_notes()
    if title in notes:
        del notes[title]
        save_notes(notes)
        st.success("Note deleted successfully!")
    else:
        st.error("Note not found.")


st.title("Command-line Note-taking App")
menu_option = st.sidebar.selectbox("Menu", ["Add Note", "List Notes", "View Note", "Delete Note"])
if menu_option == "Add Note":
    st.header("Add a New Note")
    title = st.text_input("Enter the title of the note:")
    content = st.text_area("Enter the content of the note:")
    if st.button("Add Note"):
        if title and content:
            add_note(title, content)
        else:
            st.error("Title and content are required.")
elif menu_option == "List Notes":
    st.header("List of Notes")
    list_notes()
elif menu_option == "View Note":
    st.header("View a Note")
    title = st.text_input("Enter the title of the note:")
    if st.button("View Note"):
        if title:
            view_note(title)
        else:
            st.error("Title is required.")
elif menu_option == "Delete Note":
    st.header("Delete a Note")
    title = st.text_input("Enter the title of the note:")
    if st.button("Delete Note"):
        if title:
            delete_note(title)
        else:
            st.error("Title is required.")

        
