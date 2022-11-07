[![Continuous Integration](https://github.com/nogibjj/SA_project3/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/SA_project3/actions/workflows/main.yml)

# Project 3: Query Spotify Popularity Database

The goal for this project is to create a script that use SQL command to query a database. I will be useing SQLite which is a self-contained and fast SQL fatabse engine. It is one of the most used database engines in the world and is built into countless devices and applications that people use every day. With SQLite I will build a database with a table containing data from `songs_normalize.csv` and execute SQL commands on this table to answer some insightful questions.

## Key Objective of Project

- Work in a cloud-based environment (Github Codespaces)
- Define some questions to answer: 
    1. How many songs did each artist release?
    2. What are the top 5 longest songs?
    3. What are the top 10 most popular songs?
    4. How many songs were released each year?
    5. Which year had the most songs release?
- Connect to a database. 
- Use queries to answer your questions.
- Build a command-line tool for users to execute queries. 

## Project Breakdown

![project3](https://user-images.githubusercontent.com/55010363/200214621-cc4e4fc7-882a-49e0-865a-6bf94aaa09ad.png)

## How to execute queries
To find the answer to one of these questions: 
- Clone project and open terminal
- `python3 create_db.py`
    - This will create the spotify database, if not already present in repo. 
- `python3 spotify_query.py`
    - Read Usage message to find what query you want to execute
- `python3 spotify_query.py {function}`
    - This will return the results of the query

