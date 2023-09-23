import os
import json
from glob import glob

# -----

def merge_JsonFiles(filenames, targetfile):
  file_data = []

  for f1 in filenames:

    print(f1)
    with open(f1) as infile:
      data = json.load(infile)
      file_data.append(data)

  f = open(targetfile, "w")
  # convert back to json.
  json.dump(file_data, f, indent = 4)
  f.close


def findFiles(search_path):
  result = glob(search_path+"/*", recursive=True)

  return result


# -----

def main():
  files = findFiles("license-list-data/json/details")
  merge_JsonFiles(files, "data.json")


# -----

if __name__ == '__main__':
  main()
