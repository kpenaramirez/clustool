# import os

from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP
# from dash import DiskcacheManager, CeleryManager

from src.components.layout import create_layout
from src.data.loader import load_input_data
from src.data.source import DataSource

DATA_PATH = "./data/sample_data.csv"

# if "REDIS_URL" in os.environ:
#     # Use Redis & Celery if REDIS_URL set as an env variable
#     # https://dash.plotly.com/background-callbacks
#     from celery import Celery

#     celery_app = Celery(
#         __name__, broker=os.environ["REDIS_URL"], backend=os.environ["REDIS_URL"]
#     )
#     background_callback_manager = CeleryManager(celery_app)

# else:
#     # Diskcache for non-production apps when developing locally
#     import diskcache

#     cache = diskcache.Cache("./cache")
#     background_callback_manager = DiskcacheManager(cache)


def main() -> None:

    # load the data and create the data manager
    data = load_input_data(DATA_PATH)
    data = DataSource(data)

    app = Dash(
        external_stylesheets=[BOOTSTRAP],
        # background_callback_manager=background_callback_manager,
    )
    app.title = "Clustering tool"
    app.layout = create_layout(app, data)
    app.run()


if __name__ == "__main__":
    main()
