import datetime
import json
from pprint import pprint

from engine.config import config
from requests_oauthlib import OAuth1Session

AK = config["twitter"]["api_key"]
AS = config["twitter"]["api_secret"]
AT = config["twitter"]["access_token"]
ATS = config["twitter"]["access_token_secret"]
twitter = OAuth1Session(AK, AS, AT, ATS)


def search_image(screen_name, post_id=None):
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    images = []

    params = dict(
        screen_name=screen_name, count=200, include_rts=False, exclude_replies=True
    )
    if post_id:
        params.update({"since_id": post_id})
    # params ={'screen_name':'_aopyun_', 'count' : 200, 'include_rts': False, 'exclude_replies': True}
    res = twitter.get(url, params=params)

    if res.status_code == 200:
        timelines = json.loads(res.text)
        id_flag = True
        for line in timelines:
            print(line["user"]["name"] + "::" + line["text"])
            print("*******************************************")
            created_at = datetime.datetime.strptime(
                line["created_at"], "%a %b %d %H:%M:%S %z %Y"
            )
            fname = created_at.strftime("%F/%T")
            if id_flag:
                post_id = line.get("id_str", post_id)
                id_flag = False
            if line.get("extended_entities"):
                # pprint.pprint(line)
                desc = (
                    line["created_at"]
                    + "\n"
                    + line["text"]
                    + "\ntweet_key: "
                    + line["id_str"]
                )
                for i, item in enumerate(line["extended_entities"].get("media")):
                    is_video = 0
                    title = line["id_str"] + "-" + str(i + 1)
                    url = item["media_url"] + ":orig"
                    if "video_info" in item:
                        is_video = 1
                        url = item["video_info"]["variants"][1]["url"]
                    images.append(
                        {
                            "url": url,
                            "title": title,
                            "description": desc,
                            "fname": fname,
                            "is_video": is_video,
                        }
                    )
    else:
        print("Failed: %d" % res.status_code)

    print(screen_name + ": " + str(datetime.datetime.now()))
    pprint(images)
    print("=" * 20)
    return post_id, images


if __name__ == "__main__":
    # print(config['twitter'].keys())
    search_image("_aopyun_")
