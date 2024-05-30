from collections.abc import Iterable
import OrgIterator

class Organization(Iterable):
    def __init__(self,root):
        self.root = root

    def __iter__(self):
        return OrgIterator.OrgIterator(self.root)