from mostcited import  MostCited
from subject import Subject 

most_cited = MostCited()
for url, data in most_cited.keys_tuples():
    print( most_cited.find(url,data) )

subject = Subject()
for key in subject.subject():
    print( key )