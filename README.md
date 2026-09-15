# LiveBusTracker

A bus tracking application built with Python and FastAPI. The application allows users to view live bus locations and bus vehicle information.

<b>Try the app:<b/> [Click here](https://bustrackingapp-afh5.onrender.com)

## ✨ Features
- 🚌 View live bus locations
- 📍 Track buses on an interactive map
- 🔎 View bus and vehicle information
- 🌐 Web-based interface

## ⚙️ Installation

### 1. Clone the repository 
```
git clone https://github.com/niksbiedrins/BusTrackingApp.git
cd BusTrackingApp
```

### 2. Create a virtual environment
```python
python -m venv .venv
```
Activate the virtual environment:

<b>Windows</b>: ```venv\Scripts\activate```<br>
<b>macOS/Linux</b>: ```source venv/bin/activate```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Run the application
```
uvicorn src.main:app --reload
````
The application will be available at:
```
http://127.0.0.1:8000/
```
