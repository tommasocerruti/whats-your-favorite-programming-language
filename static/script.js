document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('languageForm');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const language = document.getElementById('language').value;

        try {
            const response = await fetch('/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ language }),
            });
            
            if (!response.ok) {
                throw new Error('Failed to submit');
            }
            
            updateChart();
        } catch (error) {
            console.error('Error submitting language:', error);
            alert('Failed to submit. Please try again.');
        }
    });

    let chart = null;

    async function updateChart() {
        try {
            const response = await fetch('/languages');
            if (!response.ok) {
                throw new Error('Failed to fetch data');
            }
            
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
                    maintainAspectRatio: false,
                    animation: false,
                }
            });
        } catch (error) {
            console.error('Error updating chart:', error);
        }
    }

    updateChart();
});