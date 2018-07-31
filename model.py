from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom

class SyscallTable(GraphObject):

    def __init__(self, index, name):
        super().__init__()
        self.index = index
        self.name = name

    # properties
    index = Property()
    name = Property()

    syscalls = RelatedTo("Syscall", "OWNS_SYSCALL")

class Syscall(GraphObject):

    def __init__(self, index, name, address):
        super().__init__()
        self.index = index
        self.name = name
        self.address = address

    # properties
    index = Property()
    name = Property()
    address = Property()

    owned_by = RelatedTo("SyscallTable", "OWNED_BY")
