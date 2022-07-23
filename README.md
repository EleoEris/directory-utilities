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
Work in progress (dead as of now)<br>
Might be usable to shred files, but hasn't been tested.
<!-- Shreds files in a secure way after the date you've set (it overwrites them with random bytes). Change values in shred_if variable at the end of the file datetime(year, month, day, hour, minute). <br/>
Be sure to make the file run after the log in. Putting it in __shell:startup__ (in windows) makes it run before the user is logged in, thus making it imposible to delete files.<br/>
You might want to create a scheduled task (check https://www.tenforums.com/tutorials/173596-how-create-task-run-app-script-logon-windows-10-a.html)

**Warning! Files might be recoverable but they shouldn't be. STILL NEEDS TESTING!** -->
