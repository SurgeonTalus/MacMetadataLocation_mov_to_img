# GUI Program for Embedding Metadata and Modifying Dates

This GUI program allows you to embed metadata like location data from an input file (video or image) and modify the creation and modified dates of the output file(s). The program provides a simple user interface to select the input file and choose either a folder to process multiple files or a single output file.

![Embedded Modified Date](Modified%20Date.png)

## How It Works

1. **Select the Input File:** Click the "Select Input File" button to choose the input file. The input file can be a video (e.g., .mp4, .mov, .avi) or an image (e.g., .jpg, .png, .gif).

2. **Select the Output Folder or File:** Click the "Select Output" button to specify the output location. You can either choose a folder to process multiple files in batch mode or select a single output file.

3. **Embed Metadata and Modify Dates:** When you've chosen the input file and output location, click the "Embed Metadata & Modify Dates" button to execute the program. Metadata from the input file, including the "Modified Date," will be embedded into the output file(s). The creation and modified dates of the output file(s) will be updated to match the input file.

## Dependencies

To run this program on macOS, you need to install the following dependencies:

- [ExifTool](https://exiftool.org/): ExifTool is used to copy metadata from the input file to the output file. You can install it using [Homebrew](https://brew.sh/):

    ```shell
    brew install exiftool
    ```

## Running the Program

1. Clone or download this repository to your local machine.

2. Install the required dependencies (ExifTool) as mentioned above.

3. Open a terminal and navigate to the project directory.

4. Run the program by executing the following command:

    ```shell
    python gui_program.py
    ```

5. The GUI will open, allowing you to select the input file and choose the output folder or file. Follow the on-screen instructions to embed metadata and modify dates.

## Author

- Your Name

## License

This project is licensed under the [MIT License](LICENSE).
