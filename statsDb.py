import sqlite3
import pathlib


class StatsDb:
  def __init__(self):
    self.conn = sqlite3.connect('data/stats.db')
    self.cursor = self.conn.cursor()

  
  def createDb(self):
    pathlib.Path('data').mkdir(parents=True, exist_ok=True)
    res = self.cursor.execute("SELECT name FROM sqlite_master WHERE name='summary'")
    if not res.fetchone():
      self.cursor.execute("CREATE TABLE summary (date TEXT PRIMARY KEY, overallSleep INTEGER, overallStress INTEGER)")

  def insertSummary(self, date, overallSleep, overallStress):
    try:
      self.cursor.execute("INSERT INTO summary (date, overallSleep, overallStress) VALUES (?, ?, ?)", (date, overallSleep, overallStress))
      self.conn.commit()
    except sqlite3.IntegrityError:
      print("Data already exists")
