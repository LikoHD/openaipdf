from supabase import create_client, Client
import os

def query_and_store_book_records(file_name, file_type, word_count, page_count, books):
    # 连接到Supabase数据库
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)

    # 插入查询记录
    query_record = supabase.table("query_records").insert({
        "file_name": file_name,
        "file_type": file_type,
        "word_count": word_count,
        "page_count": page_count,
        "total_books_mentioned": len(books)
    }).execute()

    query_id = query_record.data[0]['id']

    # 插入结果明细
    for book_name, data in books.items():
        supabase.table("result_details").insert({
            "query_id": query_id,
            "book_name": book_name,
            "mention_count": data['count'],
            "pages": ','.join(map(str, data['pages']))
        }).execute()

    print("查询记录和结果明细已成功存储到数据库中。")

# 示例使用
file_name = "示例书籍.pdf"
file_type = "pdf"
word_count = 50000
page_count = 200
books = {
    "书籍1": {"count": 5, "pages": [1, 15, 30, 45, 60]},
    "书籍2": {"count": 3, "pages": [10, 25, 40]},
    "书籍3": {"count": 2, "pages": [20, 35]}
}

query_and_store_book_records(file_name, file_type, word_count, page_count, books)