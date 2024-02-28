import tkinter as tk
from tkinter import scrolledtext, ttk
import requests
from bs4 import BeautifulSoup

def fetch_departure_info(url):
    departures = []  # List to store departure information
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors

        soup = BeautifulSoup(response.content, 'html.parser')
        departure_board = soup.find('ol', class_='departure-board')  # Use find to get the first ol if only one exists, otherwise find_all

        if departure_board:
            for item in departure_board.find_all('li', class_='departure-board__item'):  # Correct iteration over li elements
                service = item.find('div', class_='single-visit__name').text.strip() if item.find('div', class_='single-visit__name') else 'N/A'
                destination = item.find('div', class_='single-visit__description').text.strip() if item.find('div', class_='single-visit__description') else 'N/A'
                departure_time = item.find('div', class_='single-visit__arrival-time__cell').text.strip() if item.find('div', class_='single-visit__arrival-time__cell') else 'N/A'
                
                departures.append({'service': service, 'destination': destination, 'departure_time': departure_time})

        return departures
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None

def update_departures():
    url = "https://www.nctx.co.uk/stops/3390J6"  # URL to scrape
    departure_info = fetch_departure_info(url)
    departure_list.delete(1.0, tk.END)  # Clear current list
    if departure_info:
        for departure in departure_info:
            departure_list.insert(tk.END, f"{departure['service']} - {departure['destination']} at {departure['departure_time']}\n")
    else:
        departure_list.insert(tk.END, "Could not fetch departure information.")
    progress_bar['value'] = 0  # Reset progress bar after updating
    root.after(20000, update_departures)  # Schedule this function to be called again after 20,000 milliseconds
    update_progress_bar(20, 1000)  # Reset and start the progress bar update

def update_progress_bar(duration, interval):
    """
    Update the progress bar.
    :param duration: Total time to fill the progress bar in seconds.
    :param interval: Interval to update the progress bar in milliseconds.
    """
    step = 100 / (duration * 1000 / interval)  # Calculate step size
    current_value = progress_bar['value']
    new_value = current_value + step
    if new_value < 100:
        progress_bar['value'] = new_value
        root.after(interval, lambda: update_progress_bar(duration, interval))
    else:
        progress_bar['value'] = 100  # Optionally reset progress bar here or elsewhere

# Set up the GUI
root = tk.Tk()
root.title("Departure Information")

departure_list = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
departure_list.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

progress_bar = ttk.Progressbar(root, orient='horizontal', length=100, mode='determinate')
progress_bar.pack(padx=10, pady=10, fill=tk.X)

update_departures()  # Initial call to start the update process

root.mainloop()
