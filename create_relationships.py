"""
Description:
 Creates the relationships table in the Social Network database
 and populates it with 100 fake relationships.

Usage:
 python create_relationships.py
"""
import os
import sqlite3 
from faker import Faker
fake = Faker()
from random import randint, choice 

# Determine the path of the database
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'social_network.db')

def main():
    create_relationships_table()
    populate_relationships_table()

def create_relationships_table():
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    # SQL query that creates a table named 'relationships'.
    create_relationships_tbl_query = """
    CREATE TABLE IF NOT EXISTS relationships    
    (
    id INTEGER PRIMARY KEY,
    person1_id INTEGER NOT NULL,
    person2_id INTEGER NOT NULL,
    type TEXT NOT NULL,
    start_date DATE NOT NULL,
    FOREIGN KEY (person1_id) REFERENCES people (id),
    FOREIGN KEY (person2_id) REFERENCES people (id) 
    );
    """
    # Execute the SQL query to create the 'relationships' table.
    cur.execute(create_relationships_tbl_query)
    con.commit()
    con.close()

def populate_relationships_table():
   
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    # SQL query that inserts a row of data in the relationships table.
    add_relationship_query = """
    INSERT INTO relationships
    (
    person1_id,
    person2_id,
    type,
    start_date
    )
    VALUES (?, ?, ?, ?);
    """
    
    for _ in range(100):
            person1_id = randint(1, 100)
            person2_id = randint(1, 100)
            while person2_id == person1_id:
                person2_id = randint(1, 100)
            rel_type = choice(('friend', 'spouse', 'partner', 'family'))
            start_date = fake.date_between(start_date='-50y', end_date='today')
            new_relationship = (person1_id, person2_id, rel_type, start_date)
            cur.execute(add_relationship_query, new_relationship)
    con.commit()
    con.close() 

if __name__ == '__main__':
   main()