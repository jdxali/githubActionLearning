#!/bin/bash

function get_ticket_number() {

BRANCH_NAME=$GITHUB_REF_HEAD
readarray -d "-" -t arr <<< "$BRANCH_NAME"
export TICKET_NUM="A-TOLP-${arr[1]}"
echo $TICKET_NUM
}

get_ticket_number