FROM python:3
ADD my_script.py /
RUN pip install psutil
RUN pip install pymongo
RUN pip install schedule
CMD [ "python", "./my_script.py" ]