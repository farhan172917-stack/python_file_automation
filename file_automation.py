import os
import shutil
import logging

# -------------------------------
# Logging Setup
# -------------------------------
LOG_FILE = "file_automation.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# Files considered junk
JUNK_FILES = [".DS_Store"]
JUNK_EXTENSIONS = [".tmp", ".bak", ".cache"]


# -------------------------------
# Get Folder Path
# -------------------------------
def get_folder():
    while True:
        folder = input("Enter folder path: ").strip().strip('"')

        if not folder:
            print("Folder path cannot be empty.")
            continue

        if not os.path.exists(folder):
            print("Folder does not exist.")
            continue

        if not os.path.isdir(folder):
            print("The path is not a folder.")
            continue

        return os.path.abspath(folder)


# -------------------------------
# Sort Files
# -------------------------------
def sort_files(folder):
    print("\n--- Sorting Files ---")
    logging.info("Starting SORT operation")

    try:
        files = os.listdir(folder)

        for file in files:
            file_path = os.path.join(folder, file)

            # Ignore folders
            if os.path.isdir(file_path):
                continue

            extension = os.path.splitext(file)[1].lower()

            if extension:
                extension = extension[1:].upper()
            else:
                extension = "OTHER"

            new_folder = os.path.join(folder, extension + "_files")

            try:
                os.makedirs(new_folder, exist_ok=True)

                new_path = os.path.join(new_folder, file)

                if os.path.exists(new_path):
                    print(f"Skipped: {file}")
                    logging.warning(f"Skipped: {file}")
                    continue

                shutil.move(file_path, new_path)

                print(f"Moved: {file} -> {extension}_files/")
                logging.info(f"Moved {file} -> {extension}_files/")

            except (OSError, shutil.Error) as error:
                print(f"Error moving {file}: {error}")
                logging.error(f"Error moving {file}: {error}")

        print("Sorting completed.")
        logging.info("SORT operation completed")

    except OSError as error:
        print(f"Error reading folder: {error}")
        logging.error(f"Error reading folder: {error}")


# -------------------------------
# Rename Files
# -------------------------------
def rename_files(folder):
    print("\n--- Renaming Files ---")

    prefix = input("Enter prefix (example: photo): ").strip()

    if not prefix:
        prefix = "file"

    logging.info(f"Starting RENAME operation with prefix: {prefix}")

    try:
        files = [
            file for file in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, file))
        ]

        for number, file in enumerate(files, start=1):

            extension = os.path.splitext(file)[1]
            new_name = f"{prefix}_{number:03d}{extension}"

            old_path = os.path.join(folder, file)
            new_path = os.path.join(folder, new_name)

            try:
                if os.path.exists(new_path):
                    print(f"Skipped: {new_name}")
                    logging.warning(f"Skipped rename: {new_name}")
                    continue

                os.rename(old_path, new_path)

                print(f"Renamed: {file} -> {new_name}")
                logging.info(f"Renamed {file} -> {new_name}")

            except OSError as error:
                print(f"Error renaming {file}: {error}")
                logging.error(f"Error renaming {file}: {error}")

        print("Renaming completed.")
        logging.info("RENAME operation completed")

    except OSError as error:
        print(f"Error reading folder: {error}")
        logging.error(f"Error reading folder: {error}")


# -------------------------------
# Clean Files
# -------------------------------
def clean_files(folder):
    print("\n--- Cleaning Files ---")
    logging.info("Starting CLEAN operation")

    deleted = 0

    try:
        for file in os.listdir(folder):

            file_path = os.path.join(folder, file)

            if not os.path.isfile(file_path):
                continue

            extension = os.path.splitext(file)[1].lower()

            if file in JUNK_FILES or extension in JUNK_EXTENSIONS:

                try:
                    os.remove(file_path)

                    print(f"Deleted: {file}")
                    logging.info(f"Deleted junk file: {file}")

                    deleted += 1

                except OSError as error:
                    print(f"Error deleting {file}: {error}")
                    logging.error(f"Error deleting {file}: {error}")

        # Remove empty folders
        for root, directories, files in os.walk(folder, topdown=False):

            for directory in directories:

                directory_path = os.path.join(root, directory)

                try:
                    if not os.listdir(directory_path):
                        os.rmdir(directory_path)

                        print(f"Removed empty folder: {directory}")
                        logging.info(f"Removed empty folder: {directory}")

                except OSError as error:
                    logging.error(
                        f"Error removing folder {directory}: {error}"
                    )

        print(f"Cleaning completed. Files deleted: {deleted}")
        logging.info(
            f"CLEAN operation completed. Files deleted: {deleted}"
        )

    except OSError as error:
        print(f"Error reading folder: {error}")
        logging.error(f"Error reading folder: {error}")


# -------------------------------
# Main Program
# -------------------------------
def main():

    print("=" * 45)
    print("       FILE AUTOMATION TOOL")
    print("=" * 45)

    logging.info("=== New session started ===")

    while True:

        print("\nChoose an operation:")
        print("1. Sort Files")
        print("2. Rename Files")
        print("3. Clean Files")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "4":
            print("Goodbye!")
            logging.info("=== Session ended ===")
            break

        if choice not in ["1", "2", "3"]:
            print("Invalid choice. Please select 1-4.")
            continue

        folder = get_folder()

        try:
            if choice == "1":
                sort_files(folder)

            elif choice == "2":
                rename_files(folder)

            elif choice == "3":
                clean_files(folder)

        except Exception as error:
            print(f"Unexpected error: {error}")
            logging.exception("Unexpected error occurred")


# -------------------------------
# Run Program
# -------------------------------
if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
        logging.warning("Program interrupted by user.")