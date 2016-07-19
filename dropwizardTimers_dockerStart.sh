#!/usr/bin/env bash

docker run -v /data/graphite:/data -p 80:80 -p 3000:3000 -p 2003:2003 -p 2004:2004 -p 7002:7002 -p 8125:8125/udp -p 8126:8126 -d samsaffron/graphite
