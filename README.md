# Crepery REST API

## Create and select virtual environment

### First create the virtual environment

```bash
python3 -m venv venv
```

### Then source it to activate

```bash
source venv/bin/activate
```

## Database migrations

### Go inside database folder

```bash
cd database
```

### Run the following command to see if there is any new migration version

```bash
pgmigrate -t 1 info
```

### Then run this command to start migrations

```bash
pgmigrate -t 1 migrate
```
