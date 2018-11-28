#!/bin/bash
listfiles() {
 for i in "$1"/*;do
    if [ -d "$i" ];then
        echo "dir: $i"
        recurse "$i"
    elif [ -f "$i" ]; then
        echo "file: $i"
    fi
 done
}

listfiles $1