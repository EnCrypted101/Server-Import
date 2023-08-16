# Server-Import Setup:

Step 1: Make a folder called: "server"

Step 2: Paste in all the files in the folder

Step 3: Open a terminal and navigate to the root folder of your package "server". Example: cd [path of your server folder]

Step 4: Run: "pip install ."

Package is installed!

# Server-Import Commands:

Replace this with the actual path where you want to create the player data file:
`folder_path = "/path/to/your/folder"`

Create a player data file using the function from the server module:
`data_file_path = server.create_player_data_file(folder_path)
print(f"Player data file created at: {data_file_path}")`

You can use other functions or variables defined in the server module
For example, if you define additional functions or variables in server.py

Example: Calling another function from the server module:
`def display_message():
    server.show_message("Hello from the server module!")`
`display_message()`


Example: Using a variable from the server module
`print(f"Server version: {server.SERVER_VERSION}")`






