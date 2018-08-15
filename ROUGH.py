# Import create_engine function
import psycopg2
from sqlalchemy import *
# Create an engine to the census database
engine = create_engine('postgresql+psycopg2://postgres:pucit123@localhost/test')
census = Table('company', metadata, autoload=True, autoload_with=engine)

# Build select statement for census table: stmt
stmt = select([census])

# Print the emitted statement to see the SQL emitted
print(stmt)

# Execute the statement and print the results
print(engine.execute(stmt).fetchall())
# Print the table names
print(engine.table_names())
