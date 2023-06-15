#THIS MAKES THE FLASK WEBSITE RUN
from website import create_app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
#DONE MAKING THE FLASK WEBSITE RUN
 