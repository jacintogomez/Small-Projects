if [ $# -eq 0 ]; then
  read -p "Enter project name: " PROJECT_NAME
  read -p "Enter target directory (default: $HOME): " TARGET_DIR
  TARGET_DIR="${TARGET_DIR:-$HOME}"
elif [ $# -eq 1 ]; then
  PROJECT_NAME="$1"
  read -p "Enter target directory (default: $HOME): " TARGET_DIR
  TARGET_DIR="${TARGET_DIR:-$HOME}"
else
  PROJECT_NAME="$1"
  TARGET_DIR="$2"
fi

TASKS_FILE="$HOME/Downloads/tasks.txt"
TARGET_DIR_TOTAL_PATH="$HOME/$TARGET_DIR"

echo "Creating Project $PROJECT_NAME in $TARGET_DIR_TOTAL_PATH"

mkdir -p "$TARGET_DIR_TOTAL_PATH"
cd "$TARGET_DIR_TOTAL_PATH"
mkdir -p "$PROJECT_NAME"
cd "$PROJECT_NAME"
echo "Created Project in directory $TARGET_DIR_TOTAL_PATH/$PROJECT_NAME"

touch .env
echo "Created .env file"

echo ".env" > .gitignore
echo "Created .gitignore file"

if [ -f "$TASKS_FILE" ]; then
  cp "$TASKS_FILE" tasks.md
  echo "Created tasks.md from $TASKS_FILE"
else
  echo "#Tasks" > tasks.md
  echo "" >> tasks.md
  echo "Warning: $TASKS_FILE not found, created empty tasks.md"
fi