class Clock:
    def __init__(self, initial_time: str):
        self.initial_time = initial_time
        self.dct = dict()
        a, b = self.initial_time.split(':')
        self.dct['hour'] = int(a)
        self.dct['minutes'] = int(b)
    def forward(self, minutes: int):
        self.dct['minutes'] += minutes
        if self.dct['minutes']>59:
            self.dct['hour'] += self.dct['minutes']//60
            self.dct['minutes'] = self.dct['minutes']%60
        self.dct['hour'] = self.dct['hour']%12
        hour = self.dct['hour']
        min = self.dct['minutes']
        self.initial_time = f'{hour}:{min}'
    def rewind(self, minutes: int):
        self.dct['minutes'] -= minutes
        if self.dct['minutes'] < 0:
            self.dct['hour'] += self.dct['minutes'] // 60
            self.dct['minutes'] = self.dct['minutes'] % -60
            self.dct['minutes'] += 60
        self.dct['hour'] = (self.dct['hour'] % 12)
        hour = self.dct['hour']
        min = self.dct['minutes']
        self.initial_time = f'{hour}:{min}'
    def get_hour(self) -> int:
        self.a,self.b = self.initial_time.split(':')
        return int(self.a)
    def get_minute(self) -> int:
        return int(self.b)
    def reset(self):
        self.initial_time = '00:00'
