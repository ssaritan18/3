FROM node:20-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    python3 \
    make \
    g++ \
    && rm -rf /var/lib/apt/lists/*

RUN corepack enable && corepack prepare yarn@1.22.22 --activate

COPY package.json yarn.lock ./

RUN yarn install --frozen-lockfile --network-timeout 600000

COPY . .

ENV EXPO_USE_METRO_WORKSPACE_ROOT=1

EXPOSE 8081 19000 19001 19002

CMD ["yarn", "start", "--port", "8081", "--web"]
