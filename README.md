# NASA Space Apps Challenge - Community Mapping

This web application leverages satellite imagery to track and visualize the impact of salinity on agricultural land in the Baixo Vouga Lagunar region of Aveiro. The platform is designed to help researchers, students, and local farmers identify high-risk areas, enabling them to take preventative measures to protect fertile soil and ensure sustainable land use.

## Features

- **Satellite Data Visualization**: Provides interactive maps using Sentinel-2 imagery to track salinity impact on agricultural areas of the Baixo Vouga Lagunar.
- **Spectral Indices**: Displays various spectral indices for better understanding of vegetation health and land cover.
- **User-Friendly Interface**: Accessible for farmers, students, and researchers, without requiring technical expertise.

## Getting Started

### Prerequisites

- Python 3.8+
- Virtual environment (optional but recommended)

### Installation

1. **Clone the repository**:

   git clone "repository-url
   
   cd repository-folder

3. **Create a virtual environment**:

   python3 -m venv env
   
   source env/bin/activate  # On Windows: env\Scripts\activate

5. **Install the required dependencies**:

   pip install -r requirements.txt

7. **Fetch the required data**:

   python down.py

   We will need to be logged into your account in Copernicus.

   This step might take a bit.
   
9. **Running the Application**:

   Start the FastAPI server:
   
   uvicorn serve:app --reload
   
   Access the web app locally.


## Usage

After running the app, users can interact with the web interface to view satellite data, explore various indices, and analyze salinity effects on agricultural land in the region. The application enables users to identify potential risk areas and make informed decisions to protect soil fertility.

## Limitations and Future Versions
Right now the app is only available locally and it will need to be deployed for maximum impact. 

The current version does not allow date selection for satellite data visualization. All data is pre-fetched for specific dates. 

In next versions we will have to upgrade the app to allow users to select specific dates and implement a cache system to store previously fetched satellite data, improving performance and reducing repeated API calls

## Contributors

André Dora

Cecília Santos

Raquel Vinagre

Rhania Rolo
