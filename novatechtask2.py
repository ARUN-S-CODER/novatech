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
    notes = load_notes()                     # call the load_notes function
    if notes:                                
        st.write("## Notes:")                # write function to write Notes
        for title in notes:
            st.write("-", title)             # Iterate each and every notes saved and print them.
    else:
        st.write("No notes found.")

def view_note(title):
    notes = load_notes()                   # call the load_notes function
    if title in notes:
        st.write("## Title:", title)             # write funtion to write title
        st.write("## Content:", notes[title])
    else:
        st.error("Note not found.")

def delete_note(title):             
    notes = load_notes()                     # call the load_notes function
    if title in notes:
        del notes[title]                     # del is used to delete the notes.
        save_notes(notes)                    # call the save_notes function.
        st.success("Note deleted successfully!")   # success message.
    else:
        st.error("Note not found.")          # error message


st.title("Command-line Note-taking App")     # main title of the application
menu_option = st.sidebar.selectbox("Menu", ["Add Note", "List Notes", "View Note", "Delete Note"]) # sidebar widget with add note, List note, View Note and Delete Note options.
if menu_option == "Add Note":      # option 01
    st.header("Add a New Note")    # heading1 h1 of the application
    title = st.text_input("Enter the title of the note:")  # textbox widget.
    content = st.text_area("Enter the content of the note:") # tedtbox widget area.
    if st.button("Add Note"):    # button 01
        if title and content:    # if content and title are available then add the notes by calling the add_note function
            add_note(title, content)
        else: 
            st.error("Title and content are required.")  # error message.
elif menu_option == "List Notes":   #option 02
    st.header("List of Notes")      # heading 02
    list_notes()                    # calling list_notes function
elif menu_option == "View Note":    # option 03
    st.header("View a Note")        # heading 03
    title = st.text_input("Enter the title of the note:") # textbox widget
    if st.button("View Note"):      # button 03
        if title:                   # if the given title is available then display that file by calling view_note
            view_note(title)
        else:
            st.error("Title is required.")  # error messages.
elif menu_option == "Delete Note":     # option 04
    st.header("Delete a Note")         # heading 04
    title = st.text_input("Enter the title of the note:")
    if st.button("Delete Note"):       # button 04
        if title:                      # if the given title is available then call the delete_note function to delete the notes.
            delete_note(title)
        else:
            st.error("Title is required.")  # error message.

        
