import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import random
from repositories import note_repo, user_repo
from utility import display_utils

class MongoNotesGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MongoNotes Display")
        self.root.geometry("900x650")
        
        # Create notebook with tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create tabs
        self.random_note_tab = ttk.Frame(self.notebook)
        self.random_user_tab = ttk.Frame(self.notebook)
        self.all_notes_tab = ttk.Frame(self.notebook)
        self.all_users_tab = ttk.Frame(self.notebook) 
        self.note_by_id_tab = ttk.Frame(self.notebook)
        self.user_by_id_tab = ttk.Frame(self.notebook)
        
        # Add tabs to notebook
        self.notebook.add(self.random_note_tab, text="Random Note")
        self.notebook.add(self.random_user_tab, text="Random User")
        self.notebook.add(self.all_notes_tab, text="All Notes")
        self.notebook.add(self.all_users_tab, text="All Users")
        self.notebook.add(self.note_by_id_tab, text="Note by ID")
        self.notebook.add(self.user_by_id_tab, text="User by ID")
        
        # Setup tabs
        self.setup_random_note_tab()
        self.setup_random_user_tab()
        self.setup_all_notes_tab()
        self.setup_all_users_tab()
        self.setup_note_by_id_tab()
        self.setup_user_by_id_tab()
        
        # Initially load data
        self.display_random_note()
        self.display_random_user()
        self.display_all_notes()
        self.display_all_users()
    
    def setup_random_note_tab(self):
        # Create text area for note display
        self.random_note_display = scrolledtext.ScrolledText(self.random_note_tab, wrap=tk.WORD, 
                                                      width=80, height=30)
        self.random_note_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Create refresh button
        self.note_refresh_btn = ttk.Button(self.random_note_tab, text="Get Random Note", 
                                          command=self.display_random_note)
        self.note_refresh_btn.pack(pady=10)
    
    def setup_random_user_tab(self):
        # Create text area for user display
        self.random_user_display = scrolledtext.ScrolledText(self.random_user_tab, wrap=tk.WORD, 
                                                      width=80, height=30)
        self.random_user_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Create refresh button
        self.user_refresh_btn = ttk.Button(self.random_user_tab, text="Get Random User", 
                                          command=self.display_random_user)
        self.user_refresh_btn.pack(pady=10)
    
    def setup_all_notes_tab(self):
        # Create controls frame
        controls_frame = ttk.Frame(self.all_notes_tab)
        controls_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Add refresh button
        refresh_btn = ttk.Button(controls_frame, text="Refresh Notes", 
                               command=self.display_all_notes)
        refresh_btn.pack(side=tk.LEFT, padx=5)
        
        # Create text area for notes display
        self.all_notes_display = scrolledtext.ScrolledText(self.all_notes_tab, wrap=tk.WORD, 
                                                    width=80, height=30)
        self.all_notes_display.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
    
    def setup_all_users_tab(self):
        # Create controls frame
        controls_frame = ttk.Frame(self.all_users_tab)
        controls_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Add refresh button
        refresh_btn = ttk.Button(controls_frame, text="Refresh Users", 
                               command=self.display_all_users)
        refresh_btn.pack(side=tk.LEFT, padx=5)
        
        # Create text area for users display
        self.all_users_display = scrolledtext.ScrolledText(self.all_users_tab, wrap=tk.WORD, 
                                                    width=80, height=30)
        self.all_users_display.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
    
    def setup_note_by_id_tab(self):
        # Create search frame
        search_frame = ttk.Frame(self.note_by_id_tab)
        search_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Add ID label and entry
        id_label = ttk.Label(search_frame, text="Note ID:")
        id_label.pack(side=tk.LEFT, padx=5)
        
        self.note_id_entry = ttk.Entry(search_frame, width=10)
        self.note_id_entry.pack(side=tk.LEFT, padx=5)
        
        # Add search button
        search_btn = ttk.Button(search_frame, text="Find Note", 
                              command=self.find_note_by_id)
        search_btn.pack(side=tk.LEFT, padx=5)
        
        # Bind Enter key to search function
        self.note_id_entry.bind('<Return>', lambda event: self.find_note_by_id())
        
        # Create text area for note display
        self.note_by_id_display = scrolledtext.ScrolledText(self.note_by_id_tab, wrap=tk.WORD, 
                                                     width=80, height=30)
        self.note_by_id_display.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
    
    def setup_user_by_id_tab(self):
        # Create search frame
        search_frame = ttk.Frame(self.user_by_id_tab)
        search_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Add ID label and entry
        id_label = ttk.Label(search_frame, text="User ID:")
        id_label.pack(side=tk.LEFT, padx=5)
        
        self.user_id_entry = ttk.Entry(search_frame, width=10)
        self.user_id_entry.pack(side=tk.LEFT, padx=5)
        
        # Add search button
        search_btn = ttk.Button(search_frame, text="Find User", 
                              command=self.find_user_by_id)
        search_btn.pack(side=tk.LEFT, padx=5)
        
        # Bind Enter key to search function
        self.user_id_entry.bind('<Return>', lambda event: self.find_user_by_id())
        
        # Create text area for user display
        self.user_by_id_display = scrolledtext.ScrolledText(self.user_by_id_tab, wrap=tk.WORD, 
                                                     width=80, height=30)
        self.user_by_id_display.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
    
    def display_random_note(self):
        # Get all notes and choose randomly
        all_notes = list(note_repo.get_all())
        if not all_notes:
            self.random_note_display.delete(1.0, tk.END)
            self.random_note_display.insert(tk.END, "No notes found in database.")
            return
        
        # Select random note
        random_note = random.choice(all_notes)
        
        # Display formatted note
        self.random_note_display.delete(1.0, tk.END)
        formatted_note = display_utils.format_note(random_note)
        self.random_note_display.insert(tk.END, formatted_note)
        
        # Add note ID to title for reference
        self.notebook.tab(0, text=f"Random Note (ID: {random_note.get('_id', 'N/A')})")
    
    def display_random_user(self):
        # Get all users and choose randomly
        all_users = list(user_repo.get_all())
        if not all_users:
            self.random_user_display.delete(1.0, tk.END)
            self.random_user_display.insert(tk.END, "No users found in database.")
            return
        
        # Select random user
        random_user = random.choice(all_users)
        
        # Display formatted user
        self.random_user_display.delete(1.0, tk.END)
        formatted_user = display_utils.format_user(random_user)
        self.random_user_display.insert(tk.END, formatted_user)
        
        # Add user ID to title for reference
        self.notebook.tab(1, text=f"Random User (ID: {random_user.get('_id', 'N/A')})")
    
    def display_all_notes(self):
        # Get all notes
        all_notes = list(note_repo.get_all())
        
        # Clear display
        self.all_notes_display.delete(1.0, tk.END)
        
        if not all_notes:
            self.all_notes_display.insert(tk.END, "No notes found in database.")
            return
        
        # Display notes count
        self.all_notes_display.insert(tk.END, f"Found {len(all_notes)} notes:\n\n")
        
        # Display all notes
        for note in all_notes:
            formatted_note = display_utils.format_note(note)
            self.all_notes_display.insert(tk.END, formatted_note)
            self.all_notes_display.insert(tk.END, "\n" + "-"*50 + "\n")
    
    def display_all_users(self):
        # Get all users
        all_users = list(user_repo.get_all())
        
        # Clear display
        self.all_users_display.delete(1.0, tk.END)
        
        if not all_users:
            self.all_users_display.insert(tk.END, "No users found in database.")
            return
        
        # Display users count
        self.all_users_display.insert(tk.END, f"Found {len(all_users)} users:\n\n")
        
        # Display all users
        for user in all_users:
            formatted_user = display_utils.format_user(user)
            self.all_users_display.insert(tk.END, formatted_user)
            self.all_users_display.insert(tk.END, "\n" + "-"*50 + "\n")
    
    def find_note_by_id(self):
        # Get note ID from entry
        try:
            note_id = int(self.note_id_entry.get())
        except ValueError:
            messagebox.showerror("Invalid ID", "Please enter a valid numeric ID")
            return
        
        # Find note
        note = note_repo.get_by_id(note_id)
        
        # Clear display
        self.note_by_id_display.delete(1.0, tk.END)
        
        # Display note or message if not found
        if note:
            formatted_note = display_utils.format_note(note)
            self.note_by_id_display.insert(tk.END, formatted_note)
            self.notebook.tab(4, text=f"Note ID: {note_id}")
        else:
            self.note_by_id_display.insert(tk.END, f"Note with ID {note_id} not found.")
            self.notebook.tab(4, text="Note by ID")
    
    def find_user_by_id(self):
        # Get user ID from entry
        try:
            user_id = int(self.user_id_entry.get())
        except ValueError:
            messagebox.showerror("Invalid ID", "Please enter a valid numeric ID")
            return
        
        # Find user
        user = user_repo.get_by_id(user_id)
        
        # Clear display
        self.user_by_id_display.delete(1.0, tk.END)
        
        # Display user or message if not found
        if user:
            formatted_user = display_utils.format_user(user)
            self.user_by_id_display.insert(tk.END, formatted_user)
            self.notebook.tab(5, text=f"User ID: {user_id}")
        else:
            self.user_by_id_display.insert(tk.END, f"User with ID {user_id} not found.")
            self.notebook.tab(5, text="User by ID")

def launch_gui():
    """Launch the MongoNotes GUI"""
    root = tk.Tk()
    app = MongoNotesGUI(root)
    root.mainloop()

if __name__ == "__main__":
    launch_gui()