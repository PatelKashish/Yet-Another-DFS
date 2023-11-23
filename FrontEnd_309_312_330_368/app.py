import streamlit as st
import subprocess

global file_path
global destination_path

st.title("YADFS_309_312_330_368")

# Define Streamlit UI components
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Select Page", ["Home", "Commands", "About"])

if page == "Home":
    st.write("Discover the DFS Management System: Your hub for seamless operations!")
    st.write("Navigate the sidebar to explore diverse sections and enhance your experience.")
    subprocess.run(["python", "yadfs.py","--CONFIG","config\dfs_setup.json"], capture_output=False, text=True)

elif page == "Commands":
    st.subheader("DFS Commands")
    subpage = st.sidebar.selectbox("Select Page", ["Load", "Retrieve", "List", "Show", "Move", "Copy", "Create", "Delete file", "Destroy", "Clean"])
    
    if subpage == "Load":
        st.subheader("Upload")
        # user_input = st.text_area("Enter DFS command:", "")

        with st.form("User Input Form"):
        # Add a text input for username
        # username = st.text_input("Enter your username:")

            # Add a file uploader for file path
            file_path = st.file_uploader("Upload a file:")

            # Add a text input for destination path
            destination_path = st.text_input("File name in DFS:")

            # Add a submit button
            submit_button = st.form_submit_button("Submit")

        # Display the user input after form submission
        if submit_button:
            st.write("User Input:")
            # st.write(f"Username: {username}")
            st.write(f"File Path: {file_path.name if file_path else 'No file selected'}")
            st.write(f"File name in DFS: {destination_path}")


    elif subpage == "Retrieve":
        st.subheader("Download")

        with st.form("Download Form"):
            # Add a file uploader for file path
            file_path = st.file_uploader("Select a file in DFS:")

            # Add a text input for destination path
            destination_path = st.text_input("Save as:")

            # Add a submit button
            submit_button = st.form_submit_button("Submit")

        # Display the user input after form submission
        if submit_button:
            st.write("User Input:")
            st.write(f"File Path: {file_path.name if file_path else 'No file selected'}")
            st.write(f"Save as: {destination_path}")

            # Construct the 'download' command
            user_input = f"download {file_path.name if file_path else ''} {destination_path}"

            # Execute the command using subprocess and capture the output
            result = subprocess.run(user_input, shell=True, capture_output=True, text=True)

            # Display the output
            st.code(result.stdout)

    elif subpage == "List":
        st.subheader("List (Equivalent to 'ls')")

        with st.form("List Form"):
            # Add a text input for directory path
            directory_path = st.text_input("Enter directory path in DFS:")

            # Add a submit button
            submit_button = st.form_submit_button("Submit")

        # Display the user input after form submission
        if submit_button:
            st.write("User Input:")
            st.write(f"Directory Path in DFS: {directory_path}")

            # Construct the 'ls' command
            user_input = f"ls {directory_path}"

            # Execute the command using subprocess and capture the output
            result = subprocess.run(user_input, shell=True, capture_output=True, text=True)

            # Display the output
            st.code(result.stdout)

    elif subpage == "Show":
        st.subheader("Show (Equivalent to 'cat')")

        with st.form("Show Form"):
            # Add a text input for file path
            file_path = st.text_input("Enter file path in DFS:")

            # Add a submit button
            submit_button = st.form_submit_button("Submit")

        # Display the user input after form submission
        if submit_button:
            st.write("User Input:")
            st.write(f"File Path in DFS: {file_path}")

            # Construct the 'cat' command
            user_input = f"cat {file_path}"

            # Execute the command using subprocess and capture the output
            result = subprocess.run(user_input, shell=True, capture_output=True, text=True)

            # Display the output
            st.code(result.stdout)

    
    elif subpage == "Create":
        st.subheader("Create (Equivalent to 'mkdir')")

        with st.form("Create Form"):
            # Add a text input for directory path
            directory_path = st.text_input("Enter directory path in DFS:")

            # Add a submit button
            submit_button = st.form_submit_button("Submit")

        # Display the user input after form submission
        if submit_button:
            st.write("User Input:")
            st.write(f"Directory Path in DFS: {directory_path}")

            # Construct the 'mkdir' command
            user_input = f"mkdir {directory_path}"

            # Execute the command using subprocess and capture the output
            result = subprocess.run(user_input, shell=True, capture_output=True, text=True)

            # Display the output
            st.code(result.stdout)

    elif subpage == "Move":
        st.subheader("Move (Equivalent to 'mv')")

        with st.form("Move Form"):
            # Add a text input for source file/directory path
            source_path = st.text_input("Enter source path in DFS:")

            # Add a text input for destination path
            destination_path = st.text_input("Enter destination path in DFS:")

            # Add a submit button
            submit_button = st.form_submit_button("Submit")

        # Display the user input after form submission
        if submit_button:
            st.write("User Input:")
            st.write(f"Source Path in DFS: {source_path}")
            st.write(f"Destination Path in DFS: {destination_path}")

            # Construct the 'mv' command
            user_input = f"mv {source_path} {destination_path}"

            # Execute the command using subprocess and capture the output
            result = subprocess.run(user_input, shell=True, capture_output=True, text=True)

            # Display the output
            st.code(result.stdout)

    elif subpage == "Copy":
        st.subheader("Copy")

        with st.form("Copy Form"):
            # Add a text input for source file/directory path
            source_path = st.text_input("Enter source path in DFS:")

            # Add a text input for destination path
            destination_path = st.text_input("Enter destination path in DFS:")

            # Add a submit button
            submit_button = st.form_submit_button("Submit")

        # Display the user input after form submission
        if submit_button:
            st.write("User Input:")
            st.write(f"Source Path in DFS: {source_path}")
            st.write(f"Destination Path in DFS: {destination_path}")

            # Construct the 'cp' command
            user_input = f"cp {source_path} {destination_path}"

            # Execute the command using subprocess and capture the output
            result = subprocess.run(user_input, shell=True, capture_output=True, text=True)

            # Display the output
            st.code(result.stdout)

    elif subpage == "Del":
        st.subheader("Delete (Equivalent to 'rm')")

        with st.form("Delete Form"):
            # Add a text input for file or directory path
            file_or_directory_path = st.text_input("Enter file or directory path in DFS:")

            # Add a submit button
            submit_button = st.form_submit_button("Submit")

        # Display the user input after form submission
        if submit_button:
            st.write("User Input:")
            st.write(f"File or Directory Path in DFS: {file_or_directory_path}")

            # Construct the 'rm' command
            user_input = f"rm {file_or_directory_path}"

            # Execute the command using subprocess and capture the output
            result = subprocess.run(user_input, shell=True, capture_output=True, text=True)

            # Display the output
            st.code(result.stdout)

    elif subpage == "Destroy":
        st.subheader("Destroy (Equivalent to 'rmdir')")

        with st.form("Destroy Form"):
            # Add a text input for directory path
            directory_path = st.text_input("Enter directory path in DFS:")

            # Add a submit button
            submit_button = st.form_submit_button("Submit")

        # Display the user input after form submission
        if submit_button:
            st.write("User Input:")
            st.write(f"Directory Path in DFS: {directory_path}")

            # Construct the 'rmdir' command
            user_input = f"rmdir {directory_path}"

            # Execute the command using subprocess and capture the output
            result = subprocess.run(user_input, shell=True, capture_output=True, text=True)

            # Display the output
            st.code(result.stdout)

    elif subpage == "Clean":
        st.subheader("Clean (Formatting the DFS)")

        with st.form("Clean Form"):
            # Add a button for clean operation
            clean_button = st.form_submit_button("Clean")

        # Display the user input after form submission
        if clean_button:
            st.write("User Input:")
            st.write("Cleaning DFS...")

            # Construct the 'format_namenode_datanode' command
            user_input = "format_namenode_datanode"

            # Execute the command using subprocess and capture the output
            result = subprocess.run(user_input, shell=True, capture_output=True, text=True)

            # Display the output
            st.code(result.stdout)


elif page == "About":
    st.subheader("About")
    st.write("Welcome to the DFS Command Center - Unleash the Power of Your Data!")
    st.write("Embark on a journey of exploration using the sidebar to access different features.")