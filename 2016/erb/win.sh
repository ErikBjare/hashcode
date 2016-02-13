#!/bin/bash

function DOET() {
    python3 main.py < ../problemsets/${1}.in > answer_${1}_tmp.out

    echo $(tail -n 1 < answer_${1}_tmp.out)
    head -n -1 answer_${1}_tmp.out | wc -l > answer_${1}.out
    head -n -1 answer_${1}_tmp.out >> answer_${1}.out

    rm answer_${1}_tmp.out
}

DOET busy_day
DOET mother_of_all_warehouses
DOET redundancy

zip source.zip main.py classes.py util.py win.sh
