import json
import datetime
import pymysql
import redis
from fastapi import FastAPI
from fastapi.params import Query

app = FastAPI()
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def get_connection():
    return pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="q1w2e3",
        db="study",
        charset="utf8"
    )

def serialize_post(obj):
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    return obj

@app.get("/posts")
def get_posts(page: int = Query(1, ge=1), size: int = Query(10, le=100)):
    # 캐시 키 생성
    cache_key = f"posts:page{page}:size{size}"

    # 캐시 조회
    cached = redis_client.get(cache_key)
    total_cache = redis_client.get("posts:total")

    if cached and total_cache:
        print("📦 캐시에서 로딩")
        return {
            "page": page,
            "size": size,
            "total": total_cache,
            "posts": json.loads(cached)
        }

    # DB 연결
    conn = get_connection()
    cur = conn.cursor()

    # 총 개수 조회
    cur.execute("SELECT COUNT(*) FROM posts")
    total = cur.fetchone()[0]

    # 페이징 처리
    offset = (page - 1) * size
    cur.execute("SELECT id, title, created_at FROM posts ORDER BY created_at DESC LIMIT %s OFFSET %s", (size, offset))
    rows = cur.fetchall()

    # 튜플 → dict로 변환
    posts = [{"id": r[0], "title": r[1], "created_at": r[2]} for r in rows]

    cur.close()
    conn.close()

    # 캐싱
    redis_client.setex("posts:total", 1000, total)
    redis_client.setex(cache_key, 1000, json.dumps(posts, default=serialize_post))

    return {
        "page": page,
        "size": size,
        "total": total,
        "posts": posts
    }

# FastAPI 서버 실행 (터미널에서 직접 실행 시)
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("posts_web:app", host="0.0.0.0", port=8001, reload=True)
