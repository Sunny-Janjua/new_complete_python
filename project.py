import os

# Load video data from a file
def load_data():
    try:
        if os.path.exists("youtube.txt"):
            with open("youtube.txt", "r") as file:
                print(file.read())
        else:
            print("No data file found, starting fresh.")
    except Exception as e:
        print(f"Error: {e}")

# Print all videos
def print_all_videos(videos):
    print("-" * 100)
    if not videos:
        print("No videos available.")
    else:
        print("Our all videos:")
        for video in videos:
            print(f"ID: {video['id']}, Name: {video['name']}, Length: {video['length']}")

# Show a single video
def show_one_video(videos):
    try:
        video_id = input("Enter your ID: ")
        for video in videos:
            if video["id"] == video_id:
                print(f"Video found: {video}")
                return
        print("Video not found!")
    except Exception as e:
        print(f"Error: {e}")

# Add a new video
def add_one_video(videos):
    try:
        video_id = input("Enter video ID: ")
        name = input("Enter video name: ")
        length = input("Enter video length: ")

        videos.append({"id": video_id, "name": name, "length": length})
        print("Video added successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Update a video
def update_one_video(videos):
    try:
        video_id = input("Enter video ID to update: ")
        for video in videos:
            if video["id"] == video_id:
                video["name"] = input("Enter new name: ")
                video["length"] = input("Enter new length: ")
                print("Video updated successfully!")
                return
        print("Video not found!")
    except Exception as e:
        print(f"Error: {e}")

# Delete a video
def delete_one_video(videos):
    try:
        video_id = input("Enter video ID to delete: ")
        for video in videos:
            if video["id"] == video_id:
                videos.remove(video)
                print("Video deleted successfully!")
                return
        print("Video not found!")
    except Exception as e:
        print(f"Error: {e}")

# Exit the app
def exit_our_app():
    print("Exiting the app... Goodbye!")

# Initial video list
videos = [{"id": "1", "name": "sunny", "length": "5min"}]

# Main function
def main():
    while True:
        load_data()
        print("-" * 100)
        print("Welcome to My YouTube App!")
        print("1 - Show all videos")
        print("2 - Add a video")
        print("3 - Show a single video")
        print("4 - Update a video")
        print("5 - Delete a video")
        print("6 - Exit")
        print("-" * 100)

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print_all_videos(videos)
            case "2":
                add_one_video(videos)
            case "3":
                show_one_video(videos)
            case "4":
                update_one_video(videos)
            case "5":
                delete_one_video(videos)
            case "6":
                exit_our_app()
                break
            case _:
                print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
