# Pinned to the exact Node LTS patch so every student builds an identical image.
# Node 24 "Krypton" is the active LTS line (supported until 2028-04-30).
FROM node:24.21.0-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]
