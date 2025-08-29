import time
import requests
from datetime import datetime

URL = "https://www.easydoct.com/api/rdv/getRdvDayAvailabilities"

HEADERS = {
    "Host": "www.easydoct.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/json",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://www.easydoct.com",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://www.easydoct.com/rdv/gie-irldr-imagerie-rennes",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-GPC": "1",
    "Cookie": (
        "SessionKey=6dc848b2-353a-4c65-a420-e0cce551520c_213594302; "
        "UserSessionKey=N; "
        ".AspNet.Cookies=F2vNLg7g1iyNZmlyk1fZhQC96e2X4fi7mglcF-N3Ir-OH52__2mtQsiVG0rDVupibe2pnb-PAa9hqTb4hRjZJp2O9xkAJfny-LGl87FCh17TuV3Tzqd_fXl6GgaLyhcLQNjpDunbcGR4oHmq-4DDjTfZZDsuVQtcOHCvMIxq_Hifk2OmPzu5ajIHR2lbKnMQwcGSE7_jRYP_JM2WQi8Fqeh0jmgjmucnkbbU96IqIvLTvZp05S1r6ZUK97ZiyhG3ouMEUyzbS6cmgsn36-TP11iwLsISWBfpFpAtDu7KvP0tS1Xhfa18MOVHn_EUWewTOO9SH79sXYf5JnI1gxjmJswP1vfQrNUFP8oSuIZXfmjuL_EiWxSxSNLGH-6wvyU-V8audTAupC-AJzsti6Lyfg6pqbOn1tuAMMIxdeK_Mm8-1IHCP8bCguz1oOSgU47w3y5T992eIANT2VtOz9pwHXJrPohOkHMHf-63q4tWKlwtxG-tNPthiyRumLJlN3vXUxGtRw"
    )
}

PAYLOAD = {"examTypeId" : "3374",
           "minDate" :  datetime.today().strftime("%Y%m%d"),
           "examId" : "56794",
           "examSetId" : None,
           "practitionerId" : None,
           "officePlaceIds" : None,
           "isMobileView" : None,
           "patientBirthDate" : "1979-04-18T22:00:00.000+02:00",
           "officePlaceHubId" : None}

def check_availability():
    try:
        response = requests.post(URL, headers=HEADERS, json=PAYLOAD)
        if response.status_code != 200:
            print(f"HTTP error {response.status_code}")
            return False

        data = response.json()
        if data.get("availabilityCount", 0) > 0:
            print("Appointments are available!")
            for line in data.get("availabilityLines", []):
                print(f" - {line}")
            return True
        else:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] No slot available.")
            return False

    except Exception as e:
        print(f"Error: {e}")
        return False

# Check every 5 minutes
while True:
    if check_availability():
        break
    time.sleep(60)
