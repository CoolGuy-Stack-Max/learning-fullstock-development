# 使用官方 Node.js 镜像作为基础镜像
FROM node:18-alpine

# 设置工作目录
WORKDIR /app

# 复制 package.json 和 package-lock.json
COPY package.json package-lock.json ./

# 安装项目依赖
RUN npm install

# 复制所有文件到容器内
COPY . .

# 构建项目
RUN npm run build

# 使用 Nginx 镜像来托管前端应用
FROM nginx:alpine

# 删除默认的 Nginx 配置
RUN rm -rf /usr/share/nginx/html/*

# 复制构建的静态文件到 Nginx 默认路径
COPY --from=0 /app/dist /usr/share/nginx/html

# 暴露 80 端口
EXPOSE 80

# 启动 Nginx
CMD ["nginx", "-g", "daemon off;"]
