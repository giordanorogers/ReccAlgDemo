import sqlite3
import json


def initialize_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('communities.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employees (
            EmpID INT PRIMARY KEY,
            EmpName TEXT,
            Location TEXT,
            OrgLvl1 TEXT,
            OrgLvl2 TEXT,
            OrgLvl3 TEXT,
            Spaces TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Spaces (
            SpaceID INT PRIMARY KEY,
            SpaceName TEXT,
            Description TEXT,
            Category TEXT,
            Members TEXT
        )
    ''')

    # Check if Employees table is empty and insert data if it is
    cursor.execute('SELECT COUNT(*) FROM Employees')
    if cursor.fetchone()[0] == 0:
        cursor.execute(f'''
            INSERT INTO Employees (
                EmpID, 
                EmpName,
                Location,
                OrgLvl1,
                OrgLvl2,
                OrgLvl3,
                Spaces
            )
            VALUES 
            (101, 'Spongebob Squarepants', 'Boston', 'LM Technology', 'LMI Tech-LMI', 'LMI Technology-03433', '{json.dumps([8, 10, 9])}'),
            (102, 'Sandy Cheeks', 'Boston', 'LM Technology', 'LM Tech-USRM Tech', 'USRM Tech-Distribution Tech', '{json.dumps([1, 3, 8])}'),
            (103, 'Pearl Krabs', 'Boston', 'LM Technology', 'LM Tech-Corporate Functions', 'CF-Global Finance Tech', '{json.dumps([5, 8, 1])}'),
            (104, 'Patrick Star', 'Boston', 'LM Technology', 'LM Tech-USRM Tech', 'USRM Tech-Distribution Tech', '{json.dumps([6, 2, 7])}'),
            (105, 'Eugence Krabs', 'Boston', 'LM Technology', 'LM Tech-USRM Tech', 'USRM Tech-Product Tech', '{json.dumps([6, 4, 8])}'),
            (106, 'Sheldon Plankton', 'Boston', 'LM Technology', 'LM Tech-USRM Tech', 'USRM Tech-Servicing Tech', '{json.dumps([4, 7, 3])}'),
            (107, 'Gary the Snail', 'Boston', 'LM Technology', 'LM Tech-LMI', 'LMI Technology-0433', '{json.dumps([9, 2, 10])}'),
            (108, 'Squidward Tentacles', 'Boston', 'LM Technology', 'LM Tech-USRM Tech', 'USRM Tech-Claims Tech', '{json.dumps([3, 2, 6])}'),
            (109, 'Mermaid Man', 'Boston', 'LM Technology', 'LM Tech-LMI', 'LMI Technology-03433', '{json.dumps([5, 8])}')
        ''')

    # Check if Spaces table is empty and insert data if it is
    cursor.execute('SELECT COUNT(*) FROM Spaces')
    if cursor.fetchone()[0] == 0:
        cursor.execute(f'''
            INSERT INTO Spaces (
                SpaceID,
                SpaceName,
                Description,
                Category,
                Members
            )
            VALUES 
            (1, 'WE@Liberty', 'WE@Liberty strives to empower women.', 'US Employee Resource Groups', '{json.dumps([102, 103])}'),
            (2, 'LEADA', 'We imagine a world where Liberty Mutual is an employer of choice in the black community.', 'US Employee Resource Groups', '{json.dumps([104, 107, 108])}'),
            (3, 'Amigos@Liberty', 'We want to enhance understanding of the Hispanic/Latino culture.', 'US Employee Resource Groups', '{json.dumps([102, 106, 108])}'),
            (4, 'USRM Technology', '', 'Corporate Functions', '{json.dumps([105, 106])}'),
            (5, 'Women in Technology (WiT)', 'A space to network with women in technology.', 'US Employee Resource Groups', '{json.dumps([103, 109])}'),
            (6, 'Liberty IT', 'Welcome to the Liberty IT Communities space!', 'Corporate Functions', '{json.dumps([104, 105, 108])}'),
            (7, 'LIFTED Technology', 'This is home base for Technology employees.', 'Corporate Functions', '{json.dumps([104, 106])}'),
            (8, 'Liberty Torchbearers', 'Theres a Torchbearer in all of us!', 'Company Programs', '{json.dumps([101, 102, 103, 105, 109])}'),
            (9, 'Data Science @ Liberty', 'Data Science Professional Resource Group', 'Personal/Professional Interest', '{json.dumps([101, 107])}'),
            (10, 'Technology Learning', 'Drive continuous learning and relevant skill building.', 'Personal/Professional Interest', '{json.dumps([101, 107])}')
        ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
