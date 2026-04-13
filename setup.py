from setuptools import setup, find_packages

setup(
    name="nyc_taxi_trip_duration_prediction",
    version="0.1.0",
    description="Production ML pipeline for NYC Taxi Trip Duration Prediction",
    author="ancilcleetus",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.12",
    install_requires=[
        "pandas",
        "scikit-learn",
        "xgboost",
        "lightgbm",
        "fastapi",
        "uvicorn",
        "streamlit",
        "mlflow",
        "great-expectations",
        "plotly",
    ],
    extras_require={
        "dev": ["pytest"],
    },
)
