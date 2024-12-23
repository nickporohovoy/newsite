const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Укажите путь к папке с шаблонами
const templatesPath = path.join(__dirname, 'recipes', 'templates', 'recipes');

// Настройка статической папки для обслуживания файлов (CSS, JS, изображения, если есть)
app.use(express.static(templatesPath));

// Главная страница
app.get('/', (req, res) => {
    res.sendFile(path.join(templatesPath, 'home.html'));
});

// Страница добавления рецепта
app.get('/add-recipe', (req, res) => {
    res.sendFile(path.join(templatesPath, 'add_recipe.html'));
});

// Детализация рецепта
app.get('/recipe-detail', (req, res) => {
    res.sendFile(path.join(templatesPath, 'recipe_detail.html'));
});

// Запуск сервера
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
