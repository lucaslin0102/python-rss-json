import requests
import feedparser
import argparse

def post_rss_json(feedurl):
    url = 'https://api.rss2json.com/v1/api.json?rss_url={feedurl}'

    try:    
        formattedurl = url.format(feedurl=feedurl)
        response = requests.get(formattedurl)

        if response.status_code == 200:
            response = response.json()
            # print('Response:', response)
            if response:        
                blogscount = len(response["items"])
                print('Title:', response["feed"]["title"])
                print('Feed Url:', response["feed"]["url"])
                print('Number of Blogs:', blogscount)
                print('Blogs:')
                i=0
                while blogscount > 0:
                    print('#', i+1)
                    blog = response["items"][i];
                    print('Blog Title:', blog["title"])
                    print('Blog Link:', blog["link"])
                    print('Blog Author:', blog["author"])
                    print('Blog Published Date:', blog["pubDate"])
                    if blogscount == i+1:
                        break
                    i+=1
            else:
                print('Failed to fetch response from API.')
        else:
            print('Error:', response.status_code)
    except requests.exceptions.RequestException as e:
        print('Error:', e)
    
def parse_rss_json(feedurl):
    
    try:
        response = feedparser.parse(feedurl)
        # print('Response:', response)
        if response:        
            blogscount = len(response["entries"])
            print('Title:', response["feed"]["title"])
            print('Feed Url:', response["feed"]["title_detail"]["base"])
            print('Number of Blogs:', blogscount)
            print('Blogs:')
            i=0
            while blogscount > 0:
                print('#', i+1)
                blog = response["entries"][i];
                print('Blog Title:', blog["title"])
                print('Blog Link:', blog["link"])
                print('Blog Author:', blog["author"])
                print('Blog Published Date:', blog["published"])
                if blogscount == i+1:
                    break
                i+=1
        else:
            print('Failed to parse the feed url.')
    except e:
         print('Error:', e)
        

def main():
    
    # Description of the arguments
    msg = "This script supports converting RSS to JSON using 'api.rss2json.com' or 'feedparser' module."
    
    # Initialize parser
    parser = argparse.ArgumentParser(description = msg)
    
    # Argument definitions
    parser.add_argument("options", choices=['api', 'feedparser'])
    parser.add_argument("-f", "--feedurl", nargs='?', default="https://medium.com/feed/@lucaslin0102")
        
    # Read arguments from command line
    args = parser.parse_args()
 
    print ("Selected RSS to JSON option: ", args.options)
    match args.options:
        case 'api': post_rss_json(args.feedurl)
        case 'feedparser': parse_rss_json(args.feedurl);
    
    
if __name__ == '__main__':
    main()