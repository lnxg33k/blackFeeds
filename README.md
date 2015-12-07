# blackFeeds
List of malicious domains to be indexed in ELK.

##Requirements:
  * Java to run ELK
```
  sudo add-apt-repository ppa:webupd8team/java
  sudo apt-get update
  sudo apt-get install oracle-java7-installer
```
  * Elasticsearch Node
    * `echo "deb http://packages.elastic.co/elasticsearch/2.x/debian stable main" | sudo tee -a /etc/apt/sources.list.d/elasticsearch-2.x.list
sudo apt-get update && sudo apt-get install elasticsearch`

  * elasticsearch python module
    * `pip install elasticsearch`

##To use:
  * Make Sure you have Elasticsearch node up and running
```
❰lnxg33k❙~❱✔≻ curl -XGET localhost:9200
{
  "name" : "Sleeper",
  "cluster_name" : "shawkya-dev",
  "version" : {
    "number" : "2.1.0",
    "build_hash" : "72cd1f1a3eee09505e036106146dc1949dc5dc87",
    "build_timestamp" : "2015-11-18T22:40:03Z",
    "build_snapshot" : false,
    "lucene_version" : "5.3.1"
  },
  "tagline" : "You Know, for Search"
}
```
  * python blackLists.py \<Node\>
    * e.x. `python blackLists.py localhost:9200`

##Result:
```
❰lnxg33k❙~❱✔≻ curl -XGET "10.53.32.206:9200/blacklists-2015.12.07/_search?&pretty" 
{
  "took" : 3,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "failed" : 0
  },
  "hits" : {
    "total" : 715087,
    "max_score" : 1.0,
    "hits" : [ {
      "_index" : "blacklists-2015.12.07",
      "_type" : "DGA",
      "_id" : "AVF8J6-HO3g39X4KKmUE",
      "_score" : 1.0,
      "_source":{"entry": "1x0eiu07jpjsy112iw01wepy7a.com", "list_type": "domains"}
    }, {
      "_index" : "blacklists-2015.12.07",
      "_type" : "DGA",
      "_id" : "AVF8J6-HO3g39X4KKmUI",
      "_score" : 1.0,
      "_source":{"entry": "1dc2tc31vmm00ercb6710obogu.com", "list_type": "domains"}
    }, {
      "_index" : "blacklists-2015.12.07",
      "_type" : "DGA",
      "_id" : "AVF8J6-HO3g39X4KKmUM",
      "_score" : 1.0,
      "_source":{"entry": "pk2qtk1qtaed31t8h0zb1dn4j2p.com", "list_type": "domains"}
    }, {
      "_index" : "blacklists-2015.12.07",
      "_type" : "DGA",
      "_id" : "AVF8J6-HO3g39X4KKmUO",
      "_score" : 1.0,
      "_source":{"entry": "r4jo7t1kuf02a1utuvqxyfzi2n.biz", "list_type": "domains"}
    }, {
      "_index" : "blacklists-2015.12.07",
      "_type" : "DGA",
      "_id" : "AVF8J6-HO3g39X4KKmUP",
      "_score" : 1.0,
      "_source":{"entry": "jd5texlnw7te16n7ai41hw8ffu.org", "list_type": "domains"}
    }, {
      "_index" : "blacklists-2015.12.07",
      "_type" : "DGA",
      "_id" : "AVF8J6-HO3g39X4KKmUR",
      "_score" : 1.0,
      "_source":{"entry": "mupk6bxlsop1pglb9s1snt4jg.net", "list_type": "domains"}
    }, {
      "_index" : "blacklists-2015.12.07",
      "_type" : "DGA",
      "_id" : "AVF8J6-HO3g39X4KKmUW",
      "_score" : 1.0,
      "_source":{"entry": "134s9wzd15iwzo8zvwq1kalmvu.biz", "list_type": "domains"}
    }, {
      "_index" : "blacklists-2015.12.07",
      "_type" : "DGA",
      "_id" : "AVF8J6-HO3g39X4KKmUf",
      "_score" : 1.0,
      "_source":{"entry": "1vwzhcq1yu3fqdnaj5tkqw7u2z.net", "list_type": "domains"}
    }, {
      "_index" : "blacklists-2015.12.07",
      "_type" : "DGA",
      "_id" : "AVF8J6-HO3g39X4KKmUi",
      "_score" : 1.0,
      "_source":{"entry": "cc3g8c1jcyt92gwrz301c155qx.biz", "list_type": "domains"}
    }, {
      "_index" : "blacklists-2015.12.07",
      "_type" : "DGA",
      "_id" : "AVF8J6-HO3g39X4KKmUj",
      "_score" : 1.0,
      "_source":{"entry": "p70tppdbzb8f14ol2bwtoxnf1.net", "list_type": "domains"}
    } ]
  }
}
```
