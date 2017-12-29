from qc import q
from datetime import date

q.insert('trade', (date(2006, 10, 6), 'IBM', 200))
print q

