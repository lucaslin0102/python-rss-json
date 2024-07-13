import requests

def get_posts():
    url = 'https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@lucaslin0102'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()
            # print('Response:', posts)
            return posts
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

def main():
    posts = get_posts()

    if posts:        
        blogscount = len(posts["items"])
        print('Title:', posts["feed"]["title"])
        print('Feed Url:', posts["feed"]["url"])
        print('Number of Blogs:', blogscount)
        print('Blogs:')
        i=0
        while blogscount > 0:
            print('#', i+1)
            blog = posts["items"][i];
            print('Blog Title:', blog["title"])
            print('Blog Link:', blog["link"])
            print('Blog Author:', blog["author"])
            print('Blog Published Date:', blog["pubDate"])
            if blogscount == i+1:
             break
            i+=1
    else:
        print('Failed to fetch posts from API.')

if __name__ == '__main__':
    main()