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

session_q_drop = "DROP TABLE IF EXISTS song_by_session"
user_q_drop = "DROP TABLE IF EXISTS song_by_user"
song_q_drop = "DROP TABLE IF EXISTS user_by_song"


#--------------
# CREATE TABLE
#--------------

session_q_create = """CREATE TABLE IF NOT EXISTS song_by_session 
(
sessionId int,
itemInSession int,
artist text,
song text,
length float,
PRIMARY KEY (sessionId, itemInSession)
)
"""

user_q_create = """CREATE TABLE IF NOT EXISTS song_by_user 
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

song_q_create = """CREATE TABLE IF NOT EXISTS user_by_song 
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

session_q_insert = "INSERT INTO song_by_session (sessionId, itemInSession, artist, song, length) VALUES (%s, %s, %s, %s, %s)"
user_q_insert = "INSERT INTO song_by_user (userId, sessionId, itemInSession, artist, song, firstName, lastName) VALUES (%s, %s, %s, %s, %s, %s, %s)"
song_q_insert = "INSERT INTO user_by_song (song, userId, firstName, lastName) VALUES (%s, %s, %s, %s)"


#-------------------
# SELECT FROM TABLE
#-------------------

select_q_session = """
SELECT song, artist, length
FROM song_by_session
WHERE sessionId=338 AND itemInSession=4
"""

select_q_user = """
SELECT artist, song, firstName, lastName
FROM song_by_user
WHERE userID=10 AND sessionId=182
"""

select_q_song = """
SELECT artist, song, firstName, lastName
FROM user_by_song
WHERE song='All Hands Against His Own'
"""