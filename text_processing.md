Vim and sed
============

Python replace `update['key'] = ` by `key: ` => s/update\[\('.*'\)\] =/\1:/g

    Insert simple quote with sed :
    -            [{u'description': u'View email address of the account',
    +            [{u'description': u'View the account\'s email address',

```find tests/ -name "*.py"  | xargs sed -i "s/email address of the account/the account\\\'s email address/"```

