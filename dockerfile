FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN make install

ENV FLASK_ENV manage.py

EXPOSE 5000

CMD ["gunicorn", "-b", ":5000", "manage:app"]