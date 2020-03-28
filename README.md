# youtube_metadata
This script will take as imput a text file, remote github file, remote pastebin file.
It will then find all the youtube links in the file

This script then looks up title, length, username etc. of any given youtube URL.

It requires that the user create their own Google YouTube API key.

This is the info we get back from youtube from a part=snippet URL like the following:
https://www.googleapis.com/youtube/v3/videos?part=snippet&id=ve2pmm5JqmI&key={your_api_key}
you can see that there is no runtime in this one.

based on my reading of the docs, the API key has a limit of 1,000,000 units per day.
each time this script is run on one video, it takes 6 units.  so, you should be able to process roughly 160,000 video URLs per day with this. 

```
{
 "kind": "youtube#videoListResponse",
 "etag": "\"ksCrgYQhtFrXgbHAhi9Fo5t0C2I/EsNIrYZAY41gHlPRkEdbPGFrRUI\"",
 "pageInfo": {
  "totalResults": 1,
  "resultsPerPage": 1
 },
 "items": [
  {
   "kind": "youtube#video",
   "etag": "\"ksCrgYQhtFrXgbHAhi9Fo5t0C2I/W8dEfgHen39nddnTXcCCG9W--Ac\"",
   "id": "ve2pmm5JqmI",
   "snippet": {
    "publishedAt": "2015-12-23T17:30:01.000Z",
    "channelId": "UCCezIgC97PvUuR4_gbFUs5g",
    "title": "Python Tutorial: Automate Parsing and Renaming of Multiple Files",
    "description": "In this video we will be writing a quick script to automate the parsing and renaming of multiple files. Writing quick scripts to automate boring and repetitive tasks is a great way to learn Python and it is a great way to save time. Let's get started.\n\nThe code from this video can be found at:\nhttps://github.com/CoreyMSchafer/code_snippets/tree/master/Automation\n\n\n✅ Support My Channel Through Patreon:\nhttps://www.patreon.com/coreyms\n\n✅ Become a Channel Member:\nhttps://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g/join\n\n✅ One-Time Contribution Through PayPal:\nhttps://goo.gl/649HFY\n\n✅ Cryptocurrency Donations:\nBitcoin Wallet - 3MPH8oY2EAgbLVy7RBMinwcBntggi7qeG3\nEthereum Wallet - 0x151649418616068fB46C3598083817101d3bCD33\nLitecoin Wallet - MPvEBY5fxGkmPQgocfJbxP6EmTo5UUXMot\n\n✅ Corey's Public Amazon Wishlist\nhttp://a.co/inIyro1\n\n✅ Equipment I Use and Books I Recommend:\nhttps://www.amazon.com/shop/coreyschafer\n\n▶️ You Can Find Me On:\nMy Website - http://coreyms.com/\nMy Second Channel - https://www.youtube.com/c/coreymschafer\nFacebook - https://www.facebook.com/CoreyMSchafer\nTwitter - https://twitter.com/CoreyMSchafer\nInstagram - https://www.instagram.com/coreymschafer/\n\n#Python",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/ve2pmm5JqmI/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/ve2pmm5JqmI/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/ve2pmm5JqmI/hqdefault.jpg",
      "width": 480,
      "height": 360
     },
     "standard": {
      "url": "https://i.ytimg.com/vi/ve2pmm5JqmI/sddefault.jpg",
      "width": 640,
      "height": 480
     },
     "maxres": {
      "url": "https://i.ytimg.com/vi/ve2pmm5JqmI/maxresdefault.jpg",
      "width": 1280,
      "height": 720
     }
    },
    "channelTitle": "Corey Schafer",
    "tags": [
     "Python",
     "Python Tutorial",
     "Python Script",
     "Python File",
     "File Parsing",
     "Parse File",
     "Rename File",
     "Python Rename File",
     "Python os Module",
     "os module",
     "Python os",
     "Python for Beginners",
     "Learn Python",
     "Programming",
     "Computer Science",
     "Programming Tutorials",
     "Software Engineering"
    ],
    "categoryId": "27",
    "liveBroadcastContent": "none",
    "localized": {
     "title": "Python Tutorial: Automate Parsing and Renaming of Multiple Files",
     "description": "In this video we will be writing a quick script to automate the parsing and renaming of multiple files. Writing quick scripts to automate boring and repetitive tasks is a great way to learn Python and it is a great way to save time. Let's get started.\n\nThe code from this video can be found at:\nhttps://github.com/CoreyMSchafer/code_snippets/tree/master/Automation\n\n\n✅ Support My Channel Through Patreon:\nhttps://www.patreon.com/coreyms\n\n✅ Become a Channel Member:\nhttps://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g/join\n\n✅ One-Time Contribution Through PayPal:\nhttps://goo.gl/649HFY\n\n✅ Cryptocurrency Donations:\nBitcoin Wallet - 3MPH8oY2EAgbLVy7RBMinwcBntggi7qeG3\nEthereum Wallet - 0x151649418616068fB46C3598083817101d3bCD33\nLitecoin Wallet - MPvEBY5fxGkmPQgocfJbxP6EmTo5UUXMot\n\n✅ Corey's Public Amazon Wishlist\nhttp://a.co/inIyro1\n\n✅ Equipment I Use and Books I Recommend:\nhttps://www.amazon.com/shop/coreyschafer\n\n▶️ You Can Find Me On:\nMy Website - http://coreyms.com/\nMy Second Channel - https://www.youtube.com/c/coreymschafer\nFacebook - https://www.facebook.com/CoreyMSchafer\nTwitter - https://twitter.com/CoreyMSchafer\nInstagram - https://www.instagram.com/coreymschafer/\n\n#Python"
    },
    "defaultAudioLanguage": "en"
   }
  }
 ]
}
```
A part= contentDetail URL will get the runtime of the video
https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id=ve2pmm5JqmI&key={your_api_key}
```
{
 "kind": "youtube#videoListResponse",
 "etag": "\"ksCrgYQhtFrXgbHAhi9Fo5t0C2I/CeBtFO_ZBMDkJDfXg05wZso-llQ\"",
 "pageInfo": {
  "totalResults": 1,
  "resultsPerPage": 1
 },
 "items": [
  {
   "kind": "youtube#video",
   "etag": "\"ksCrgYQhtFrXgbHAhi9Fo5t0C2I/b62xyBfaK1O-p3XqydXHz0ww5HI\"",
   "id": "ve2pmm5JqmI",
   "contentDetails": {
    "duration": "PT12M34S",
    "dimension": "2d",
    "definition": "hd",
    "caption": "false",
    "licensedContent": true,
    "projection": "rectangular"
   }
  }
 ]
}
```
Finally, to get likes and dislikes, views and # of comments:
https://www.googleapis.com/youtube/v3/videos?part=statistics&id=ve2pmm5JqmI&key={your_api_key}

