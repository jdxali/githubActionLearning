#!/bin/bash

function get_ticket_number() {
BRANCH_NAME=$GITHUB_HEAD_REF
readarray -d "-" -t arr <<< "$BRANCH_NAME"
AHA_TICKET_NUM="A-TOLP-${arr[1]}"
echo "AHA_TICKET_NUM=$AHA_TICKET_NUM" >> $GITHUB_ENV
echo $AHA_TICKET_NUM
}

get_ticket_number