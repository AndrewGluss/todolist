ToDoList
# Собираем образ 
docker build . -t todolist

# Запускаем контейнер в интерактивном фоновом режиме и портом 8000
docker run -it -d 8000:8000 todolist

# Список запущенных контейнеров
docker ps

# Остановка контейнера
docker stop {container_id}
