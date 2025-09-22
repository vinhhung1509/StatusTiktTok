#!/usr/bin/env python3
import json, time, os
from datetime import datetime

UID_FILE = 'uids.txt'
OUT_FILE = 'data/views.json'

def get_views_for_uid(uid):
    """
    TODO: thay hàm này bằng cách lấy số view thật:
    - call API có authentication
    - hoặc scrape trang (cẩn thận rate-limit & legal)
    - return int view hoặc None nếu lỗi
    """
    # -- ví dụ giả: trả số ngẫu nhiên (thay chỗ này bằng logic thật) --
    import random
    return random.randint(0, 1000000)

def main():
    if not os.path.exists('data'):
        os.makedirs('data')
    uids = []
    with open(UID_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            s = line.strip()
            if s:
                uids.append(s)
    out = {}
    for uid in uids:
        try:
            v = get_views_for_uid(uid)
        except Exception as e:
            v = None
        out[uid] = {
            "views": v,
            "updated": datetime.utcnow().isoformat() + 'Z'
        }
        # optionally: small sleep to avoid rate limit
        time.sleep(1)
    with open(OUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("Wrote", OUT_FILE)

if __name__ == '__main__':
    main()
