FROM virajccx/custom-linux:latest

COPY . .
RUN pip3 install -r requirements.txt
CMD python3 bot
