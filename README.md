# Python - CFM Discord Bot

## Sections 
- [Description](#description)
    - [Endpoints](#endpoints)
- [Getting Started](#getting-started)
    - [Dependencies](#Dependencies/Libraries)
    - [Installing](#installing)
    - [Setting Up](#setting-up)
    - [Executing](#executing)
- [Author](#author)
- [License](#license)

---
## Description
This is a RESTful API made to enable users to track and store player game data such as; name, role, rank points, money in wallet, money in bank, and more. This API is created using Flask (Python) and MongoDB to store user data as JSON entries.

> This project is currently incomplete and more endpoints are planned to be added. This includes endpoints to get player names sorted by rank points, add new players, and more.


#### Endpoints
- `/accounts?user=<username>` - Fetches specefic player data when `user` argument is provided, or fetches all players data if no argument is found.
- `/transactions?user=<username>` - Fetches a json file of all in-game player transactions made by the user specified.
- `/transactions/make?to=<username>&from=<username>&amount=<money>` - Posts a new transaction to the database which logs the transactions sender, receiver and the amount (given as an integer).



---
## Getting Started

### Dependencies/Libraries
- Python >= 3.6.0
- dnspython==2.1.0
- flask==1.1.2
- pymongo==3.11.3
- python-dotenv==0.15.0
- Mac/Windows OS

<br />

### Installing 
```bash
$ git clone https://github.com/JugalBili/Game-Stats-API
```
Or you can download the zip directly from github. 

<br />


### Setting Up 
Since the private information such as the MongoDB server address, and database login information are stored as environmental variables, you must first create a `.env` file within the src folder.  

**Variables include the following:**
- DBPASS
- DBUSER
- DBSERVER


<br />


### Executing
To execute to program, open the zip file into an IDE of your choice, or use the following in the termial: 
```bash
python app.py
```
> **Make Sure** to run the command inside the src folder
<br />

> When run, the API will be started at the local home address 127.0.0.1:5000
---
## Author 
**Jugal Bilimoria**
<br />February 24st 2020

<br />Project was made as an exploration and a learning experience for the Flask library and the RESTful API system.

---
## License 


MIT License

Copyright (c) 2021 Jugal Bilimoria

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.