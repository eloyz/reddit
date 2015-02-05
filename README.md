# Scrapy Example

Scraping http://www.reddit.com for posts and images using Scrapy http://scrapy.org

First presented at the Houston Python Web Development Meetup group. http://www.meetup.com/python-web-houston/events/219729234/


## Use this code now
```
# Create a virtual environment
# mkvirtualenvwrapper must be installed
# not required, but nice to have
mkvirtualenv reddit

git clone https://github.com/eloyz/reddit.git

cd reddit
scrapy crawl pic
```

## Creating your own project
```
# Create virtual environment
# mkvirtualenvwrapper must be installed
# not required, but nice to have
mkvirtualenv reddit

# Install python packages
pip install scrapy service_identity ipython pillow
```

## Start a scrapy project
```
scrapy startproject reddit
```

At this point your `reddit` directory is created.

## Generating a spider
Go into the directory, give it a name, and specify it's domain.

```
cd reddit
scrapy genspider pic www.reddit.com
```

Now's a good time to initialize your git repo (e.g. repository).  Not required.
```
git init  # inside of the parent reddit directory
```

You can use this code as an example to help you get started as well as Scrapy's great documentation. http://doc.scrapy.org/en/0.24/