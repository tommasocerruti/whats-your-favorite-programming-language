document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('languageForm');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const language = document.getElementById('language').value;

        await fetch('/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ language }),
        });

        updateChart();
    });

    let chart = null;

    async function updateChart() {
        const response = await fetch('/languages');
        const data = await response.json();

        const ctx = document.getElementById('languageChart').getContext('2d');

        if (chart) {
            chart.destroy();
        }

        chart = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: Object.keys(data),
                datasets: [{
                    label: 'Favorite Programming Languages',
                    data: Object.values(data),
                    backgroundColor: [
                        '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF',
                        '#FF9F40', '#FFCD56', '#FF6F61', '#6B5B95', '#D0A47A',
                    ],
                }],
            },
            options: {
                responsive: false,
                maintainAspectRatio: true,
            }
        });
    }

    updateChart();
});
