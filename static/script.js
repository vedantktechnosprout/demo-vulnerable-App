// Assume AJAX or form onsubmit, but for simplicity, alert on load (demo XSS payload: <script>alert(1)</script>)
document.addEventListener('DOMContentLoaded', function() {
    // In real: fetch results and do document.getElementById('results').innerHTML = response; // XSS vuln
    console.log('App loaded - test XSS by entering payload in form');
});
