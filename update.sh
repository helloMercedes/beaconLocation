#!/bin/sh

sed -i '/location\":/c\\"location\": \"'${1}'\"' /home/ubuntu/api/api/info.json
