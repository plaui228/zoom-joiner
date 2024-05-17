from tkinter import Tk, Label, Listbox, Button
import webbrowser
import os

filename = os.path.join("links.txt")

def read_meetings(filename):
  meetings = []
  try:
    with open(filename, 'r') as file:
      print("File opened successfully!")
      for line in file:
        data = line.strip().split(";")
        # Check if data has at least two elements (link and name)
        if len(data) >= 2:
          meeting = {"link": data[0], "name": data[1]}
          meetings.append(meeting)
          print(f"Read meeting: {meeting['name']}")
        else:
          print(f"Warning: Skipping invalid line: {line.strip()}")
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except PermissionError:
    print(f"Error: Insufficient permissions to access file '{filename}'.")
  except Exception as e:  # Catch other potential errors
    print(f"Error: An unexpected error occurred: {e}")
  return meetings


def open_meeting(listbox, window, meetings):
    # Get the selected meeting link
    selected_index = listbox.curselection()
    if selected_index:
        meeting = meetings[selected_index[0]]
        meeting_link = meeting["link"]
        webbrowser.open(meeting_link)
        print(f"Opening meeting link: {meeting_link}")
    else:
        print("Please select a meeting to join.")

def main():
    window = Tk()
    window.title("Zoom Meeting Joiner")

    # Label for listbox
    label = Label(window, text="Select a Meeting:")
    label.pack()

    listbox = Listbox(window, height=20, width=50)  # Adjust height and width as needed
    listbox.pack()

    # Button to open the selected meeting
    button = Button(window, text="Join Meeting", command=lambda: open_meeting(listbox, window, meetings))
    button.pack()

    label = Label(window, text="prog by plaui")
    label.pack()

    # Read meeting links from a file
    meetings = read_meetings(filename)

    if meetings:
        for meeting in meetings:
            listbox.insert("end", meeting["name"])
    else:
        print("No meeting data found in the file.")

    window.mainloop()

if __name__ == "__main__":
    main()
