[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=lucaslin0102_python-rss-json)](https://sonarcloud.io/summary/new_code?id=lucaslin0102_python-rss-json) [![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-white.svg)](https://sonarcloud.io/summary/new_code?id=lucaslin0102_python-rss-json)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=lucaslin0102_python-rss-json&metric=bugs)](https://sonarcloud.io/summary/new_code?id=lucaslin0102_python-rss-json) [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=lucaslin0102_python-rss-json&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=lucaslin0102_python-rss-json) [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=lucaslin0102_python-rss-json&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=lucaslin0102_python-rss-json) [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=lucaslin0102_python-rss-json&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=lucaslin0102_python-rss-json)


# 📰 RSS to JSON Converter

This Python script converts RSS feeds to JSON format using either the [api.rss2json.com](api.rss2json.com) API or the 'feedparser' module, and prints relevant details about the posts.

## 🚀 Getting Started

### 📋 Prerequisites

- Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

### 📥 Installation

Clone the repository or copy the code to your local machine.

```sh
git clone https://github.com/lucaslin0102/python-rss-json.git
```

Install the required Python packages:

```sh
pip install requests feedparser argparse
```

## 🛠️ Usage

To use the script, you can run it with the following command:

```sh
python sources/rss_json.py [options] -f [feedurl]
```

### 🎛️ Options

* `api`: Use [api.rss2json.com](api.rss2json.com) to convert RSS to JSON.
* `feedparser`: Use `feedparser` module to convert RSS to JSON.

## 📡 Example

```sh
python sources/rss_json.py api -f https://medium.com/feed/@lucaslin0102
```
Example Output:
```sh
Selected RSS to JSON option: api
Title: Lucas Lin - Medium
Feed Url: https://medium.com/feed/@lucaslin0102
Number of Blogs: 10
Blogs:
# 1
Blog Title: My First Blog Post
Blog Link: https://medium.com/@lucaslin0102/my-first-blog-post
Blog Author: Lucas Lin
Blog Published Date: 2024-01-01T00:00:00Z
# 2
Blog Title: Another Interesting Post
Blog Link: https://medium.com/@lucaslin0102/another-interesting-post
Blog Author: Lucas Lin
Blog Published Date: 2024-02-01T00:00:00Z
...
```

or

```sh
python sources/rss_json.py feedparser -f https://medium.com/feed/@lucaslin0102
```
Example Output:
```sh
Selected RSS to JSON option: feedparser
Title: Lucas Lin - Medium
Feed Url: https://medium.com/feed/@lucaslin0102
Number of Blogs: 10
Blogs:
# 1
Blog Title: My First Blog Post
Blog Link: https://medium.com/@lucaslin0102/my-first-blog-post
Blog Author: Lucas Lin
Blog Published Date: 2024-01-01T00:00:00Z
# 2
Blog Title: Another Interesting Post
Blog Link: https://medium.com/@lucaslin0102/another-interesting-post
Blog Author: Lucas Lin
Blog Published Date: 2024-02-01T00:00:00Z
...
```

## 📚 Script Explanation

The script provides two functions to convert RSS to JSON:

* `post_rss_json(feedurl)`: Uses [api.rss2json.com](api.rss2json.com) to fetch and parse the RSS feed.
* `parse_rss_json(feedurl)`: Uses the `feedparser` module to fetch and parse the RSS feed.

### 🚦 Command-line Arguments

* `options`: Choose between 'api' or 'feedparser' for converting RSS to JSON.
* `-f`, `--feedurl`: (Optional) Specify the RSS feed URL. Default is `https://medium.com/feed/@lucaslin0102`.

## 🔍 Code Quality

This repository has been analyzed using SonarCloud to ensure CLEAN CODE standard and to continue to report quality gate.