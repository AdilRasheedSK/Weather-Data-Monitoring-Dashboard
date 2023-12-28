from ftplib import FTP
import datetime
import os
from dotenv import load_dotenv
from .dataEntry import run
from members.models import Member
import subprocess

load_dotenv()

def connect():
    user_input = input("Enter a date (YYYY-MM-DD): ")

    try:
        parsed_date = datetime.datetime.strptime(user_input, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None

    print(f"Date entered: {parsed_date}")
    x = parsed_date.strftime('%Y%m%d')
    folder_path = os.path.join("path_where_you_want_to_store_data_Files", "downloaded_files")
    os.makedirs(folder_path, exist_ok=True)

    # Delete all previously downloaded files
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted file: {file}")
        except Exception as e:
            print(f"Error deleting file: {file} - {e}")

    # Delete all existing entries from the Member model
    Member.objects.all().delete()

    with FTP("Server_IP_address") as ftp:
        ftp.set_pasv(False)
        ftp.login("Server_Name", "Server_Password")
        # ftp.cwd("Another_file")  #optional,,,if you want to change working directory

        for i in range(96):
            try:
                start_time = datetime.datetime.strptime("0000", "%H%M")
                current_time = start_time + datetime.timedelta(minutes=15 * i)
                formatted_time = current_time.strftime("%H%M")
                z = x + formatted_time
                fdate = "TEST4567_" + z + "00_02.csv"
                filename = os.path.join(folder_path, fdate)

                with open(filename, "wb") as target_file:
                    # Write the downloaded content directly to the target file
                    ftp.retrbinary(f"RETR {fdate}", target_file.write)
                    print("successfully file downloaded")

                # You can call the run() function or perform additional operations here if needed.
                run(filename)
            except Exception as e:
                print(f"Error: {e}")

        print("After downloading all files.")

    flask_app_path = os.path.join("members", "scripts", "app.py")
    subprocess.run(["python", flask_app_path])





