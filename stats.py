from garth import Client as GarthClient

import os
from dotenv import load_dotenv
import garth
from garth.exc import GarthException
from datetime import date, timedelta

load_dotenv()

class Stats:
    TOKENS_PATH = "tokens/garth"

    def __init__(self, tokenPath="tokens/garth"):
        self.tokenPath = tokenPath

    def __login(self):
      email = os.getenv("GARMIN_USERNAME")
      password = os.getenv("GARMIN_PASSWORD")
      try:
        garth.client.login(email, password)
      except GarthException as e:
        print("Login failed, check your credentials")

      garth.save(self.tokenPath)

    def login(self):
      # Try to resume the session from the tokens file
      try:
        garth.resume(self.tokenPath)
      except (FileNotFoundError, GarthException):
        self.__login()

      username = garth.client.username
      print("Logged in as", username)

    def getDaySummary(self):
      cur_date = str(date.today() - timedelta(days=1))
      # Sleep for today - the previous sleep, where date is current day
      sleepOverall = garth.DailySleep.list(period=1)[0].value
      stressOverall = garth.DailyStress.list(date.today() - timedelta(days=1))[0].overall_stress_level

      return (cur_date, sleepOverall, stressOverall)

    def fetchLatestSleepQuality(self):
      print(garth.DailySleep.list(period=1)[0].value)
    