25.8/ 30 min
    - read the task blue print and the task check list to find out where I left last time 
    as I was sick for 4 days and unable to continue the project-
    - I was in middle of researching the json files and how to use them to persist the to do tasks
    - added learning journal to make catch up from now on easier
    - added comments to the code so catching up and possible debugging becomes easier
    - began testing how to access data from json
      - I stored data as string or dictionary am guessing as string because when I try to print the dictionary as for loop 
      - I get only the first key as I stored it as {key: {values}}

27.8/ 30 min (added 30.8)
    - learned why I  got this result {key: {values}} because I used tuple method instead of using dictionary method if I want key,value pair dictionary I need to use .items() on dictionary so mostly same syntax as for tuples but adding items() method no the dictionary
    - I forgot to write the journal after coding session so most of the knowledge is vague but I succeeded printing stored dictionary and failed to edit the stored data.

30.8/ 30 min
    - previous days used to get training place so not much of progress for the project but as there was 3 days difference since last commit I can see if my journaling and logs are good enough to help me continue from where I left last time and do I achieve it shortest amount of time.
    - I had forgotten how to give cli arguments to argparse I gave buy milk buy milk from the store 2025-08-30 which led to error because now took every word as an argument what it wanted was this 'buy milk from the store' 2025-08-30 quotes on every argument so it knows where argument starts and ends the date gets automatically quotes either due to my lambda function or its default for the int type in argparse will look to it later
    - I was not able to continue where I left fast but I was able to progress coherently forward which is improvement from the time when I did not have logs or journal to help me.

31.8/ 30 min
    - I am trying in this session to get the edit_task() working on the terminal I can alter the loaded content from the json file but there does not seem to be clean way to edit the data on the file so far it appears that I need to get data from the file edit it and then save whole data back to file even if I want to just add one comma.
    - only solution is read all data edit what I need then append to all data and store whole junk again using 'w' other options would likely lead to errors with my present capacity
    - my goal is to load from the json file and edit then save it back but filesystem does not support such an solution so I need to read file to memory alter it then store back to file

02.9/ 10 min
    - lot to do today got myself 10 will use it to see if my present system can sustain quick drop ins or not
    - it was possible even though it took moment of orientation I solved what to print in case that file exists but its empty

03.9/ 30 min
    - now I can
      - get data from the json file,
      - deal with error that may rise when opening the file,
      - edit the data
      - write edited data back to file  
      - next is to edit data directly from the cli.
      - there are something called subparsers

4.9/ 23 min
    - Will research more about subparsers
    - I have to redo the code a bit there is way to do it easier and more structured way 
    - I should figure out how I can get this kind of knowledge sooner thou it appears that this is one of those learn by touching the stove things
    - adding global level parser and subparser.
    - alt+shift allows multi cursors in vscode

5.9/ 15 min
    - bit tired so very little progress expected
    - using sub parsers makes me do programming little bit different than am used to all the cli functionality will be outside the functions and functions manage only json file reading and writing
    - I just found out that something like match/case exists it came at python 3.10 its really good for my project
    - further searching and I found about set_default(func=function_name) this allows me to connect subparsers directly to functions so there is no if/else or match/case.
    - I would likely benefit if at the beginning of any project from now on I would have moment of looking how everything should flow so I would avoid these writing and rewriting the code so much

6.9/ 60 min
    - now I have to rereason bit how I will do the project I will also check how I have so far followed the task blue print and the checklist
    - my project managment side is lacking so far I have file called in_execution and I have not kept it up to date perhaps I have too much and I need to get rid of some parts 
    - made quick check with deepseek and it crushed my assumption that I was just doing something instead of following project documentation. I am following the blueprint and the checklist.  
    - there is just bit improvement to be done in the following check list that is to look at it beginning of every sessions so I wont be taken over by the "problems" of previous session.
    - so the blueprint is destination and the checklist is the compass to destination.
    - I dont seem to know how to read checklist anymore
    - correction I had not looked at it for so long that I forgot how to read it.
    - everything is as it should be
    - I used 35 min to do this assessment of the situation so far but now I can proceed with peace of mind
    - I will try to do this assessment periodically maybe every 10-15 days to see if am still on the correct path.
    - took care of few small details left in the #0 research and discovery now I know how taskwarrior looks like I jumped to work without looking around not good habit.
    - next is to refactor the code using set_default. 

7.9/ 60 min
    - I have began refactoring the code and adding the fucntionalities of delete, list, etc
    - maybe I should have planning file to avoid problems that arise because I do and then think.
    - ok now the add_task works as it should be and looks very professional
    - I achieved better solution than I planned by edit function edits the json file arbitrarily but it does it and I dont yet know how it does it
    - 