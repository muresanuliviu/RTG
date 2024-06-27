import random
import tkinter as tk
from tkinter import messagebox


class RandomTeamGenerator:
  def __init__(self, root):
    self.root = root
    self.root.title("Random Team Generator")
    
    # Set up the UI
    self.label = tk.Label(root, text="Enter names (comma separated):")
    self.label.pack(pady=10)
    
    self.label = tk.Label(root, text="Urn 1:")
    self.label.pack()
    self.names1 = tk.Entry(root, width=100)
    self.names1.pack(pady=10)
    
    self.label = tk.Label(root, text="Urn 2:")
    self.label.pack()
    self.names2 = tk.Entry(root, width=100)
    self.names2.pack(pady=10)
    
    self.label = tk.Label(root, text="Urn 3:")
    self.label.pack()
    self.names3 = tk.Entry(root, width=100)
    self.names3.pack(pady=10)
    
    self.generate_button = tk.Button(root, text="Generate Teams", command=self.generate_teams)
    self.generate_button.pack(pady=10)
    
    self.result_label = tk.Label(root, text="")
    self.result_label.pack(pady=10)
    
  def generate_teams(self):
    names1 = self.names1.get().split(',')
    names1 = [name.strip() for name in names1 if name.strip()]  # Clean up names
    
    names2 = self.names2.get().split(',')
    names2 = [name.strip() for name in names2 if name.strip()]
    
    names3 = self.names3.get().split(',')
    names3 = [name.strip() for name in names3 if name.strip()]
    
    if len(names1) + len(names2) + len(names3) < 3:
        messagebox.showerror("Error", "Please enter at least 3 names.")
        return
    
    random.shuffle(names1)
    random.shuffle(names2)
    random.shuffle(names3)
    teams = [[], [], []]
    
    for i, name in enumerate(names1+names2+names3):
        teams[i % 3].append(name)
    
    result_text = "Team 1:\n" + ", ".join(teams[0]) + "\n\n"
    result_text += "Team 2:\n" + ", ".join(teams[1]) + "\n\n"
    result_text += "Team 3:\n" + ", ".join(teams[2])
    
    self.result_label.config(text=result_text)

if __name__ == "__main__":
  root = tk.Tk()
  app = RandomTeamGenerator(root)
  root.mainloop()
