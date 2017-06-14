

Finding duplicates
------------------


From : http://stackoverflow.com/questions/2594829/finding-duplicate-values-in-a-sql-table

SELECT
    name, email, COUNT(*) -- not mandatory, just let you know how many are there
FROM
    users
GROUP BY
    name, email
HAVING
    COUNT(*) > 1  -- this is where you query for multiple row


Removing duplicates
-------------------

From : http://stackoverflow.com/questions/22181875/how-to-remove-duplicates-in-a-table

+ example with ctid


  delete from join_table
  where ctid not in (select min(ctid)
                     from join_table
                     group by id1, id2);

-- > keeps one of the duplicate

An other way:

delete from document where
        (lang, version_id, path) in
            (select lang, version_id, path
             from document group by lang, version_id, path
             having count(*) > 1 )
        and ctid not in (select min(ctid)
            from document
            group by lang, version_id
            having count(*) > 1) ;

-- > This seems to be waylonger. am wondering which is better ?
On the one hand this seems pretty inelegant, but maybe acting on smallers sets can be better if there are very few duplicates.


Manipulating enums :
--------------------


select * from pg_enum;

delete from pg_enum where enumabel = 'foobar' -- and so on


delete from pg_enum
    where enumlabel = value_to_remove
    and enumtypid = (select oid from pg_type where typname = 'enum_type_name')

alter type enum_entity_status add value 'some_new_value' ;

Generate sql request with data:
-------------------------------


select 'update table scope set category=''category_' || name || ''' where name =''' || name || ''';' from scope;

where scope has an name attribute.

