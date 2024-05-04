# proyecto de ihc

## dependencies

### virtualenv

tener virtualenv installado y correr

```
$ virtualenv venv
$ source venv/bin/activate
```

luego installar requiramentos

```
$ pip3 install -r requirments.txt
```

## Correr proyecto

```
$ flask run
```

## setup db

```
CREATE TABLE Sugerencias(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name Text,
    email TEXT,
    asunto TEXT,
    mensaje TEXT
);
```
