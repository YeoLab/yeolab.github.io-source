#!/usr/bin/env bash
BRANCH=master
TARGET_REPO=YeoLab/yeolab.github.io.git
PELICAN_OUTPUT_FOLDER=output

echo -e "Testing travis-encrypt"
echo -e "$VARNAME"

if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
    echo -e "Starting to deploy to Github Pages\n"
    if [ "$TRAVIS" == "true" ]; then
        git config --global user.email "travis@travis-ci.org"
        git config --global user.name "Travis"
    fi
    #using token clone gh-pages branch
    mkdir built_website
    #go into directory and copy data we're interested in to that directory
    cd built_website
    git init
    git pull https://${GH_TOKEN}@github.com/$TARGET_REPO > /dev/null
    rsync -rv --exclude=.git  ../$PELICAN_OUTPUT_FOLDER/* .
    cp ../CNAME .
    #add, commit and push files
    git add -f .
    git commit -m "Travis build $TRAVIS_BUILD_NUMBER pushed to Github Pages"
    # git remote set-url origin https://${GH_TOKEN}@github.com/gbic-ucsd/gbic-ucsd.github.io-source.git
    git push -f https://${GH_TOKEN}@github.com/$TARGET_REPO $BRANCH > /dev/null
    echo -e "Deploy completed\n"
fi
