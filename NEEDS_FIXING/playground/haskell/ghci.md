
# GHCI

Glasgow Haskell Compiler Interactive Read-Eval-Print Loop.

<br>

## Useful Commands 
---

<br>

repeat last command
<pre> : </pre>

<br>

multiline command
<pre> :{\n ..lines.. \n:}\n </pre>       

<br>

display the names defined by module [mod] (!: more details; *: all top-level names)
<pre> :browse[!] [[*] [mod]] </pre>

<br>

change directory to [dir]
<pre>:cd [dir] </pre>                   

<br>

display information about the given names (!: do not filter instances)
<pre> :info[!] [[name] ...]</pre>

<br>

show the kind of [type] (!: also print the normalised type)
<pre> :kind[!] [type] </pre>      

<br>

load module(s) and their dependents (!: defer type errors)
<pre> :load[!] [*][module] ... </pre>

<br>

run the main function with the given arguments
<pre> :main [[argument] </pre>

<br>

reload the current module set (!: defer type errors)
<pre> :reload[!] </pre>      

<br>

show the type of [expr]
<pre> :type [expr] </pre>      

<br>

remove module(s) from the current target set
<pre> :unadd [module] </pre>      

<br>

run the shell command [command]
<pre> :![command] </pre>      

<br>

show the current imports, modules, search paths, etc
<pre> :show [imports/modules/path/...] </pre>
