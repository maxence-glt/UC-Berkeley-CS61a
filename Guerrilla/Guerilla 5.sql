-- Guerilla 5 of UC Berkeley's cs61a spring 2020 course
-- https://inst.eecs.berkeley.edu/~cs61a/sp20/disc/guer05.pdf

CREATE TABLE people(name, age, state, hobby);

CREATE TABLE posts(post_id, poster, text, time);

CREATE TABLE likes(post_id, name, time);

CREATE TABLE requests(friend1, friend2);

-- 2.1
SELECT name, age
  FROM people
  WHERE age <= 26;

-- 2.2
SELECT poster, time
  FROM posts
  WHERE time <= 230

-- 2.3
SELECT a.name
  FROM posts AS a, likes AS b
  WHERE b.name = a.name AND a.posts = b.posts;

-- 2.4
CREATE TABLE friends AS
  SELECT a.friend1, a.friend2
    FROM requests AS a, requests AS b
    WHERE a.friend1 = b.friend2 AND a.friend2 = b.friend1;

-- 2.5
SELECT friend1
  FROM friends
  GROUP BY friend1
  HAVING COUNT(*) >= 4;

-- 2.6
SELECT a.state1
  FROM people as a, requests as b
  GROUP BY b.friend1
  HAVING b.friend1 = "Will"

-- impossible to test more complicated functions without any sample data
