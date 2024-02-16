from stats import Stats
from statsDb import StatsDb
import sqlite3




if __name__ == "__main__":
  stats = Stats()
  statsDb = StatsDb()
  stats.login()
  curDate, overallSleep, overallStress = stats.getDaySummary()
  statsDb.insertSummary(curDate, overallSleep, overallStress)
