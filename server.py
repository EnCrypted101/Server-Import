import os

def create_player_data_file(folder_path):
    data_folder = os.path.join(folder_path, 'player_data')
    
    if not os.path.exists(data_folder):
        os.mkdir(data_folder)
    
    data_file_path = os.path.join(data_folder, 'data.txt')
    
    with open(data_file_path, 'w') as file:
        file.write("Player data goes here!")

    return data_file_path
