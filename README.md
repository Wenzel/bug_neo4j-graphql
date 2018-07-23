# bug_neo4j-graphql

## create the DB


    cd db/
    docker build -t neo4jdb .
    ./create_db.sh

## create `venv`

    virtualenv -p python3 venv
    source venv/bin/activate
    (venv) pip install py2neo

## run

    ./test.py
    
