import sys
import os

sys.path.append("..\\..\\Public\\")

import JSON_Function as j
from NFC_Reader import NFC_Reader
from FTPClient import FTPClient
from TopUpGUI import Open_TopUp
from NewUserGUI import NewUser_GUI


def is_uid_exists(nisit_data, uid):
    return uid in nisit_data


fileName = "nisit.json"
if __name__ == "__main__":
    ftp_client = FTPClient("127.0.0.1", user="admin", passwd="")

    # ดาวโหลดไฟล์ลง directory ปัจจุบัน
    ftp_client.download_file(fileName)

    # โหลดข้อมูลจาก json file
    all_nisit_data = j.load_data(fileName)

    # ตรวจสอบว่ามี UID อยู่แล้วในฐานข้อมูลหรือไม่
    uid = "11 22 33 42"  # UID ปลอมขึ้นมา
    if is_uid_exists(all_nisit_data, uid):
        print("UID already exists in the JSON file.")
        # ไปที่หน้าเติมเงินเข้าบัตร
        Open_TopUp(nisitData=all_nisit_data, uid=uid)
    else:
        NewUser_GUI(uid, all_nisit_data, ftp_client)
