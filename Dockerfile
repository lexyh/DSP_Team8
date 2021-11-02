# To be filled by students
FROM python:3.8.2
WORKDIR /streamlit_app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . ./streamlit_app
EXPOSE 8501
CMD ["streamlit","run","app/streamlit_app.py"]