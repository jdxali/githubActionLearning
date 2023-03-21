#!/bin/bash

function get_ticket_number() {
BRANCH_NAME=$GITHUB_HEAD_REF
readarray -d "-" -t arr <<< "$BRANCH_NAME"
AHA_TICKET_NUM="AHA Ticket : A-TOLP-${arr[1]}\n"
PR_TITLE="PR TITLE : ${github.event.pull_request.title}\n"
BRANCH_TITLE="BRANCH : ${GITHUB_HEAD_REF}\n"
echo "AHA_TICKET_NUM=$AHA_TICKET_NUM $PR_TITLE $BRANCH_TITLE" >> $GITHUB_ENV
echo $AHA_TICKET_NUM
}

get_ticket_number