# Curvex_Dashboard
interactive dashboard for Curvex written in Python using Plotly Dash library

The app.py file creates a basic layout of the app: a responsive header which has a dropdown menu to select from 3 pages, which then determine the rest of the layout and give different functionality to the dashboard. These pages are contained in a pages folder.
Mainpage.py lets you upload a file and based on the file it displays graphs. Freqinfo.py displays the information about the different frequencies. ADHDProbability.py lets you upload a file based on which the machine learning algoritm predicts if the user has ADHD or not.

The style of the dashboard is created using the style.css file in an assets folder.

The login_pseudocode.txt describes the ideal way of creating a Login for the dashboard using the Flask library in a form of a pseudocode.

File 17.csv is used as example values for the graphs, and the person.xlsx is used as example value for the prediction of ADHD. The Samlet_data.xlsx is used for the machine learning algorithm.
