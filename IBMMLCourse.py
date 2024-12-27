import sqlite3 as sq3
import pandas.io.sql as pds
import pandas as pd

path = 'data/baseball.db'
con = sq3.Connection(path)

query = '''
SELECT * FROM allstarfull;
'''

#hello world
# Execute the query
observations = pds.read_sql(query, con)

observations.head()

print(observations)

