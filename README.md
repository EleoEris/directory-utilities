# directory-utilities
## makeJSONtree
Creates a JSON tree of a folder.

<dl>
  <dt>makeJSONtree.Tree.tree</dt>
  <dd>json dictionary</dd>
  
  <dt>str(makeJSONtree.Tree)</dt>
  <dd>json.dumps of the tree</dd>
</dl>

## autoShredder
Shreds files in a secure way after the date you've set (it overwrites them with random bytes). Change values in shred_if variable at the end of the file datetime(year, month, day, hour, minute).

**Warning! Files might be recoverable but they shouldn't be. STILL NEEDS TESTING!**
