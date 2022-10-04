# -*- coding: utf-8 -*-

from dpa.server.Service import BaseService
from set_tko import SetTko


class API(BaseService):
    def __init__(self):
        super(API, self).__init__()

    def makeAPIDeclarations(self):
        self.declareAPI('API', ('create_set_tko',
                                'read_set_tko',
                                'update_set_tko',
                                'delete_set_tko',
                                ))

    def create_set_tko(self, args):
        return SetTko().create_set_tko(args)

    def read_set_tko(self, arg):
        return SetTko().read_set_tko(arg)

    def update_set_tko(self, args):
        return SetTko().update_set_tko(args)

    def delete_set_tko(self, args):
        return SetTko().delete_set_tko(args)
