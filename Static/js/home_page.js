const search = document.getElementById('searchInput');
const search_results = document.getElementById('results');
const prompt = document.createElement('p');
prompt.classList.add('prompt');

function update_results(results) {
    search_results.innerHTML = "";
    if (results.length === 0){
        search_results.appendChild(prompt);
        prompt.textContent = `No results found`;
    }
    else {
        results.forEach(result => {
            const book = document.createElement("a");
            const book_cover = document.createElement("img");
            const book_name = document.createElement("figcaption");
            book.classList.add('book');
            book_cover.classList.add('book-cover');
            book_name.classList.add('book-name');

            book_cover.setAttribute("src", `/static/media/book_covers/${result.cover_page}`);
            book.setAttribute("href", `/book/${result.book_id}`)
            book_name.textContent = `${result.title}`
            book.appendChild(book_cover);
            book.appendChild(book_name);
            search_results.appendChild(book);
        });
    }
}

search.addEventListener('input', async (e) => {
    const q = e.target.value;
    if (q.trim() === ""){
        search_results.innerHTML = "";
        return
    }
    try {
        const results = await fetch(`/book_search?search=${encodeURIComponent(q)}`);
        if (!results.ok){
            throw new Error("Failed to get data.");
        }
        const data = await results.json()
        update_results(data)
    }
    catch (Error){
        console.error("Error:", Error);
        search_results.innerHTML = "<p>Error fetching data.</p>";
    }
});