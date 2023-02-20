#!/bin/sh

# Give some buffer time for app to finish set up
sleep 5
nginx -g 'daemon off;'
