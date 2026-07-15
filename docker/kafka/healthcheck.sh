#!/bin/bash

kafka-topics.sh \
--bootstrap-server localhost:9092 \
--list >/dev/null 2>&1

exit $?