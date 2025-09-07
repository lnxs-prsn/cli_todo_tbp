

### **CLI Todo Project Blueprint**  
#### **0. Research & Discovery**  
- **Knowledge gaps:**  
  - Python’s `argparse`/`click` for CLI interactions X 
  - File handling (JSON/text) for task persistence   X
  - Best practices for CLI UX (colors, help text)    
- **References:**  
  - Python’s `argparse`/`click` documentation        X
  - Popular CLI todo apps (e.g., Taskwarrior) for inspiration  X
- **Validation:**  
  - Quick prototype: Can tasks be added/deleted via CLI?  X

#### **1. Objective**  
- **Core functionality:**  
  - Add/delete/list tasks  
  - Mark tasks as complete  
  - Save tasks between sessions  
- **Stretch goals:**  
  - Priority levels, due dates  
  - Search/filter tasks  

#### **2. Success Criteria**  
- **Must-have:**  
  - Tasks persist after program exit  
  - Basic CRUD operations work  
- **Nice-to-have:**  
  - Colored output, help flags  
  - Undo/error recovery  

#### **3. Phases & Steps**  
1. **Setup**  
   - Single-file structure (`todo.py`)  
   - Dependencies: `argparse` (or `click`), `json` for storage  

2. **Core Logic**  
   - Task storage: List of dictionaries (JSON file)  
   - Functions: `add_task()`, `delete_task()`, `list_tasks()`  

3. **User Interaction**  
   - CLI commands: `add "task name"`, `done 1`, `list`  
   - Input validation: Handle missing/duplicate tasks  

4. **Extras & Robustness**  
   - Auto-create storage file if missing  
   - Handle file corruption edge cases  

#### **4. Resources**  
- **Time:** 3-5 hours (research + MVP)  
- **Tools:** Python 3.10+, `argparse`, `json`  
- **Skills:** Basic Python, file I/O  

#### **5. Risks & Mitigations**  
- **Risk:** JSON file corruption → **Fix:** Backup file or switch to SQLite  
- **Risk:** Poor CLI UX → **Fix:** Use `click` for better help/colors  

