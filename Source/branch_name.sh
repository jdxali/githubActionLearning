#!/bin/bash

function get_ticket_number() {

BRANCH_NAME=$GITHUB_REF_HEAD
readarray -d "-" -t arr <<< "$BRANCH_NAME"
AHA_TICKET_NUM="A-TOLP-${arr[1]}"
echo $AHA_TICKET_NUM
}

get_ticket_number