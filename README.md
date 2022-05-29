# Sample CRUD

[![Build Status](https://travis-ci.org/meysam81/SampleCRUD.svg?branch=master)](https://travis-ci.org/meysam81/SampleCRUD)
[![Coverage Status](https://coveralls.io/repos/github/meysam81/SampleCRUD/badge.svg)](https://coveralls.io/github/meysam81/SampleCRUD)

This repository is an example of a good coding practice for several reasons.

* It adheres to [Clean Architecture](https://medium.com/amerandish/clean-architecture-simplified-223f45e1a10),
and in result SOLID. ❤
* It has tests all over the place. 😊
* TODO: It has CI/CD integrated. 😍
* It uses [ORM](https://en.wikipedia.org/wiki/Object-relational_mapping) which
is optimized with the help of dozens of awesome developers. 🙏
* It uses different environments for deploying (e.g. dev, prod, test). 🎶
* It was written by a cool developer. Just kidding. Or am I? ©®😎
* It has README for lord's sake. ✔

The full story is explained
[right here](https://medium.com/python-in-plain-english/how-to-write-tests-for-your-python-web-app-f6c6993abe36).
Check it out for the explanation.

Also shout out to the [best guys out there](https://github.com/gothinkster/flask-realworld-example-app)
for sharing their knowledge with the rest of us. ™

## How to test the app?

There are proper tests in place to check the integrity of the app. In order to run the
automation tests, simply install and run `tox`.

If you're interested in seeing the app live in action, run the following command in your
terminal:

```bash
docker run --rm -p 8000:8000 ghcr.io/meysam81/sampleapp
```

And then, here are the URIs you can interact with the app:

| URI                           | Methods                  |
| ----------------------------- | ------------------------ |
| `/api/v1/books`               | `GET`, `POST`            |
| `/api/v1/books/<int:book_id>` | `GET`, `PATCH`, `DELETE` |
