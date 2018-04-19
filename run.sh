#!/bin/bash
# Master script.

cd "$(dirname "$0")"
source ~/.virtualenvs/csi/bin/activate
exec uwsgi --ini uwsgi.cfg
