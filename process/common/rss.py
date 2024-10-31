from datetime import datetime, timezone

from feedgen.feed import FeedGenerator


def generate_rss():
    # Feed 생성
    fg = FeedGenerator()
    fg.title("My Blog RSS Feed")
    fg.link(href="https://www.alljum.com", rel="alternate")
    fg.description("올점에서 주역, 사주팔자, 타로, 이름학 등 다양한 운세와 전통 지혜를 만나보세요. 세계의 모든 운세를 통해 깊은 통찰과 자기 발견의 여정을 지원합니다.")
    fg.language("ko")

    # 데이터 항목 추가
    posts = [
        {"title": "올점에 대해", "link": "https://www.alljum.com/intro", "description": "올점에 대한 설명 입니다.", "pubDate":  datetime(2024, 10, 30, 12, 0, tzinfo=timezone.utc)},
        {"title": "무료 점괘", "link": "https://www.alljum.com/hexagram", "description": "무료 점괘를 통해 운세를 제공합니다.", "pubDate":  datetime(2024, 10, 30, 12, 0, tzinfo=timezone.utc)},
        {"title": "당사주", "link": "https://www.alljum.com/chizodiac", "description": "무료 당사주를 통해 운세를 제공합니다.", "pubDate": datetime(2024, 10, 30, 12, 0, tzinfo=timezone.utc)},
        {"title": "타로 운세", "link": "https://www.alljum.com/tarot", "description": "무료 타로 운세를 통해 운세를 제공합니다.","pubDate": datetime(2024, 10, 30, 12, 0, tzinfo=timezone.utc)},
        {"title": "매일 별자리 운세", "link": "https://www.alljum.com/dailystarzodiac", "description": "무료 별자리 운세를 매일 제공합니다.","pubDate": datetime(2024, 10, 30, 12, 0, tzinfo=timezone.utc)}
    ]

    for post in posts:
        fe = fg.add_entry()
        fe.title(post["title"])
        fe.link(href=post["link"])
        fe.description(post["description"])
        fe.pubDate(post["pubDate"])

    # RSS XML 생성
    rss_feed = fg.rss_str(pretty=True)
    return rss_feed
