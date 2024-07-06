FROM node:18-alpine

WORKDIR /app

COPY . .

RUN chmod +x ./start.sh

RUN cd client && npm install && \
    cd ../server && npm install

ENV PORT=3000

EXPOSE 3000

RUN ls

CMD ["sh", "./start.sh", "production"]
