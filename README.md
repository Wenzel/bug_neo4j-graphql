# bug_neo4j-graphql

1. create the DB

    cd db/
    docker build -t neo4jdb .
    ./create_db.sh

2. create `venv`

    virtualenv -p python3 venv
    source venv/bin/activate
    (venv) pip install py2neo
