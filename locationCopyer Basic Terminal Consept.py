import subprocess
def embed_metadata(video_path, photo_path):
    try:
        # Use exiftool to copy metadata from video to photo
        subprocess.run(["exiftool", "-overwrite_original", "-TagsFromFile", video_path, photo_path])
        print("Metadata embedded successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    input_video = "input_video.MOV"
    input_photo = "input_photo.jpg"

    embed_metadata(input_video, input_photo)
