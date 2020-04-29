def test():

  import urllib.request


  file_path = r'C:\Users\bryan\Desktop\Python\Git\Python_practice\example.txt'

  url = r'https://google.com'

  html = None

  with urllib.request.urlopen(url) as req:
    html = req.read()

  with open(file_path, 'w') as f:
    #print(html, file=f)
    print(html)


if __name__ == '__main__':
  from timeit import timeit
  print(timeit("test()", setup="from __main__ import test", number=50))
  #standard print == 18.003/18.289/17.608 #flush=True print == 18.162/19.573/19.651 #flush=False ==21.050/20.571/19.786
