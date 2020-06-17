# Data modeling with apache cassandra

## Purpose 

In this project, I apply what I learned on data modeling with Apache Cassandra and complete an ETL pipeline using Python, for Udacity project. The goal is to create database for startup called Sparkify, for data analsys. The analysis team is particularly interested in understanding what songs users are listening to. 

___

## database schema

The scheme is denormalized tabels, with one table per select query, total of 3 tabels.

1. **Table 1** - created for getting song deatils - artist, length and title.
   
  ```SQL
SELECT 
    artist, song, length 
FROM 
    session_query 
WHERE 
    sessionId=338 AND itemInSession=4
 ```
 2.  **Table 2** - created for getting user deatils - name, song title, etc.
   
  ```SQL
SELECT 
    firstName, lastName, song, artist
FROM 
    user_query 
WHERE 
    userID=10 AND sessionId=182
 ```
1. **Table 3** - created for getting users list from specific song title.
   
  ```SQL
SELECT 
    firstName, lastName
FROM 
    song_query 
WHERE 
    song='All Hands Against His Own'
 ```
___

## ETL Pipeline

The pipeline work the follwing way:

1. All queries are in *sql_queries.py*.
2. *preprocessing.py* include a function for csv readering and writing.
3. *etl notebook* - the full process, creating the db, reading the csv and query them.
