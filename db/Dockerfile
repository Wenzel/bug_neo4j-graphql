FROM neo4j:latest

RUN apk update && apk add \
        git maven openjdk8
WORKDIR /var/lib/neo4j
RUN wget 'https://github.com/neo4j-graphql/neo4j-graphql/releases/download/3.4.0.1/neo4j-graphql-3.4.0.1.jar' -P plugins/
RUN echo 'dbms.unmanaged_extension_classes=org.neo4j.graphql=/graphql' >> conf/neo4j.conf
