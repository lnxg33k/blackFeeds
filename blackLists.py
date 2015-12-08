#!/usr/bin/env python
# Written by Ahmed Shawky @lnxg33k

from requests import request
from datetime import datetime
# from json import dumps
from re import findall
import sys

from elasticsearch import Elasticsearch
from elasticsearch import helpers


def getBlackLists(blackType="domains"):
    blackLists = {
        "malc0de": {
            "url": "http://malc0de.com/bl/ZONES",
            "regex": r"zone\s+\"(.*?)\"\s*{",
            "type": "domains",
        },
        "malwaredomains": {
            "url": "http://mirror1.malwaredomains.com/files/domains.txt",
            "regex": r"\r\n(?:\#|)\t(?:\d+|)\t(.*?)\s+",
            "type": "domains",
        },
        "DGA": {
            "url": "http://osint.bambenekconsulting.com/feeds/dga-feed.txt",
            "regex": r"\n(.*?),Domain",
            "type": "domains"
        },
        "zeus": {
            "url": "https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist",
            "regex": r"([^#]*?)\n",
            "type": "domains"
        },
        "sans": {
            "url": "https://isc.sans.edu/feeds/suspiciousdomains_High.txt",
            "regex": r"\n(.*?)\t",
            "type": "domains"
        }
    }

    result = {}
    for k, v in blackLists.items():
        try:
            if not blackType:
                src = request("GET", url=v['url']).content
            else:
                if v['type'] == blackType:
                    src = request("GET", url=v['url']).content
            result[k] = {
                'data': filter(None, map(str.strip, findall(v['regex'], src))),
                'list_type': v['type']
            }
        except:
            pass
    return result


def main():
    if len(sys.argv) != 2:
        exit("[+] %s <Elasticsearch_Node>" % sys.argv[0])

    # blackLists elasticsearch node
    ELK = sys.argv[1].strip('/')

    now = datetime.now().strftime("%Y.%m.%d")
    index_name = "blacklists-%s" % now

    print "[+] Downloading blacklisted entries ..."
    maliciousEntries = getBlackLists(blackType=None)

    entries = []
    for k, v in maliciousEntries.items():
        for i in v['data']:
            action = {
                "_index": index_name,
                "_type": k,
                "_source": {"entry": i, "list_type": v['list_type']}
            }
            entries.append(action)

    print "[+] Pushing parsed entries to the blacklists index ...."

    es = Elasticsearch(ELK)

    mapping = {
        "mappings": {
            "_default_": {
              "properties": {
                "entry": {
                  "type": "string",
                  "index": "not_analyzed",
                  "doc_values": True
                },
                "list_type": {
                  "type": "string",
                  "index": "not_analyzed",
                  "doc_values": True
                }
              }
            }
        }
    }

    # Create mapping and push data to the index
    es.indices.create(index=index_name, ignore=400, body=mapping)
    helpers.bulk(es, entries, chunk_size=5000)

if __name__ == '__main__':
    main()
