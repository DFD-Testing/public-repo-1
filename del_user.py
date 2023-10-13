from zipfile import ZipFile

def extract_bad(zippath, dest):
    zipped = ZipFile(zippath)
    try:
        zipped.extractall(dest)
    finally:
        zipped.__del__()

if __name__=="__main__" : 
  extract_bad()
