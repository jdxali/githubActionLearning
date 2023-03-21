#!/bin/bash

function get_ticket_number() {
BRANCH_NAME=$GITHUB_HEAD_REF
readarray -d "-" -t arr <<< "$BRANCH_NAME"
AHA_TICKET_NUM="AHA Ticket : A-TOLP-${arr[1]}"
TICKET_INFO=$(printf "PR : ${GITHUB_PR_TITLE} \n  BRANCH NAME : ${BRANCH_NAME} \n")
echo "${TICKET_INFO}"
echo "AHA_TICKET_NUM=${TICKET_INFO}" >> $GITHUB_ENV
echo $AHA_TICKET_NUM
}

get_ticket_number