from mostcited import  MostCited

a = MostCited()
for url, data in a.keys_tuples():
    print( a.find(url,data) )