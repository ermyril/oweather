#!/usr/bin/env sh

./main.py $@ \
    | awk 'BEGIN {print "| City | Temperature | \n |-|-:|"}
                 { print "|" $1 "|" $2 "|"}' \
    | pandoc -f markdown -o /output/result.pdf
