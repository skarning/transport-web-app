from transport import app

if __name__ == "__main__":
    """Uncomment for running locally"""
#     app.run(host="0.0.0.0")
    """ Uncomment for deployment"""
    app.run(host='0.0.0.0', port=80)
