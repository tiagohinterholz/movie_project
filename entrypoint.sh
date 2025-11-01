#!/bin/bash
set -e

if [ ! -f "/aap/.env" ]; then
  echo "Criando arquivo .env..."
  cat <<EOF > .env
DEBUG=True
SECRET_KEY=$(openssl rand -hex 32)
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ORIGIN=http://localhost:5173

ENGINE_DB=django.db.backends.postgresql
NAME_DB=movies
USER_DB=root
PASSWORD_DB=rootroot
HOST_DB=db
PORT_DB=5432

TMDB_API_KEY=48911223dd3e848cb3b7a6b330fc8fa0
EOF
fi

echo "⏳ Aguardando banco de dados..."
while ! nc -z db 5432; do
  sleep 1
done
echo "✅ Banco disponível!"

echo "📦 Rodando migrações..."
export $(grep -v '^#' /app/.env | xargs)
python manage.py migrate --noinput

echo "👤 Verificando superusuário..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "admin123")
EOF

echo "🚀 Subindo servidor Django..."
exec "$@"
