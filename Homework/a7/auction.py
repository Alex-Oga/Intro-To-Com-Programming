# Assignment 7, Task 4
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
from typing import List
from typing import Set
from typing import Dict
class Bid:
    def __init__(self,bid_id: int,bidder_id: str,auction: str):
        self.bid_id = bid_id
        self.bidder_id = bidder_id
        self.auction = auction
    def placeBid(bidder_id):
        bidder_id.bidder_id = bidder_id
class Auction:
    def __init__(self, auction: str):
        self.auction = auction
def CSV2List(csvFilename: str) -> List[Bid]:
    reader = open(csvFilename,'r')
    lst = []
    for line in reader:
        lst.append(line)
def mostPopularAuction(bidList: List[Bid]) -> Set[Auction]:

def auctionWinners(bidList: List[Bid]) -> Dict[str, Auction]:
