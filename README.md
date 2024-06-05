# Yongsen Mao Website

This is my personal website.

# Installation
```bash
pip install pelican
pip install ghp-import 
```

# Build the Website
```bash
pelican content # build the static website
pelican --listen # visualize locally
ghp-import output -b gh-pages # update the gh-pages
git push origin gh-pages # push to remote gh-pages
```