#!/usr/bin/env python3

# sys
import os
import sys
import json
import logging

from model import SyscallTable, Syscall

# 3rd
from py2neo import Graph


__SCRIPT_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
DB_PASSWORD = 'admin'
TABLE_NAMES = {
    0: 'nt',
    1: 'win32k'
}


def init_logger(debug=False):
    logging_level = logging.INFO
    if debug:
        logging_level = logging.DEBUG
    logging.basicConfig(level=logging_level)
    # suppress annoying log output
    logging.getLogger("httpstream").setLevel(logging.WARNING)
    logging.getLogger("neo4j.bolt").setLevel(logging.WARNING)


def main():
    init_logger(debug=True)

    logging.info('connect to Neo4j DB')
    graph = Graph(password=DB_PASSWORD)

    logging.info('delete previous graph')
    graph.delete_all()

    with open('syscall-table.json') as f:
        sdt = json.load(f)

    logging.info('Inserting syscall table into database')
    for table_index, table in sdt:
        systable = SyscallTable(table_index, TABLE_NAMES[table_index])
        for index, name, address in table:
            syscall = Syscall(index, name, address)
            syscall.owned_by.add(systable)
            systable.syscalls.add(syscall)
            logging.info('Inserting syscall %s', (index, name, address))
            graph.push(syscall)
        graph.push(systable)



if __name__ == '__main__':
    main()
