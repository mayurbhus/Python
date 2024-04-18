import json

#Function that returns the list of all vidoes.
def all_videos(videos):
    if len(videos) == 0:
        print("File not available. Select option 2 to create file.")
    else:
        print("-" *50)
        for index, video in enumerate(videos, start=1):
            print(f"{index}.{video['title']}({video['duration']})")
        print("-" *50)

#Function that add video in the list.            
def add_video(videos):
    title = input("Enter title of video : ")
    duration = input("Enter duration of video : ")
    videos.append({'title' : title, 'duration' : duration})
    save_data_helper(videos)

#Function that update any video from the list.
def update_list(videos):
    if len(videos) == 0:
        print("There is no file to update. Select option 2 to create file.")
    else:
        all_videos(videos)
        index = input("Which video you want to update : ")
        new_title = input("Enter new title : ")
        new_duration = input("Enter duration : ")
        videos[int(index)-1] = {'title' : new_title, 'duration' : new_duration}
        save_data_helper(videos)
        print("Updated list : ")
        all_videos(videos)

#Function for deletion of a video.
def delete_video(videos):
    all_videos(videos)
    index = int(input("Enter which video you want to delete : "))
    del videos[index-1]
    save_data_helper(videos)
    all_videos(videos)

#Function which read from the file in JSON format.
def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

#Function which write to the file.    
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

#Main program.
def main():

    videos = load_data()

    while True:
        print("\n")
        print("Welcome to YouTube Manager")
        print("1. List of saved videos")
        print("2. Add item to list")
        print("3. Update list")
        print("4. Delete item from list")
        print("5. Exit")
        choice = input("Enter your choice : ")

        match choice:
            case '1':
                all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_list(videos)
            case '4':
                delete_video(videos)
            case '5':
                break

#Program execution starts here.
if __name__ == "__main__":
    main()
