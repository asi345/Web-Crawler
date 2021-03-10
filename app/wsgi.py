## @file wsgi.py
# @author İsmail Ata İnan
# @brief Starts the webserver for the web application.

from app import application

if __name__ == "__main__" :
    application.run()
