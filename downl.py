
import gdown
import zipfile
import os

def download_folder_from_drive(file_id, output_zip_path):
    """Download a zipped folder from Google Drive using gdown."""
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output_zip_path, quiet=False)

def unzip_folder(zip_file_path, extract_to_dir):
    """Unzip the downloaded file to the specified directory."""
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_dir)

def main():
    # Replace 'YOUR_FILE_ID' with your actual file ID
    file_id = '15LlJZDkicrEGBStQmfPei0XFzTQt18DE'
    zip_file_path = 'downloaded_folder.zip'
    unzip_dir = 'unzipped_folder'

    print("Downloading folder...")
    download_folder_from_drive(file_id, zip_file_path)
    
    if os.path.exists(zip_file_path):
        print(f"Downloaded file saved as {zip_file_path}.")
        print("Unzipping folder...")
        unzip_folder(zip_file_path, unzip_dir)
        print(f"Folder extracted to {unzip_dir}.")
    else:
        print("Failed to download the file.")

if __name__ == "__main__":
    main()
