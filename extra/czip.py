from extra.xdbSearcher import XdbSearcher


def loadXdb():
    # 1. 预先加载整个 xdb
    dbPath = "./data/ip2region.xdb"
    cb = XdbSearcher.loadContentFromFile(dbfile=dbPath)

    # 2. 仅需要使用上面的全文件缓存创建查询对象, 不需要传源 xdb 文件
    searcher = XdbSearcher(contentBuff=cb)
    return searcher
