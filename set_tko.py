#-*- coding: utf-8 -*-

from dbConnect import ConnectClass
from datetime import datetime

class SetTko(object):

    def __init__(self):
        self.con = ConnectClass().get_connect()
        self.cur = self.con.cursor()
        self.cur.execute("select * from set_tko")
        rows = self.cur.fetchall()
        self.cur.close()
        self.con.close()
        col_names = ['type', 'name', 'blocks', 'interfaces']
        self.set_tko_cach = {}
        for i in rows:
            #self.set_tko_cach[i[0]] = {'type':i[1], 'name':i[2], 'blocks':i[3], 'interfaces':i[4]}
            self.set_tko_cach[i[0]] = {}
            for numb, c_name in enumerate(col_names):
                if i[numb+1] == None:
                    self.set_tko_cach[i[0]][c_name] = 'None'
                else:
                    self.set_tko_cach[i[0]][c_name] = i[numb+1]
        print "ОБНОВЛЕНИЕ КЭША ИЗ БАЗЫ", datetime.now()

    def create_set_tko(self, args):
        if type(args) == list or type(args) == tuple:
            list_data = args
            key_data = args[0]
            dict_data = {'type': args[1], 'name': args[2], 'blocks': args[3], 'interfaces': args[4]}
        elif type(args) == dict:
            list_data = [args['sn'], args['type'], args['name'], args['blocks'], args['interfaces']]
            key_data = args['sn']
            dict_data = {'type': args['type'], 'name': args['name'], 'blocks': args['blocks'], 'interfaces': args['interfaces']}
        elif type(args) == str:
            list_data = args.split('%')
            key_data = list_data[0]
            dict_data = {'type': list_data[1], 'name': list_data[2], 'blocks': list_data[3], 'interfaces': list_data[4]}
        else:
            return 'Wrong data type'

        try:
            self.con = ConnectClass().get_connect()
            self.cur = self.con.cursor()
            db_query = "INSERT INTO set_tko (sn, type, name, blocks, interfaces) VALUES {}".format(tuple(list_data))
            self.cur.execute(db_query)
            self.con.commit()
            self.cur.close()
            self.con.close()
        except:
            self.con = ConnectClass().get_connect()
            self.cur = self.con.cursor()
            db_query = "UPDATE set_tko SET type='{}', name='{}', blocks='{}', interfaces='{}' WHERE sn='{}'".format(list_data[1], list_data[2], list_data[3], list_data[4], list_data[0])
            self.cur.execute(db_query)
            self.con.commit()
            self.cur.close()
            self.con.close()

        self.set_tko_cach[key_data] = dict_data

        return True

    def read_set_tko(self, arg):
        try:
            if arg == '0':
                return self.set_tko_cach
            else:
                return self.set_tko_cach[arg]
        except:
            #raise Exception('Wrong serial number')
            #return 'Wrong serial number'
            return False

    def update_set_tko(self, args):
        pass
        return True

    def delete_set_tko(self, arg):
        if arg in self.set_tko_cach.keys():
            del self.set_tko_cach[arg]

            self.con = ConnectClass().get_connect()
            self.cur = self.con.cursor()
            db_query = "DELETE FROM set_tko WHERE sn = '{}'".format(arg)
            self.cur.execute(db_query)
            self.con.commit()
            self.cur.close()
            self.con.close()
            return True
        else:
            return False

#GG = SetTko()
#GG.create_set_tko(['sn3', 'TTTTTTTT', 'rwesd', '{"rter":"sdfs"}', '{"asdffffffff":"asdfadfa3weaq"}'])
