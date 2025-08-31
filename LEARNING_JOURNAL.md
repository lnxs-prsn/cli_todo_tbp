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