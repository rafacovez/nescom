FROM node:18-alpine

WORKDIR /app

COPY start.sh ./start.sh
COPY client ./client
COPY server ./server

RUN chmod +x ./start.sh

RUN cd client && npm install && \
    cd ../server && npm install

ENV PORT=3000

EXPOSE 3000

RUN ls

CMD ["sh", "./start.sh", "production"]
