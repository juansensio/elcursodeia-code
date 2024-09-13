from fasthtml.common import *
import joblib
import pandas as pd


model = joblib.load("my_model.pkl")
pipeline = joblib.load("my_pipeline.pkl")

app, rt = fast_app(
    pico=False,
    hdrs=(
        Link(rel='stylesheet', href='styles.css', type='text/css'),
))

@dataclass
class FormData:
    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    population: float
    households: float
    median_income: float
    ocean_proximity: str

@rt('/')
def get():
    return Div(
        Div(
            H1("House price predictor 🏠"),
            Form(
                Label("Longitude:"),
                Input(type="number", name="longitude", placeholder="Longitude", step="any", value="-121.89"),
                Label("Latitude:"),
                Input(type="number", name="latitude", placeholder="Latitude", step="any", value="37.29"),
                Label("Housing Median Age:"),
                Input(type="number", name="housing_median_age", placeholder="Housing Median Age", step="any", value="38"),
                Label("Total Rooms:"),
                Input(type="number", name="total_rooms", placeholder="Total Rooms", step="any", value="1568"),
                Label("Total Bedrooms:"),
                Input(type="number", name="total_bedrooms", placeholder="Total Bedrooms", step="any", value="351"),
                Label("Population:"),
                Input(type="number", name="population", placeholder="Population", step="any", value="710"),
                Label("Households:"),
                Input(type="number", name="households", placeholder="Households", step="any", value="339"),
                Label("Median Income:"),
                Input(type="number", name="median_income", placeholder="Median Income", step="any", value="2.7042"),
                Label("Ocean Proximity:"),
                Select(
                    Option("<1H OCEAN", value="<1H OCEAN", selected=True),
                    Option("INLAND", value="INLAND"),
                    Option("NEAR OCEAN", value="NEAR OCEAN"),
                    Option("NEAR BAY", value="NEAR BAY"),
                    Option("ISLAND", value="ISLAND"),
                    name="ocean_proximity"
                ),
                Input(type="submit", value="Predict"),
                hx_post="/predict",
                hx_target="#result"
            ),
            Div(id="result"),
            cls="container"
        )
    )

@rt('/predict')
def post(data: FormData):
    data = pd.DataFrame({
        'longitude': [data.longitude],
        'latitude': [data.latitude],
        'housing_median_age': [data.housing_median_age],
        'total_rooms': [data.total_rooms],
        'total_bedrooms': [data.total_bedrooms],
        'population': [data.population],
        'households': [data.households],
        'median_income': [data.median_income],
        'ocean_proximity': [data.ocean_proximity]
    })
    X_test_prepared = pipeline.transform(data)
    final_predictions = model.predict(X_test_prepared)
    return f"Predicted house value: ${final_predictions[0]:,.2f}"

serve()