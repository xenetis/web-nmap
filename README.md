# 📡 WEB NMAP

---

**Web-nmap** is a Python Flask project doing NMAP scan and display readable results

## 🛠 Local Setup

---

### Install requirement
````bash
pip3 install -r requirements.txt
````

### Local run
````bash
flask run --host=0.0.0.0 --port=5000
````

### Access

[http://localhost:5000/](http://localhost:5000/)


## 🗃 Versions

---

### v0.2.0

- Create and delete scan
- Display JSON Nmap result
- Arguments to Nmap command
- Add scanner in sidebar

### v0.1.0

- Flask framework
- Getbootstrap template
- SQLite support
- GulpJS JS & SCSS watch and build
- Dockerfile
- Create / delete / display targets in Db (IP / domain)
- Create / delete / display commands in Db
- Thread scanner start and stop
- Run nmap scan in a separate Thread
- Retrieve, save JSON Nmap result

## 🗺 Roadmap

---

- Seeds for targets and commands
- Mariadb support
- Analyse JSON Nmap result
- Call API CVE Db with version retrieved from NMAP
- Crontab Nmap scan
- Add Nikto scan
- Add dependencies (CSS JS) inside project and Gulp these files
- Add [Socket.IO](https://stackoverflow.com/questions/62173332/how-to-render-messages-in-real-time-flask-python) support to display the thread scanner status in navigation bar
- Search bar 
- Delete button: conditional display 
- Update my account

## 🏗 Third Parts

---

- [Flask](https://palletsprojects.com/p/flask/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Gulpjs](https://gulpjs.com/)
- [Jquery](https://www.jquery.com)
- [Getbootstrap](https://getbootstrap.com/)
- [Fontawesome](https://fontawesome.com/)
- [Docker](https://www.docker.com/)
