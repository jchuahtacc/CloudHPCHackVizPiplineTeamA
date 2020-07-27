FROM python:3.7-slim

EXPOSE 8050

RUN pip install dash==1.11.0 werkzeug==1.0.0 gunicorn==20.0.4 \
    plotly==4.6.0 us==1.0.0 pandas==1.0.3 xlrd==1.2.0 scipy==1.3.2 \
    openpyxl==3.0.3 memoization==0.2.3

COPY . /app
WORKDIR /app

RUN python collect.py

CMD ["gunicorn", "--preload", "-w 16", "-b :8050",  "-t 90", "app:server"]
