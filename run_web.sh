# Serve app with gunicorn in the background
gunicorn run:app --config=./instance/gunicorn.py &

# Global search process gunicorn
# ps aux|grep gunicorn

#Restart gunicorn gracefully (with pid above as the parameter e.g. kill -SIGHUP 9527)
# kill -SIGHUP 