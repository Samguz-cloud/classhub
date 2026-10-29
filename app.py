
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>ClassHub</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f2f5fc;
                color: #17264b;
            }
            header {
                background: #183477;
                color: white;
                padding: 22px 8%;
                font-size: 26px;
                font-weight: bold;
            }
            main {
                max-width: 1000px;
                margin: 40px auto;
                padding: 20px;
            }
            .hero {
                background: linear-gradient(120deg, #183477, #4169e1);
                color: white;
                padding: 38px;
                border-radius: 20px;
            }
            .hero h1 {
                font-size: 38px;
            }
            .hero p {
                line-height: 1.8;
            }
            .cards {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 18px;
                margin-top: 25px;
            }
            .card {
                background: white;
                padding: 23px;
                border-radius: 15px;
                border: 1px solid #e1e6f0;
            }
            .card p {
                color: #657089;
                line-height: 1.7;
            }
            footer {
                text-align: center;
                padding: 30px;
                color: #657089;
            }
            @media (max-width: 700px) {
                .cards {
                    grid-template-columns: 1fr;
                }
                .hero h1 {
                    font-size: 30px;
                }
            }
        </style>
    </head>
    <body>
        <header>ClassHub</header>
        <main>
            <section class="hero">
                <h1>Your classroom. One platform.</h1>
                <p>
                    Access lecture notes, answer quizzes,
                    and track your academic progress.
                    Learn together, wherever you are.
                </p>
                <strong>Our learning. Our progress. Our future.</strong>
            </section>
            <h2>Your Learning Dashboard</h2>
            <section class="cards">
                <article class="card">
                    <h3>Lecture Materials</h3>
                    <p>Lecturers share slides with students.</p>
                </article>
                <article class="card">
                    <h3>Online Quizzes</h3>
                    <p>Answer questions and earn points.</p>
                </article>
                <article class="card">
                    <h3>Class Leaderboard</h3>
                    <p>Track scores across different lectures.</p>
                </article>
            </section>
        </main>
        <footer>ClassHub | Our first Python project</footer>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=False)
