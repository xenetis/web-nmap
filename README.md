# 📡 WEB NMAP

---

**Web-nmap** is a Python Flask project doing NMAP scan and display readable results.

## 🪪 Access

---

[http://localhost:5000/](http://localhost:5000/)

Login: **admin**

Password: **admin**


## 🏁 Docker-compose

---

````yaml
version: "3.5"
services:
  webnmap:
    image: xenetis/web-nmap:latest
    container_name: webnmap
    restart: always
    environment:
      - TZ=Europe/Paris
    ports:
      - "5000:5000"
    volumes:
      - "./webnmap:/src/_datas"
````

Or find it here: https://github.com/xenetis/docker-compose-examples/tree/main/web-nmap

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

## 🗃 Versions

---

### v0.4.0
- Add Socket.IO messages from thread scanner
- Add Bootstrap Toast messages 
- Add nb_scans on homepage

### v0.3.0
- Seeds for user, target and commands
- Nmap in Dockerfile
- Better display script part of Nmap scan
- Add rememberMe on Login
- Update my account

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

- Mariadb support
- Analyse JSON Nmap result
- Call API CVE Db with version retrieved from Nmap
- Crontab Nmap scan
- Add Nikto scan
- Add Dirsearch scan
- Add dependencies (CSS JS) inside project and Gulp these files
- Search bar 
- Delete button: conditional display
- Change datatables buttons from form post to ajax

## 🏗 Third Parts

---

- [Flask](https://palletsprojects.com/p/flask/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pyhton-Nmap](https://bitbucket.org/xael/python-nmap/src/master/)
- [Python-Socket IO](https://python-socketio.readthedocs.io/en/latest/)
- [Gulpjs](https://gulpjs.com/)
- [Jquery](https://www.jquery.com)
- [Getbootstrap](https://getbootstrap.com/)
- [Fontawesome](https://fontawesome.com/)
- [Docker](https://www.docker.com/)
