#!/bin/sh

exec gunicorn -w 2 -t 2 -b 0.0.0.0:${PORT:-8000} main:app
