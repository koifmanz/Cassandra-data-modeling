#------------------
# connect keyspace
#------------------

keyspace_create = """
    CREATE KEYSPACE IF NOT EXISTS sparkify 
    WITH REPLICATION = 
    { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }"""

#------------
# DROP TABLE
#------------

session_q_drop = "DROP TABLE IF EXISTS session_query"
user_q_drop = "DROP TABLE IF EXISTS user_query"
song_q_drop = "DROP TABLE IF EXISTS song_query"


#--------------
# CREATE TABLE
#--------------

session_q_create = """CREATE TABLE IF NOT EXISTS session_query 
(
sessionId int,
itemInSession int,
artist text,
song text,
length float,
PRIMARY KEY (sessionId, itemInSession)
)
"""

user_q_create = """CREATE TABLE IF NOT EXISTS user_query 
(
    userId int,
    sessionId int,
    itemInSession int,
    artist text, 
    song text, 
    firstName text, 
    lastName text,   
    PRIMARY KEY ((userId, sessionId), itemInSession)
)
"""

song_q_create = """CREATE TABLE IF NOT EXISTS song_query 
(
song text,
userID int,
firstName text,
lastName text,
PRIMARY KEY ((song), userID)
)
"""

#-----------------
# INSERT TO TABLE
#-----------------

session_q_insert = "INSERT INTO session_query (sessionId, itemInSession, artist, song, length) VALUES (%s, %s, %s, %s, %s)"
user_q_insert = "INSERT INTO user_query (userId, sessionId, itemInSession, artist, song, firstName, lastName) VALUES (%s, %s, %s, %s, %s, %s, %s)"
song_q_insert = "INSERT INTO song_query (song, userId, firstName, lastName) VALUES (%s, %s, %s, %s)"


#-------------------
# SELECT FROM TABLE
#-------------------

select_q_session = """
SELECT *
FROM session_query
WHERE sessionId=338 AND itemInSession=4
"""

select_q_user = """
SELECT *
FROM user_query
WHERE userID=10 AND sessionId=182
"""

select_q_song = """
SELECT *
FROM song_query
WHERE song='All Hands Against His Own'
"""