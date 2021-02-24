# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class FundrazorPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('funds.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""drop table if exists funds_tb""")
        self.curr.execute("""create table funds_tb(
                       campaignTitle text,
                       goal text,
                       currencyType text,
                       numberContributors text,
                       story text,
                       url text
                       )""")

    def process_item(self, item, spider):
        self.store_db(item)
        print("Pipeline :" + item['campaignTitle'][0:])
        return item

    def store_db(self, item):
        self.curr.execute("""insert into funds_tb values(?,?,?,?,?,?)""", (
            item['campaignTitle'][0:],
            item['goal'][0:],
            item['currencyType'][0],
            item['numberContributors'][0],
            item['story'][0:],
            item['url'][0]
        ))
        self.conn.commit()





