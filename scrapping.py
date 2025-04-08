from youtube_comment_downloader import YoutubeCommentDownloader
import pandas as pd
import time

video_urls = [
    "https://www.youtube.com/watch?v=hzUG58aJ124",
    "https://www.youtube.com/watch?v=UJP8MMLcUBM",
    "https://www.youtube.com/watch?v=uMzaDzRUzqs",
]

downloader = YoutubeCommentDownloader()
all_comments = []

for url in video_urls:
    for sort_mode in [0, 1]:  # 0 = top, 1 = newest
        print(f"Scraping from: {url} | Sort: {sort_mode}")
        try:
            for comment in downloader.get_comments_from_url(url, sort_by=sort_mode):
                all_comments.append(
                    {
                        "video_url": url,
                        "author": comment["author"],
                        "text": comment["text"],
                        "time": comment["time"],
                    }
                )
                if len(all_comments) >= 26000:  # berhenti kalau udah cukup
                    break
        except Exception as e:
            print(f"Gagal ambil komentar dari {url}: {e}")
        time.sleep(1)
    if len(all_comments) >= 26000:
        break

# Simpan ke CSV
df = pd.DataFrame(all_comments)
df.to_csv("komentar_youtube_windah.csv", index=False, encoding="utf-8-sig")
print(f"Berhasil menyimpan {len(df)} komentar dari {len(video_urls)} video.")
