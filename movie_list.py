from app import create_app, cli

from pyfladesk import init_gui

app = create_app()
cli.register(app)

if __name__ == "__main__":
    # app.run()
    init_gui(app, port=8001, width=900, height=600, window_title='Movie List')
