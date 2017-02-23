Python:

`git diff master --name-status | grep "^[AM]" | cut -c 3- | xargs pep8  | cut -d: -f 1 | sort | uniq | xargs autopep8 -i `
Get added or modified list | check for pep8 | get filenames | autopep8 them

`git diff master --name-status | grep "^[AM]" | cut -c 3- | xargs flake8 `



