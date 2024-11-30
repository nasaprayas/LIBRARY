const searchInput = document.getElementById('book_title');
const author = document.getElementById('author_name');
const shelf = document.getElementById('shelf_id');
const suggestionList = document.getElementById('suggestionList');

searchInput.addEventListener('input', async (e) => {
    const title = e.target.value;
    if (title.length > 2) { // Trigger suggestions after 2 characters
        try {
            const response = await fetch(`/book_search?search=${encodeURIComponent(title)}`);
            var suggestions = await response.json();
            suggestionList.innerHTML = '';
            suggestions.forEach(suggestion => {
                const li = document.createElement('li');
                li.textContent = suggestion.title;
                li.addEventListener('click', () => {
                    searchInput.value = suggestion.title;
                    author.value = suggestion.author;
                    shelf_id.value = suggestion.shelf_id;
                    suggestionList.innerHTML = ''; // Clear suggestions
                });
                suggestionList.appendChild(li);
            });
        } catch (error) {
            console.error('Error fetching suggestions:', error);
            suggestions = [];
        }
    } else {
        suggestionList.innerHTML = ''; // Clear suggestions
    }
});

