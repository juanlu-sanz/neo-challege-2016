#!/bin/bash

clear

echo 'Kill all processes'
echo '=================='
killall dnx


echo 'Fetching from git'
echo '================='

git pull origin master

echo 'Git pull done'

echo 'Deploying WI'
echo '============'

cd WebInterface/src/WebInterface
dnu restore
. ~/.dnx/dnvm/dnvm.sh
dnvm use default -r coreclr && dnu build --framework dnxcore50

tmux new-window -t $SESSION:1 -n 'DNX' 'dnx web'

tmux detach


cd ../../../
