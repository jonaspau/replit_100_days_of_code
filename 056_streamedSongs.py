import os
import csv

filename = "100MostStreamedSongs.csv"

with open(filename) as f:
  
  reader = csv.DictReader(f)
  for row in reader:
    dir = os.listdir()
    artist = row["Artist(s)"]
    song = row["Song"]
    
    if artist not in dir:
      os.mkdir(artist)
    
    path = os.path.join(f"{artist}/{song}")
    f = open(path, "w")
    f.close()
