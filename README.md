<h5 align="center">
    <img src="https://raw.githubusercontent.com/vsnthdev/flask-queue-sse/designs/header.png" alt="flask-queue-sse">
</h5>
<p align="center">
    <strong>
        A simple implementation of <a href="https://web.dev/eventsource-basics">Server-Sent Events</a> for <a
            href="https://flask.palletsprojects.com">Flask</a> that
        doesn't require Redis pub/sub.
    </strong>
</p>
<p align="center">
    <a target="_blank" rel="noopener" href="https://pypi.org/project/flask-queue-sse">
        <img src="https://img.shields.io/pypi/v/flask-queue-sse?style=flat-square" alt="">
    </a>
    <a target="_blank" rel="noopener" href="https://pypi.org/project/flask-queue-sse/#history">
        <img src="https://img.shields.io/pypi/dm/flask-queue-sse" alt="">
    </a>
    <a href="https://github.com/vsnthdev/flask-queue-sse/issues">
        <img src="https://img.shields.io/github/issues/vsnthdev/flask-queue-sse.svg?style=flat-square" alt="">
    </a>
    <a href="https://github.com/vsnthdev/flask-queue-sse/commits/main">
        <img src="https://img.shields.io/github/last-commit/vsnthdev/flask-queue-sse.svg?style=flat-square" alt="">
    </a>
</p>
<br>

<!-- header -->

**flask-queue-sse** is my first ever Python library. It implements the Server-Sent Events protocol using the built-in Python `Queue` class. Please read [why this package](#💡-why-this-package) before using it in production.

> Tweet to me <a target="_blank" rel="noopener" href="https://vas.cx/twitter">@vsnthdev</a>, I'd love to know your
experience of this project 😀

## 💡 Why this package

Most implementations of Server-Sent Events available in PyPi for Flask require having a Redis database. This is to support horizontal scaling.

This library targets projects that don't want to deploy Redis seperately to get SSE working, and aren't aiming to horizontally scale _(have multiple instances of your app running behind a load balancer)_.

## 💿 Installation

```
pip install flask-queue-sse
```

Python 3.10 and above is required.

<!-- quick start -->

<!-- docs to build the project -->

## 🏷️ Referrences

This library has been inspired by, and developed after consuming following resources:

1. [Server-sent events in Flask without extra dependencies](https://maxhalford.github.io/blog/flask-sse-no-deps)
2. [Why do I need redis?](https://github.com/singingwolfboy/flask-sse/issues/7)

<!-- footer -->

## 📰 License
> The **flask-queue-sse** project is released under the [Zlib license](https://github.com/vsnthdev/flask-queue-sse/blob/main/LICENSE.md). <br> Developed &amp; maintained By Vasanth Srivatsa. Copyright 2023 © Vasanth Developer.
<hr>

> <a href="https://vsnth.dev" target="_blank" rel="noopener">vsnth.dev</a> &nbsp;&middot;&nbsp;
> YouTube <a href="https://vas.cx/videos" target="_blank" rel="noopener">@VasanthDeveloper</a> &nbsp;&middot;&nbsp;
> Twitter <a href="https://vas.cx/twitter" target="_blank" rel="noopener">@vsnthdev</a> &nbsp;&middot;&nbsp;
> LinkedIn <a href="https://vas.cx/linkedin" target="_blank" rel="noopener">Vasanth Srivatsa</a>