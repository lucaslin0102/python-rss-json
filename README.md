[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=lucaslin0102_python-rss-json)](https://sonarcloud.io/summary/new_code?id=lucaslin0102_python-rss-json) [![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-white.svg)](https://sonarcloud.io/summary/new_code?id=lucaslin0102_python-rss-json)


# 📰 Medium RSS to JSON Converter

This Python script fetches blog posts from a given Medium RSS feed, converts them to JSON format using the API from [rss2json.com](rss2json.com), and prints relevant details about the posts.

## ⚙️ Prerequisites

- Python 3.x
- `requests` library

You can install the `requests` library using pip if you don't already have it:

```bash
pip install requests
```

## 🚀 Usage
- Save the script as `rss-json.py`.
- Replace the `rss_url` parameter in the `url` variable with your own Medium post RSS feed URL. For example, replace `rss_url=https://medium.com/feed/@lucaslin0102` with `rss_url=https://medium.com/feed/@your_username`.
```
url = 'https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@your_username'
```
- Run the script:
```
python rss-json.py
```

## 🔧 Functionality

The script contains the following functions:

`get_posts()`
This function fetches the blog posts from the Medium RSS feed URL by converting it to JSON using the `https://api.rss2json.com/v1/api.json` API. It returns the JSON response if successful, otherwise it returns None.

`main()`
This function calls `get_posts()` to fetch the blog posts, and then prints details including the feed title, feed URL, the number of blog posts, and details of each post such as title, link, author, and published date.

## 📄 Example Output
```
Title: Your Feed Title
Feed Url: Your Feed URL
Number of Blogs: X
Blogs:
# 1
Blog Title: Title of the first blog
Blog Link: Link to the first blog
Blog Author: Author of the first blog
Blog Published Date: Published date of the first blog
# 2
...
```

## ⚠️ Error Handling

The script handles errors gracefully and prints appropriate error messages if:

- The API request fails due to network issues.
- The API returns a non-200 status code.

## 🛠️ Code Analysis

The code has been analyzed using SonarCloud to ensure CLEAN CODE standard and to continue to report quality gate.