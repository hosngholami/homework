from hossein_gholami_hw5.src.read_file import read_file
def load_proffesor():
  try:
    data =  read_file('/hossein_gholami_hw5/data/proffesor.json')
    return data
  except:
    print('first, you insert proffesor data')
