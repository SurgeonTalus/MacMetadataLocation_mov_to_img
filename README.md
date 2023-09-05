# MacMetadataLocation_mov_to_img
Copies location metadata from mov to img

<!DOCTYPE html>
<html>
<head>
    <title>Metadata Embedding Script</title>
</head>
<body>

<h1>Metadata Embedding Script</h1>

<p>This script allows you to embed metadata from a video file into a photo file using exiftool on macOS.</p>

## Dependencies

- [exiftool](https://exiftool.org/) - A command-line tool for reading and writing metadata in various file formats.

## Installation

1. **Install exiftool:** If you haven't already, you can install exiftool via Homebrew:

    ```bash
    brew install exiftool
    ```

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. **Run the script:**

    Replace `"input_video.MOV"` and `"input_photo.jpg"` with the actual paths to your video and photo files.

    ```bash
    python embed_metadata.py
    ```

3. **Check the result:**

    The script will embed metadata from the video into the photo. You can check the photo file to see the changes.

## Example

Here's a sample usage of the script:

```python
import subprocess

def embed_metadata(video_path, photo_path):
    try:
        subprocess.run(["exiftool", "-overwrite_original", "-TagsFromFile", video_path, photo_path])
        print("Metadata embedded successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    input_video = "input_video.MOV"
    input_photo = "input_photo.jpg"

    embed_metadata(input_video, input_photo)
