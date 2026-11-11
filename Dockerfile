# Stage 1: Build
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

# Stage 2: Production
FROM node:20-alpine

WORKDIR /app

ENV NODE_ENV=production

COPY package*.json ./
RUN npm ci

COPY --from=builder /app/public ./public
COPY --from=builder /app/src ./src
COPY --from=builder /app/build ./build

EXPOSE 3000

CMD ["npm", "start"]
