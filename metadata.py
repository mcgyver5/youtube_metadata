import sys
import json
import requests
import re
import urllib.request

class Video_Metadata():
    youtube_url = ""
    title = ""
    pub_date = ""
    runtime = ""
    viewCount = ""
    likeCount = ""
    dislikeCount = ""
    commentCount = ""
    tags = []
# should have a constructor and a to_string and an equals
    def __init__(self,youtube_url,title,pub_date,runtime,viewCount,likeCount,dislikeCount,commentCount, tags):
        self.youtube_url = youtube_url
        self.title = title
        self.pub_date = pub_date
        self.runtime = runtime
        self.viewCount = viewCount
        self.likeCount = likeCount
        self.dislikeCount = dislikeCount
        self.commentCount = commentCount
        self.tags = tags
    def __str__(self):
        output = "{} {} Date Published: {} Runtime: {} likeCount: {} tag: {}".format(self.youtube_url,
                self.title, 
                self.pub_date, 
                self.runtime,
                self.likeCount,
                self.tags[0])
        return output

    def md_output(self):
        output = "1. **{0}** [{1}]({1}) runtime : {2} **Date Published** : {3} **Views** : {4} **Likes** : {5} **Comments**: {6} **tag**: {7}\n".format(self.title,self.youtube_url, self.runtime, self.pub_date, self.viewCount, self.likeCount, self.commentCount, self.tags[0])
        return output

def convertDate(ptFormat):
    answer = ""
    hh = re.search(re.compile("([0-9]*)H"),ptFormat)
    mm = re.search(re.compile("([0-9]*)M"),ptFormat)
    ss = re.search(re.compile("([0-9]*)S"),ptFormat)
    if hh: 
        answer = answer + hh.group(1) + ":"
    if mm: 
        answer = answer + mm.group(1) + ":"
    if ss: 
        answer = answer + ss.group(1) 

    return answer

def parse_out_video_id(youtube_url):
# https://www.youtube.com/watch?v=0v1kp2JTZMA
    tup = youtube_url.rsplit('=',1)
    video_id = tup[1].strip()
    return video_id

def get_video_list():
    video_list = []
    with open("test_video_links.txt") as vid_file:
        for video in vid_file:
            video_list.append(video.strip())
    return video_list

def get_data_from_api_url(api_key, video_id, part):
    api_url = f"https://www.googleapis.com/youtube/v3/videos?part={part}&id={video_id}&key={api_key}"
    
    result = urllib.request.urlopen(api_url)
    data = json.loads(result.read())
    return data['items'][0][part]

def get_metadata_object(api_key, video_url):
    attribute_map = {} 
    video_id = parse_out_video_id(video_url)
#   title and date
    data = get_data_from_api_url(api_key, video_id, 'snippet')
    pub_date = data['publishedAt']
    pub_date = pub_date.split('T')[0]
    tags = data['tags']
#   runtime
    detail_data = get_data_from_api_url(api_key, video_id, 'contentDetails')
    runtime = detail_data['duration']
    runtime = convertDate(runtime)
#   stats
    stats = get_data_from_api_url(api_key,video_id,'statistics')
    
    metadata_object = Video_Metadata(
            video_url,
            data['title'],
            pub_date,
            runtime,
            stats['viewCount'],
            stats['likeCount'],
            stats['dislikeCount'],
            stats['commentCount'],
            tags)
    return metadata_object

def run_lookup():
    video = None
    video_list = get_video_list()
    print(len(video_list))
    video_object_list = []
    with open("api_key.txt") as fh_key:
        api_key = fh_key.read()
            
    try:
        for v in video_list:
            video_metadata = get_metadata_object(api_key,v)
            video_object_list.append(video_metadata)
    except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_tb.tb_lineno)
            print(e)

    with open("video_info.md","w") as file_handle:
        for vmd in video_object_list:
            file_handle.write(vmd.md_output())
            print(vmd.md_output())


if __name__ == '__main__':
    run_lookup()