clock = Clock('01:01')
clock.reset()  # should be 0:00
clock.forward(2423) # should be 4:23
print(clock.get_hour())
print(clock.get_minute())
# from typing import List
# def mirror(L:List[str]) -> List[str]:
#     newlist = []
#     for i in L:
#         newlist.append(i[::-1])
#     return newlist[::-1]
# assert mirror(['IwDd', 'MosF']) == ['FsoM', 'dDwI']
# assert mirror(['vCeq', 'kfCX']) == ['XCfk', 'qeCv']
# assert mirror(['mEYupO', 'BneBDtn']) == ['ntDBenB', 'OpuYEm']
# assert mirror(['PN', 'QrzYyo', 'ezVQAaD']) == ['DaAQVze', 'oyYzrQ', 'NP']
# assert mirror(['IgwY', 'x', 'aqKjcB']) == ['BcjKqa', 'x', 'YwgI']
# assert mirror(['reW', 'zRU', 'PKEkFG']) == ['GFkEKP', 'URz', 'Wer']
# assert mirror(['lSHRa', 'ec', 'ISChRT', 'YOiRlYmV']) == ['VmYlRiOY', 'TRhCSI', 'ce', 'aRHSl']
# assert mirror(['ifjtvyed', 'DdmrRu', 'rj', 'DnBhH']) == ['HhBnD', 'jr', 'uRrmdD', 'deyvtjfi']
# assert mirror(['pgrPla', 'O', 'NDPKcZv', 'YrEQ']) == ['QErY', 'vZcKPDN', 'O', 'alPrgp']
# assert mirror(['JLIu', 'biswRx', 'zOdVoHe', 'jQhj', 'hxbCQm']) == ['mQCbxh', 'jhQj', 'eHoVdOz', 'xRwsib', 'uILJ']
# assert mirror(['GQOJni', 'IJutRtVq', 'BnDt', 'p', 'L']) == ['L', 'p', 'tDnB', 'qVtRtuJI', 'inJOQG']
# assert mirror(['VCCQdr', 'cXDN', 'a', 'CQrXNjF', 'c']) == ['c', 'FjNXrQC', 'a', 'NDXc', 'rdQCCV']
# assert mirror(['MOhSf', 'vHUejETA', 'qa', 'wnPY', 'oU', 'PklU']) == ['UlkP', 'Uo', 'YPnw', 'aq', 'ATEjeUHv', 'fShOM']
# assert mirror(['Cicm', 'gLHa', 'GiKQEi', 'hc', 'NKTNMfrz', 'Sdh']) == ['hdS', 'zrfMNTKN', 'ch', 'iEQKiG', 'aHLg', 'mciC']
# assert mirror(['RHdgt', 'pkUyP', 'jYTWTOv', 'p', 'ypEpm', 'jMkFCFm']) == ['mFCFkMj', 'mpEpy', 'p', 'vOTWTYj', 'PyUkp', 'tgdHR']
# assert mirror(['WbWmv', 'o', 'HqcWy', 'qLQ', 'XYDNqd', 'QtflQbxE', 'y']) == ['y', 'ExbQlftQ', 'dqNDYX', 'QLq', 'yWcqH', 'o', 'vmWbW']
# assert mirror(['w', 'o', 'y', 'Fzg', 'ASQ', 'rxUnRMsz', 'WkH']) == ['HkW', 'zsMRnUxr', 'QSA', 'gzF', 'y', 'o', 'w']
# assert mirror(['toAHcdHg', 'W', 'sDOxNsix', 'pXiXCVey', 'NW', 'gIdRDrwy', 'WeJ']) == ['JeW', 'ywrDRdIg', 'WN', 'yeVCXiXp', 'xisNxODs', 'W', 'gHdcHAot']
# assert mirror(['WTIG', 'VAWlSdx', 'ak', 'TkHiJ', 'HKLRp', 'mi', 'J', 'EhMj']) == ['jMhE', 'J', 'im', 'pRLKH', 'JiHkT', 'ka', 'xdSlWAV', 'GITW']
# assert mirror(['FtlilkFB', 'YdkwZeKq', 'Qaa', 'cjroOk', 'pOmujXL', 'wSyuoK', 'ssHBY', 'QjT']) == ['TjQ', 'YBHss', 'KouySw', 'LXjumOp', 'kOorjc', 'aaQ', 'qKeZwkdY', 'BFkliltF']
# assert mirror(['y', 'HB', 'qnC', 'KnigfARZ', 'XatlNiG', 'dTNwNfR', 'nYJ', 'Yaldy']) == ['ydlaY', 'JYn', 'RfNwNTd', 'GiNltaX', 'ZRAfginK', 'Cnq', 'BH', 'y']
# assert mirror(['TGmYPS', 'SjoZxlaF', 'WOQptCue', 'QCwScSO', 'FcZexw', 'edfYDy', 'orZnl', 'iHGs', 'YLgTj']) == ['jTgLY', 'sGHi', 'lnZro', 'yDYfde', 'wxeZcF', 'OScSwCQ', 'euCtpQOW', 'FalxZojS', 'SPYmGT']
# assert mirror(['SNblNA', 'MsxKvV', 'AQG', 'Bdbt', 'mpWvYk', 'Rt', 'tI', 'jwbUo', 'ScHa']) == ['aHcS', 'oUbwj', 'It', 'tR', 'kYvWpm', 'tbdB', 'GQA', 'VvKxsM', 'ANlbNS']
# assert mirror(['OLzfD', 'WgzyyT', 'UAeKgq', 'JEXUe', 'mjboFkh', 'HY', 'HLs', 'VyDe', 'svR']) == ['Rvs', 'eDyV', 'sLH', 'YH', 'hkFobjm', 'eUXEJ', 'qgKeAU', 'TyyzgW', 'DfzLO']

# from typing import List
# from typing import Dict
# def shopping(shopping_list: Dict[str, int], stores: List[Dict[str, dict]]) -> float:
#     stock = dict()
#     for i in stores:
#         for j in i:
#             stock[j] = 0
#     return stock
# print(shopping({ "beef":1, "milk":2},
# [ { "bread": { "stock": 10, "price": 2 },
#     "eggs": { "stock": 4, "price": 2 },
#     "milk": { "stock": 2, "price": 1.5 } },
#   { "bread": { "stock": 10, "price": 1.5 },
#     "eggs": { "stock": 10, "price": 2.5 },
#     "milk": { "stock": 5, "price": 2 },
#     "oreo": { "stock": 10, "price": 4 } } ]))