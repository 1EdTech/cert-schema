#!/usr/bin/env bash

# automate PR process to Blockcerts.org: update blockcerts-verifier dependency
GITHUB_COM=github.com
BLOCKCERTS_GITHUB_REPO=blockchain-certificates-web/blockchain-certificates-web.github.io
GIT_REPO=$GITHUB_COM/$BLOCKCERTS_GITHUB_REPO.git
WORK_BRANCH=feat/update-schemas
GITHUB_USER=botcerts

# clone CTS repo
git clone https://$GIT_REPO
cd blockchain-certificates-web.github.io

# rename remote to add authentication
git remote rm origin
git remote add origin https://$GITHUB_USER:$BOTCERTS_PR_GITHUB_TOKEN@$GIT_REPO

# run script from client repo
. scripts/update_blockcerts_schemas.sh

# open PR
#{
#  "title": "Amazing new feature",
#  "body": "Please pull this in!",
#  "head": "octocat:new-feature",
#  "base": "master"
#}

curl --data '{"head":"'${WORK_BRANCH}'", "base":"master", "title": "updatee Blockcerts Schemas", "body": "Please review and merge @lemoustachiste @raiseandfall"}' -H "Authorization: token ${BOTCERTS_PR_GITHUB_TOKEN}" https://api.github.com/repos/$BLOCKCERTS_GITHUB_REPO/pulls -v

# clean after use
cd ..
echo 'Delete working directory'
rm -rf blockchain-certificates.github.io
