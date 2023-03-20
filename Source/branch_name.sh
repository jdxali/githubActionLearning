#!/bin/bash

function get_ticket_number() {

BRANCH_NAME=$GITHUB_REF_HEAD
readarray -d "-" -t arr <<< "$BRANCH_NAME"
TICKET_NUM="A-TOLP-${arr[1]}"
echo "TICKET_NUM=$TICKET_NUM" >> $GITHUB_ENV
echo $TICKET_NUM
}

get_ticket_number