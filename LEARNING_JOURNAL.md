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

8.9/ 24 min
    - I used nargs='?' as parser expects fixed order led to situation that user would need to write every argument or the first argument would have taken what ever was given.
    - solution might be dest which directs? while in reality it renames but not yet clear.

9.9/ 30 min 
    - I have resolved the other fields but date field is still an problem 
    - if I make it optional I need to resolve possible errors I will check the docs if there is some easy solution
    - ok it was actually lot easier I just keep using lambda in the type=  
    - next I need to check if there is none received from the argparse and in that case ensure that it will not replace the stored data will likely use the new thing I learned match/case

11.9/ 30 min
    - yesterday searching trainee positions.
    - scheduled this bit wrong prayer is happening soon so likely lot less than 30 min
    - lots of problems 

12.9/ 10 min
    - got extra shift so the 60 intended turned to 10 min
    - goal is to solve how to turn the argparser str output to dict so 
    - success I just put what ever the function receives from argparser which is object to vars() which converts it to dict

13.9  30 min
    - today I hope to finally have working edit_task function after which the project should come to fast conclusion 
    - as I have then solved most of the data flow processess between different part of the project 
    - I learned from this experience to figure out the project bit parts and how they interact if I figure that out at the planning stage I think I can finnish projects faster
    - right know 
      - am trying to iterate throught the args received from the argparser
      - see if there is None in the args in that case i will replace None with value from the json data
  - I was too ambitious I found out I know what I need to do and generally know how to do it but unfortunately I dont know how to do it specificaly
  - I really need the course to polish my fundamentals 

14.9/ 30 min
    - I figured out last time that I need to get inner dict in my json file. I used nested dict to separate different tasks in file.
    - in coherent day realized that I over complicated simple thing

15.9/ 27 min
    - I already know arguments function takes. All I need to do is just simple if/elif/else statement
    - its true what its said that beginners cannot see the forest from the woods 
    - ok it took longer than 27 min intended but now I have stored edited data to json file everything is hard coded right now so next I need to figure out how not to hard code everything 

19.9/ 9 min
    - very little time I missed this.


20.9/ 30s
    - too little time but I kept the momentum going.

21.9/ 60 min
    - finally back now I have to resolve how can I access stored data without hardcoding I have been asking AI to guide me withoug giving solutions
      - my initial design was flawed 
        - json.dump({f'{args.task_name}':{'task_name':f'{task_name}', 'task_description':f'{task_description}', 'end_date':f'{end_date}'}}
        - above leads to situation  where I need to hardcode the key of the outer dict or build system where the user gives the name of the task which they want to edit
        - option 1 is senseless and option 2 scope is lot bigger than intended despite being from human perspective intuitive its very challenging for the computer
      - solution I will make list of dict and use one key value of the dict to find out 
      - I also have to go and fix my add_task function
        - it does not have capacity to append tasks it 'w' which overwrites contents of file if it exists else creates a new file
  

22.9/ 5 min
    - very short moment
    - now I need to open the file get the list append it and store it back to file which will likely use the 'w' or 'w+' 
  

23.9/ 15 min
    -  continue from yesterday now I can append the list but if I append the json file throws an error after adding the second file 
       -  reason there is no comma between data dicts in the list
  
24.9/ 1 min
    - not much I have been planning through out the day about the project I dont understand why it did not show the appended list in the json file previously

25.9/ 5 min
    - made the add task function work 

26.9/ 60 min
    - next to fix the edit_task function so the user can find specific task from the list of tasks 
    - best approach is likely to first loop the list and then see if value is in the dicts
    - I will do this intuitively or impulsively this time but I intend to learn a way to do this with structure
    - editing specific task is now possible 
    - resolved the problem in the main() 
      - I specifically called each function add,edit etc which led to all of them running but I found out that set_defaults does it for me so it was unnessessary
    - next task is to do the task_list func
      - list fuction is ready
    - next is delete function
  
27.9/ 30 min
    - solving how to delete dict that is inside list
      - i can locate first the dict storing the task using a loop and then locate its index that way
      - but I will see if there are other easier ways to do delete the task
      - solution was to find the correct dict and use remove() on the list
    - next is done_task()
      - I have problem deciding how to do it
        - create new file 
          - that stores all the done tasks and allow user to manually move them to done file
        - keep same file and add new field done
          - then after task is marked done move to bottom of the tasks so there would be clear distinction 

28.9/ 60 min
    - today I will continue figuring out which solution to problem I should choose I will apply what I said I would in 26.9
      - structured way to decide solution to problem
        - how should I implement done functionality to the todo project
          - 1. add new field called done and edit it using the edit_task()
            - fast and easy all I have to do is just call the delete_task() if user edits the field
          - 2. create done file and add done flag to cli it would move task to different file where the user could access all the past tasks
            - more effort and might go beyond the scope of my present learning goal (over engineering)
      - solution
        - option 1 for now its easy to expand later if I decide to learn something more it can even become my expand further project
    - done functionality is added now I have completed the project



here are the evaluations of sr devs (gpt) and (deepseek)
Overall Assessment (gpt)

Structured Thinking: ✅ Your learning journal closely mirrors blueprint and checklist. You tracked gaps → solutions → testing → reflection.

Project Execution: ✅ Iterative, aligned with MVP, clear reasoning behind design choices.

Improvements:

Could explicitly mark each journal entry with checklist item references (0.A, 1.B, etc.) for easier auditing.

Could summarize lessons learned per milestone to reinforce reflection.


 Overall Assessment: (deepseek)



### **Project Execution (The Gap)**
- **Process discipline** - consistently using your tools
- **Session planning** - intentional focus each work period
- **Progress validation** - regularly checking against milestones
- **Scope management** - resisting distraction by interesting problems

## **Evidence from Your Journal:**

**Good Architecture Thinking:**
- *"I should figure out how everything should flow"* (9/5)
- *"subparsers makes me do programming little bit different than am used to"* (9/5)
- *"realized that I over complicated simple thing"* (9/14) - **this shows architectural reflection**

**Project Execution Gaps:**
- *"I dont seem to know how to read checklist anymore"* (9/6)
- *"I had not looked at it for so long"* (9/6)
- *"problems of previous session"* taking over (9/6)
- Many sessions starting by continuing yesterday's problem vs. planned next step

## **The Irony:**

You actually **had a great project management system** (blueprint + checklist) but didn't consistently **execute** using that system. 
This is like having a perfect roadmap but occasionally driving without checking it.





personal reflections 


for a first time doing any project like this.
  - I liked how I was constantly knowing what I was doing and why I was doing 
    - many of my previous projects died out due to project running off course 
    - it was pleasant to have project finished as intended instead of it turning to frankenstains monster
  - I have to improve how often I visit the checklist and blueprint 
    - I will likely create process which will force 5 min visit in the begining
  - this project succeeded because the CI (comanders intent was present constantly)
    - I want to get better at this.
  - 