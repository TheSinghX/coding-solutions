# SQLP186

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com

 **Case Study: Dotify Music App** 

- One of the Data Analyst at Dotify wants to look at things from user's perspective. He asks you to retrieve the name of user’s along with the count of singers (Non-Zero) they are following.
### Task
- Write a query to Retrieve the name of user’s along with the count of singers they are following as Total_count
### Expected Output Format

 **user_name** 
 **Total_count** 

### Description of Tables
- PK stands for Primary Key
- FK stands for Foreign Key
### Dataset tables
- User
- Song
- Singer
- Liked_by
- Follower
- Belongs_to
- Playlist

 **Expected Output** 

```
┌───────────────────┬─────────────┐
│     user_name     │ Total_count │
├───────────────────┼─────────────┤
│ Ajay Maheshwari   │ 3           │
│ Mahek Jain        │ 5           │
│ Camren Escobar    │ 1           │
│ Emelia Fritz      │ 3           │
│ Brogan Beasley    │ 1           │
│ Mikayla Dodson    │ 3           │
│ Taniya Rojas      │ 1           │
│ Taniya Rojas      │ 4           │
│ Erika Harris      │ 2           │
│ Jermaine Jarvis   │ 3           │
│ Salvatore Sweeney │ 1           │
│ Dominique Cohen   │ 2           │
│ Madilynn Mccoy    │ 1           │
│ Skylar Pham       │ 1           │
│ Tamara Li         │ 1           │
│ Alex Pineda       │ 1           │
└───────────────────┴─────────────┘

```

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-05T07:49:10.119Z  

```sql
SELECT
    U.user_name AS user_name,
    COUNT(F.singer_id) AS Total_count
FROM Follower F
JOIN User U ON U.user_id =F.user_id
GROUP BY F.user_id, U.user_name
ORDER BY F.user_id;
```

---

[View on CodeChef](https://www.codechef.com/problems/SQLP186)