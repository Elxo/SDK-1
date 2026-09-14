# Pinned to the exact Node LTS patch so every student builds an identical image.
FROM node:24.21.0-slim

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Prisma 7 resolves DATABASE_URL for every CLI command, `generate` included, so
# the client is generated at container start rather than during the image build
# (where no database is configured). Prisma 7 also no longer seeds implicitly -
# `db seed` must be invoked explicitly.
CMD sh -c "npx prisma generate && npx prisma migrate deploy && npx prisma db seed"
